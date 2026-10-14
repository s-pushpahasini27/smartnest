(() => {
  'use strict';
  const form = document.querySelector('#auth-form');
  if (!form) return;
  const password = document.querySelector('#password');
  const confirm = document.querySelector('#confirm-password');
  const toggle = document.querySelector('.password-toggle');
  const feedback = document.querySelector('#auth-feedback');
  form.querySelector('[type="submit"]').disabled = false;
  toggle.addEventListener('click', () => {
    const visible = password.type === 'password';
    password.type = visible ? 'text' : 'password';
    toggle.textContent = visible ? 'Hide password' : 'Show password';
    toggle.setAttribute('aria-pressed', String(visible));
  });
  function validateMatch() {
    if (confirm) confirm.setCustomValidity(confirm.value && confirm.value !== password.value ? 'Your passwords don’t match. Please try again.' : '');
  }
  password.addEventListener('input', validateMatch);
  confirm?.addEventListener('input', validateMatch);
  form.addEventListener('submit', event => {
    event.preventDefault();
    validateMatch();
    if (!form.reportValidity()) return;
    // UI preview only. Never transmit or persist any entered credentials.
    password.value = '';
    password.type = 'password';
    if (confirm) confirm.value = '';
    toggle.textContent = 'Show password';
    toggle.setAttribute('aria-pressed', 'false');
    feedback.textContent = 'Form checked. This is a design preview, so no account was created and you haven’t been logged in.';
    feedback.hidden = false;
    feedback.focus();
  });
})();
