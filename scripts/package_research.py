"""Publish only public media references and bounded collection metadata from local captures."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urljoin
import json

ROOT = Path(__file__).resolve().parents[1]

class Media(HTMLParser):
    def __init__(self, url):
        super().__init__()
        self.url, self.items = url, []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ('video', 'source', 'iframe'):
            for key in ('src', 'data-src', 'poster'):
                value = a.get(key, '')
                if value and not value.startswith('data:'):
                    self.items.append({'element': tag, 'attribute': key, 'url': urljoin(self.url, value), 'downloaded': False, 'license': 'not established'})

def responses(path):
    wrapper = json.loads(path.read_text(encoding='utf-8'))
    for block in wrapper.get('content', []):
        if block.get('type') == 'text':
            value = json.loads(block['text'])
            if 'url' in value:
                yield value

if __name__ == '__main__':
    records = []
    for value in responses(ROOT / 'research/raw-html.json'):
        parser = Media(value['url'])
        parser.feed('\n'.join(value.get('content', [])))
        records.append({'requested_url': value['url'], 'http_status': value['status'], 'collected_date': '2026-11-16', 'method': 'Scrapling bulk_get; public HTML only', 'media_references': parser.items, 'coverage': 'Elements exposed in this response only; no in-app catalog or video download'})
    target = ROOT / 'research/media-inventory.json'
    target.write_text(json.dumps(records, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f'Published metadata for {len(records)} public pages; {sum(len(r["media_references"]) for r in records)} media references.')
