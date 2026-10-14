(() => {
'use strict';
const status = document.querySelector('#status');
let timer;
function announce(message) {
  status.textContent = message; status.classList.add('visible');
  clearTimeout(timer); timer = setTimeout(() => status.classList.remove('visible'), 3500);
}
const storageKey = 'smartnest.saved.v1';
let saved = new Set();
try {
  const ids = JSON.parse(localStorage.getItem(storageKey) || '[]');
  if (Array.isArray(ids)) saved = new Set(ids.filter(id => Number.isInteger(id) && id > 0));
} catch { announce('Saved homes are unavailable in this browser.'); }
function refresh() {
  document.querySelectorAll('.saved-count').forEach(el => el.textContent = saved.size);
  document.querySelectorAll('[data-save]').forEach(button => {
    const active = saved.has(Number(button.dataset.save));
    button.setAttribute('aria-pressed', String(active));
    if (button.hasAttribute('data-save-label')) button.textContent = active ? '♥ Saved home' : '♡ Save home';
    else { button.textContent = active ? '♥' : '♡'; button.setAttribute('aria-label', (active ? 'Unsave ' : 'Save ') + button.closest('article').querySelector('h3').textContent); }
  });
  const grid = document.querySelector('[data-saved-only]');
  if (grid?.dataset.savedOnly === 'true') {
    let count = 0;
    grid.querySelectorAll('[data-property-id]').forEach(card => {card.hidden = !saved.has(Number(card.dataset.propertyId)); if (!card.hidden) count++;});
    document.querySelector('#result-count').textContent = count;
    document.querySelector('#result-noun').textContent = count === 1 ? 'home' : 'homes';
    document.querySelector('#empty-state').hidden = count > 0;
  }
}
document.querySelectorAll('[data-save]').forEach(button => button.addEventListener('click', () => {
  const id = Number(button.dataset.save), active = saved.has(id);
  const next = new Set(saved); active ? next.delete(id) : next.add(id);
  try { localStorage.setItem(storageKey, JSON.stringify([...next])); saved = next; refresh(); announce(active ? 'Home removed from your shortlist.' : 'Home saved to your shortlist.'); }
  catch { announce('Could not save. Please allow browser storage and try again.'); }
}));
window.addEventListener('storage', event => {
  if (event.key !== storageKey) return;
  try { const ids = JSON.parse(event.newValue || '[]'); saved = new Set(Array.isArray(ids) ? ids.filter(Number.isInteger) : []); refresh(); } catch {}
});
refresh();
const state = document.querySelector('#state'), city = document.querySelector('#city');
if (state && city) {
  const cities = JSON.parse(document.querySelector('#cities-data').textContent);
  function updateCities() {
    const previous = city.value;
    city.replaceChildren(new Option('All cities', ''));
    const names = state.value ? cities[state.value] || [] : Object.values(cities).flat();
    names.forEach(name => city.add(new Option(name, name)));
    city.value = names.includes(previous) ? previous : '';
  }
  state.addEventListener('change', updateCities); updateCities();
}
document.querySelectorAll('[data-property-image]').forEach(img => {
  function fallback() { img.hidden = true; img.parentElement.classList.add('image-unavailable'); const text = document.createElement('span'); text.className = 'fallback-label'; text.textContent = '⌂  Photo unavailable'; img.parentElement.append(text); }
  img.addEventListener('error', fallback, {once:true});
  if (img.complete && img.naturalWidth === 0) fallback();
});
const form = document.querySelector('#emi-form');
if (form) {
  function calculate() {
    if (!form.reportValidity()) return;
    const principal = Number(form.dataset.price) * (1 - Number(document.querySelector('#down-payment').value) / 100);
    const rate = Number(document.querySelector('#interest').value) / 1200;
    const months = Number(document.querySelector('#years').value) * 12;
    const monthly = rate === 0 ? principal / months : principal * rate / (1 - Math.pow(1 + rate, -months));
    document.querySelector('#emi').textContent = '₹' + Math.round(monthly).toLocaleString('en-IN') + ' / month';
  }
  form.addEventListener('submit', event => { event.preventDefault(); calculate(); }); calculate();
}
document.querySelector('#share-home')?.addEventListener('click', async () => {
  try {
    if (navigator.share) await navigator.share({title: document.title, url: location.href});
    else { await navigator.clipboard.writeText(location.href); announce('Link copied to clipboard.'); }
  } catch (error) { if (error.name !== 'AbortError') announce('Copy the page address to share this home.'); }
});
})();
