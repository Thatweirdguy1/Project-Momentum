"""Collect public directory facts with Scrapling; keep unlicensed text/media local."""
from pathlib import Path
from urllib.parse import urljoin, urlsplit
from concurrent.futures import ThreadPoolExecutor
import csv
import json
import re
import shutil
import subprocess
import time
from scrapling.fetchers import Fetcher

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'data/exercises'
LOCAL = OUT / 'local-only'
SEEDS = ['https://www.jefit.com/exercises', 'https://www.muscleandstrength.com/exercises', 'https://www.acefitness.org/resources/everyone/exercise-library/']

def fetch(url):
    time.sleep(0.35)
    try:
        response = Fetcher.get(url, timeout=40, retries=0)
        return url, response
    except Exception as error:
        return url, str(error)

def main():
    LOCAL.mkdir(parents=True, exist_ok=True)
    repo = ROOT / 'local-exercises-dataset'
    commit = subprocess.check_output(['git', '-C', str(repo), 'rev-parse', 'HEAD'], text=True).strip()
    exercises = json.loads((repo / 'data/exercises.json').read_text(encoding='utf-8'))
    normalized = []
    for exercise in exercises:
        item = {k: v for k, v in exercise.items() if k not in ('image', 'gif_url')}
        item.update(source_repository='https://github.com/hasaneyldrm/exercises-dataset', source_commit=commit, text_license='MIT', media_included=False, media_license='Separate Gym visual license required')
        normalized.append(item)
    (OUT / 'exercises.json').write_text(json.dumps(normalized, ensure_ascii=False, separators=(',', ':')) + '\n', encoding='utf-8')
    for name in ('LICENSE', 'NOTICE.md'):
        shutil.copyfile(repo / name, OUT / ('upstream-' + name))
    facts, seen, failures, queue = {}, set(), [], list(SEEDS)
    # Follow observed listing/category/pagination links only; cap listing crawl explicitly.
    for wave in range(3):
        todo = [u for u in dict.fromkeys(queue) if u not in seen][:100]
        if not todo:
            break
        queue = []
        with ThreadPoolExecutor(max_workers=3) as pool:
            for url, response in pool.map(fetch, todo):
                seen.add(url)
                if isinstance(response, str) or response.status != 200:
                    failures.append({'url': url, 'error': response if isinstance(response, str) else response.status})
                    continue
                text = response.body.decode('utf-8', errors='replace')
                import hashlib
                (LOCAL / (hashlib.sha256(url.encode()).hexdigest()[:16] + '.html')).write_text(text, encoding='utf-8')
                for anchor in response.css('a'):
                    href = anchor.attrib.get('href', '')
                    absolute = urljoin(url, href).split('#')[0]
                    label = ' '.join(anchor.get_all_text().split())
                    host = urlsplit(absolute).netloc
                    path = urlsplit(absolute).path
                    is_detail = bool(host.endswith('jefit.com') and re.fullmatch(r'/exercises/\d+/[^/]+/?', path) or host.endswith('muscleandstrength.com') and path.startswith('/exercises/') and path.endswith('.html') or host.endswith('acefitness.org') and re.search(r'/exercise-library/\d+/', path))
                    if is_detail:
                        # Store bibliographic facts, not copied instruction prose or media.
                        facts[absolute] = {'source_url': absolute, 'name': path.rstrip('/').rsplit('/', 1)[-1].removesuffix('.html').replace('-', ' ').title(), 'discovered_from': url, 'detail_collected': False, 'license': 'Not established; reference only'}
                    elif host in [urlsplit(s).netloc for s in SEEDS] and ('/exercises' in path or '/exercise-library/' in path):
                        if absolute not in seen:
                            queue.append(absolute)
        print(f'Wave {wave + 1}: {len(seen)} listings, {len(facts)} exercise references', flush=True)
    # Representative details verify the shape of each source. Full instructions remain local.
    selected = []
    for host in ('jefit.com', 'muscleandstrength.com', 'acefitness.org'):
        selected.extend([u for u in facts if host in urlsplit(u).netloc][:8])
    with ThreadPoolExecutor(max_workers=3) as pool:
        for url, response in pool.map(fetch, selected):
            if isinstance(response, str) or response.status != 200:
                failures.append({'url': url, 'error': response if isinstance(response, str) else response.status})
                continue
            import hashlib
            (LOCAL / (hashlib.sha256(url.encode()).hexdigest()[:16] + '.html')).write_bytes(response.body)
            facts[url]['detail_collected'] = True
            h1 = response.css('h1::text').get()
            if h1:
                facts[url]['name'] = h1.strip()
            facts[url]['media_references'] = list(dict.fromkeys(urljoin(url, x) for x in response.css('video::attr(src), video source::attr(src), iframe::attr(src)').getall()))
    records = list(facts.values())
    (OUT / 'public-directory.json').write_text(json.dumps(records, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    summary = {'licensed_text_records': len(normalized), 'upstream_commit': commit, 'languages': sorted(normalized[0].get('instructions', {})), 'public_directory_records': len(records), 'listing_pages_fetched': len(seen), 'details_collected': sum(r['detail_collected'] for r in records), 'crawl_limits': 'Three listing waves, max 100 pages/wave; up to eight representative details per source; incomplete catalogs explicitly retained', 'failures': failures, 'media_redistributed': False, 'google_share_resolved_to': SEEDS[2]}
    (OUT / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(summary, indent=2), flush=True)

if __name__ == '__main__':
    main()
