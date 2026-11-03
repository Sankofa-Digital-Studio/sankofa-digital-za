// ==========================================================================
// SANKOFA DIGITAL ZA — INTERACTIVE ENGINEERING SYSTEM
// ==========================================================================

// Global state
const header = document.querySelector('[data-header]');
const menuToggle = document.querySelector('[data-menu-toggle]');
const nav = document.querySelector('[data-nav]');
const progressBar = document.getElementById('scrollProgressBar');
const pageLoader = document.getElementById('pageLoader');
const backToTopBtn = document.getElementById('backToTopBtn');
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

// 1. GLOBAL INITIALIZATION & PAGE LOADER
window.addEventListener('DOMContentLoaded', () => {
  // Update dynamic year
  document.querySelectorAll('[data-year]').forEach((element) => {
    element.textContent = new Date().getFullYear();
  });

  // Fade out loader smoothly once DOM is ready or window loads
  const finishLoading = () => {
    if (pageLoader) {
      pageLoader.classList.add('loaded');
      setTimeout(() => pageLoader.remove(), 600);
    }
  };

  if (reduceMotion) finishLoading();
  else setTimeout(finishLoading, 450);
});

// Fallback in case DOMContentLoaded already fired
window.addEventListener('load', () => {
  if (pageLoader && !pageLoader.classList.contains('loaded')) {
    pageLoader.classList.add('loaded');
    setTimeout(() => pageLoader.remove(), 600);
  }
});

// 2. SCROLL PROGRESS BAR & HEADER SCROLLED STATE
const onScroll = () => {
  const scrollTop = window.scrollY || document.documentElement.scrollTop;
  const docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  const scrollPercent = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;

  if (progressBar) {
    progressBar.style.width = `${Math.min(100, Math.max(0, scrollPercent))}%`;
  }

  if (header) {
    header.classList.toggle('scrolled', scrollTop > 24);
  }

  if (backToTopBtn) {
    if (scrollTop > 500) {
      backToTopBtn.classList.add('visible');
    } else {
      backToTopBtn.classList.remove('visible');
    }
  }
};

window.addEventListener('scroll', onScroll, { passive: true });
onScroll();

// Back to top click handler
backToTopBtn?.addEventListener('click', () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
});

// 3. MOBILE MENU TOGGLE
menuToggle?.addEventListener('click', () => {
  const open = menuToggle.getAttribute('aria-expanded') === 'true';
  menuToggle.setAttribute('aria-expanded', String(!open));
  nav?.classList.toggle('open', !open);
  document.body.classList.toggle('menu-open', !open);
  if (!open) nav?.querySelector('a')?.focus();
});

nav?.querySelectorAll('a').forEach((link) => {
  link.addEventListener('click', () => {
    nav.classList.remove('open');
    menuToggle?.setAttribute('aria-expanded', 'false');
    document.body.classList.remove('menu-open');
  });
});

document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && nav?.classList.contains('open')) {
    nav.classList.remove('open');
    menuToggle?.setAttribute('aria-expanded', 'false');
    document.body.classList.remove('menu-open');
    menuToggle?.focus();
  }
});

// 4. INTERSECTION OBSERVER FOR REVEALS & STAT COUNTERS
if ('IntersectionObserver' in window) {
  // Elements reveal
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

  document.querySelectorAll('.reveal').forEach((el) => revealObserver.observe(el));

  // Stat counters animation
  const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const counterEl = entry.target;
        if (reduceMotion) {
          counterEl.textContent = counterEl.getAttribute('data-target-count') + (counterEl.getAttribute('data-suffix') || '');
        } else {
          animateCounter(counterEl);
        }
        counterObserver.unobserve(counterEl);
      }
    });
  }, { threshold: 0.25 });

  document.querySelectorAll('[data-target-count]').forEach((el) => counterObserver.observe(el));
} else {
  document.querySelectorAll('.reveal').forEach((el) => el.classList.add('visible'));
  document.querySelectorAll('[data-target-count]').forEach((el) => {
    el.textContent = el.getAttribute('data-target-count') + (el.getAttribute('data-suffix') || '');
  });
}

function animateCounter(el) {
  const target = parseInt(el.getAttribute('data-target-count'), 10) || 0;
  const suffix = el.getAttribute('data-suffix') || '';
  const duration = 1800; // ms
  const frameRate = 1000 / 60;
  const totalFrames = Math.round(duration / frameRate);
  let frame = 0;

  const timer = setInterval(() => {
    frame++;
    // Ease-out cubic
    const progress = frame / totalFrames;
    const easedProgress = 1 - Math.pow(1 - progress, 3);
    const currentVal = Math.round(easedProgress * target);

    el.textContent = `${currentVal}${suffix}`;

    if (frame >= totalFrames) {
      el.textContent = `${target}${suffix}`;
      clearInterval(timer);
    }
  }, frameRate);
}

// 5. LIVE CODE INTERPRETER / COMPILER SIMULATOR
const runCodeBtn = document.getElementById('runCodeBtn');
const codeOutput = document.getElementById('codeOutput');
const compilerPill = document.getElementById('compilerPill');
const terminalLogs = document.getElementById('terminalLogs');

if (runCodeBtn && codeOutput && compilerPill) {
  let isExecuting = false;

  runCodeBtn.addEventListener('click', () => {
    if (isExecuting) return;
    isExecuting = true;

    // Show compiler executing state
    runCodeBtn.disabled = true;
    runCodeBtn.innerHTML = `
      <span class="btn-spinner"></span>
      <span>Compiling...</span>
    `;
    compilerPill.textContent = 'COMPILING AST';
    compilerPill.className = 'compiler-pill compiling';

    if (terminalLogs) {
      terminalLogs.innerHTML = `
        <div class="terminal-line"><span class="log-dim">[1/3]</span> Loading African epistemological ruleset...</div>
      `;
    }

    setTimeout(() => {
      if (terminalLogs) {
        terminalLogs.innerHTML += `
          <div class="terminal-line"><span class="log-dim">[2/3]</span> Synthesizing ancestor lessons with modern runtime...</div>
        `;
      }
    }, 450);

    setTimeout(() => {
      if (terminalLogs) {
        terminalLogs.innerHTML += `
          <div class="terminal-line"><span class="log-dim">[3/3]</span> Verifying resilience under local load constraints...</div>
        `;
      }
    }, 850);

    setTimeout(() => {
      // Completed successfully
      compilerPill.textContent = 'SYSTEM ACTIVE';
      compilerPill.className = 'compiler-pill ready';
      
      codeOutput.innerHTML = `
        <div class="output-success-block">
          <div class="output-badge">✓ EXECUTION SUCCESSFUL (0.018s)</div>
          <div class="output-payload">
            <code>
            {\n
            &nbsp;&nbsp;"philosophy": "Sankofa - Se wo were fi na wosankofa a yenkyi",\n
            &nbsp;&nbsp;"status": "Uncompromised custom architecture",\n
            &nbsp;&nbsp;"verdict": "Sons of the soil build sovereign software",\n
            &nbsp;&nbsp;"legacyProtected": true\n
            }
            </code>
          </div>
        </div>
      `;

      runCodeBtn.disabled = false;
      runCodeBtn.innerHTML = `
        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg>
        <span>Re-run Build Logic</span>
      `;
      isExecuting = false;
    }, 1300);
  });
}

// 6. CONTACT FORM SIMULATION & ACTION HANDLERS
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
