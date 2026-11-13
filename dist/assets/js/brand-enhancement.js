(() => {
  const heroCopy = document.querySelector('.reset-hero-copy');
  if (!heroCopy || heroCopy.querySelector('.hero-brand-logo')) return;

  const logo = document.createElement('img');
  logo.className = 'hero-brand-logo';
  logo.src = 'assets/images/sankofa-digital-logo-enhanced.webp';
  logo.alt = 'Sankofa Digital';
  logo.width = 1600;
  logo.height = 893;
  logo.decoding = 'async';
  logo.style.cssText = 'display:block;width:min(100%,22rem);height:auto;margin:0 0 clamp(1.5rem,4vw,2.75rem);border-radius:1rem;box-shadow:0 1.5rem 3rem rgba(23,25,22,.18)';
  heroCopy.prepend(logo);
})();
