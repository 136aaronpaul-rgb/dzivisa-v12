const CACHE_NAME = 'dzivisa-v25-2-aqua-working-1787902833';
const urlsToCache = [
  './',
  './index.html',
  './manifest.json',
  './icon-192.png',
  './icon-512.png',
  './wallpaper.png',
  './database.js',
  './engine.js',
  './runner.js',
  './code-engine.js',
  './override.js',
  './langs/dictionary.js',
  './plugins/loader.js',
  './plugins/power-ui.js',
  './plugins/reporter.js',
  './plugins/viral.js'
]

self.addEventListener('install', event => {
  event.waitUntil(caches.open(CACHE_NAME).then(cache => cache.addAll(urlsToCache)));
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil(caches.keys().then(keys => Promise.all(keys.map(k => k !== CACHE_NAME && caches.delete(k)))));
  self.clients.claim();
});

self.addEventListener('fetch', event => {
  event.respondWith(caches.match(event.request).then(res => res || fetch(event.request)));
});
