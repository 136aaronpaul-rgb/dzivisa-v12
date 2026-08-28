const CACHE_NAME = 'dzivisa-v25-2-WORKING-FINAL-1787903133';
const urlsToCache = [
  './',
  './index.html?v=dzivisa-v25-2-WORKING-FINAL-1787903133',
  './manifest.json?v=dzivisa-v25-2-WORKING-FINAL-1787903133',
  './icon-192.png',
  './icon-512.png',
  './database.js?v=dzivisa-v25-2-WORKING-FINAL-1787903133',
  './engine.js?v=dzivisa-v25-2-WORKING-FINAL-1787903133',
  './override.js?v=dzivisa-v25-2-WORKING-FINAL-1787903133'
];
self.addEventListener('install', event => {
  event.waitUntil(caches.open(CACHE_NAME).then(cache => cache.addAll(urlsToCache)));
  self.skipWaiting();
});
self.addEventListener('activate', event => {
  event.waitUntil(caches.keys().then(keys => Promise.all(keys.map(k => k !== CACHE_NAME && caches.delete(k)))));
  self.clients.claim();
});
self.addEventListener('fetch', event => {
  event.respondWith(caches.match(event.request).then(res => res || fetch(event.request, {cache: 'no-store'})));
});
