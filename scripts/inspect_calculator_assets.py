"""Acquire public client scripts for static REA inspection; never execute target code."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor
import json
import hashlib
from scrapling.fetchers import Fetcher

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / 'research/local-calculator-assets'

class Scripts(HTMLParser):
    def __init__(self):
        super().__init__(); self.inside=False; self.inline=[]; self.urls=[]
    def handle_starttag(self, tag, attrs):
        if tag=='script':
            self.inside=True; a=dict(attrs)
            if a.get('src'):self.urls.append(a['src'])
    def handle_endtag(self, tag):
        if tag=='script':self.inside=False
    def handle_data(self, data):
        if self.inside and data.strip():self.inline.append(data)

def collect(url):
    r=Fetcher.get(url,timeout=30,retries=0)
    if r.status!=200:return {'url':url,'status':r.status}
    p=Scripts();p.feed(r.body.decode('utf-8',errors='replace'))
    slug=url.rsplit('/',1)[-1].replace('.html','')
    for i,script in enumerate(p.inline):
        (FOLDER / f'{slug}-{i}.js').write_text(script,encoding='utf-8')
    return {'url':url,'status':r.status,'inline_scripts':len(p.inline),'external_scripts':[urljoin(url,s) for s in p.urls],'sha256':hashlib.sha256(r.body).hexdigest()}

if __name__=='__main__':
    FOLDER.mkdir(exist_ok=True)
    r=json.loads((ROOT/'research/raw-calculator-index.json').read_text(encoding='utf-8'))
    import re
    text=''.join(r['structuredContent']['result'][0]['content'])
    urls=list(dict.fromkeys('https://www.calculator.net'+u for u in re.findall(r'\]\((/[a-z-]+-calculator\.html)\)',text)))
    urls=[u for u in urls if not any(x in u for x in ('fitness-and-health','financial-calculator','math-calculator','other-calculator'))]
    with ThreadPoolExecutor(max_workers=2) as pool: results=list(pool.map(collect,urls))
    (ROOT/'research/calculator-script-inventory.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
    print('Acquired public inline scripts for static inspection:',len(results))
