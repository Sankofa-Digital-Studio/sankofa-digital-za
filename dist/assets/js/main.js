const header = document.querySelector('[data-header]');
const menuToggle = document.querySelector('[data-menu-toggle]');
const nav = document.querySelector('[data-nav]');

const setHeader = () => header?.classList.toggle('scrolled', window.scrollY > 24);
setHeader();
window.addEventListener('scroll', setHeader, { passive: true });

menuToggle?.addEventListener('click', () => {
  const open = menuToggle.getAttribute('aria-expanded') === 'true';
  menuToggle.setAttribute('aria-expanded', String(!open));
  nav?.classList.toggle('open', !open);
  document.body.classList.toggle('menu-open', !open);
});

nav?.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => {
  nav.classList.remove('open');
  menuToggle?.setAttribute('aria-expanded', 'false');
  document.body.classList.remove('menu-open');
}));

document.querySelectorAll('[data-year]').forEach((element) => {
  element.textContent = new Date().getFullYear();
});

if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });
  document.querySelectorAll('.reveal').forEach((element) => observer.observe(element));
} else {
  document.querySelectorAll('.reveal').forEach((element) => element.classList.add('visible'));
}

const form = document.querySelector('[data-enquiry-form]');
const status = document.querySelector('[data-form-status]');

const enquiryText = (data) => [
  `Website enquiry from ${data.get('name') || ''}`,
  '',
  `Name: ${data.get('name') || ''}`,
  `Email: ${data.get('email') || ''}`,
  `Organisation: ${data.get('organisation') || 'Not supplied'}`,
  `Project type: ${data.get('projectType') || 'Not selected'}`,
  `Project stage: ${data.get('stage') || 'Not selected'}`,
  '',
  'Problem or opportunity:',
  data.get('message') || ''
].join('\n');

form?.addEventListener('submit', (event) => {
  event.preventDefault();
  if (!form.reportValidity()) return;
  const data = new FormData(form);
  const subject = encodeURIComponent(`Sankofa Digital ZA enquiry from ${data.get('name')}`);
  const body = encodeURIComponent(enquiryText(data));
  if (status) status.textContent = 'Opening your email application with the enquiry prepared.';
  window.location.href = `mailto:sankofa.digital.studios@gmail.com?subject=${subject}&body=${body}`;
});

document.querySelector('[data-whatsapp-enquiry]')?.addEventListener('click', () => {
  if (!form || !form.reportValidity()) return;
  const data = new FormData(form);
  const message = encodeURIComponent(enquiryText(data));
  if (status) status.textContent = 'Opening WhatsApp with the enquiry prepared.';
  window.open(`https://wa.me/27754654865?text=${message}`, '_blank', 'noopener,noreferrer');
});
