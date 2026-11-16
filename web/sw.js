const CACHE='momentum-diary-v5';
const FILES=['./index.html','./diary.html','./tools.html','./style.css','./diary.css','./diary.mjs','./diary-model.mjs','./diary-store.mjs','./csv.mjs','./barcode.mjs','./app.mjs','./calculators/engine.mjs','./calculators/catalog.mjs','./manifest.webmanifest','./icon.svg','../data/nutrition/usda_macros.csv','../data/nutrition/usda_diary_micronutrients.csv'];
self.addEventListener('install',e=>e.waitUntil(caches.open(CACHE).then(c=>c.addAll(FILES)).then(()=>self.skipWaiting())));
self.addEventListener('activate',e=>e.waitUntil(self.clients.claim()));
const allowed=new Set(FILES.map(f=>new URL(f,self.location).href));
self.addEventListener('fetch',e=>{if(e.request.method!=='GET'||!allowed.has(e.request.url))return;e.respondWith(fetch(e.request).then(r=>{if(r.ok){const copy=r.clone();caches.open(CACHE).then(c=>c.put(e.request,copy));}return r;}).catch(()=>caches.match(e.request)));});
