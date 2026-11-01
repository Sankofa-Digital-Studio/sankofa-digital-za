import os

def generate_svg_icons():
    icons_dir = 'dist/assets/icons'
    os.makedirs(icons_dir, exist_ok=True)

    # 1. Sankofa Bird Emblem (Detailed Adinkra Gold Bird)
    sankofa_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none" role="img" aria-label="Sankofa Bird Emblem">
  <defs>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffe082" />
      <stop offset="50%" stop-color="#f59e0b" />
      <stop offset="100%" stop-color="#b45309" />
    </linearGradient>
  </defs>
  <!-- Tail feathers fanned out -->
  <path d="M 30,55 C 24,52 14,56 12,65 C 10,72 17,76 25,73 C 27,67 29,61 30,55 Z" fill="url(#goldGrad)" opacity="0.9" />
  <path d="M 27,62 C 20,62 12,69 13,78 C 15,85 24,86 31,80 C 31,74 29,68 27,62 Z" fill="url(#goldGrad)" opacity="0.8" />
  <path d="M 32,71 C 26,75 19,83 23,91 C 27,97 37,94 40,84 C 37,79 34,75 32,71 Z" fill="url(#goldGrad)" opacity="0.95" />
  <!-- Bird Body -->
  <path d="M 40,48 C 30,55 30,78 48,82 C 64,85 76,75 75,58 C 74,45 63,38 52,38 C 45,38 41,43 40,48 Z" fill="url(#goldGrad)" />
  <!-- Wing Adinkra Geometry Cutouts -->
  <path d="M 45,55 C 40,58 40,68 47,72 C 55,75 65,70 65,60 C 65,52 56,48 48,50 Z" fill="#090a0b" />
  <circle cx="53" cy="61" r="4.5" fill="url(#goldGrad)" />
  <rect x="58" y="55" width="4" height="10" rx="1.5" fill="url(#goldGrad)" />
  <rect x="44" y="57" width="3.5" height="7" rx="1" fill="url(#goldGrad)" />
  <!-- Elegant backward-turned Neck and Head -->
  <path d="M 54,39 C 64,39 74,32 74,22 C 74,12 62,8 52,14 C 44,19 44,28 49,32 C 51,34 53,37 54,39 Z" fill="url(#goldGrad)" />
  <!-- Eye -->
  <circle cx="60" cy="18" r="2.2" fill="#090a0b" />
  <!-- Beak & Egg -->
  <path d="M 68,20 L 75,23 L 69,25 Z" fill="url(#goldGrad)" />
  <ellipse cx="76" cy="27" rx="4" ry="5.5" fill="url(#goldGrad)" stroke="#ffd54f" stroke-width="1" />
  <!-- Sturdy Perched Legs -->
  <path d="M 50,82 L 48,93 L 42,95 M 48,93 L 49,95 M 48,93 L 54,95" stroke="url(#goldGrad)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />
  <path d="M 62,80 L 64,93 L 58,95 M 64,93 L 65,95 M 64,93 L 70,95" stroke="url(#goldGrad)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />
</svg>'''

    with open(f'{icons_dir}/sankofa-bird.svg', 'w', encoding='utf-8') as f:
        f.write(sankofa_svg)
    with open(f'{icons_dir}/logo-mark.svg', 'w', encoding='utf-8') as f:
        f.write(sankofa_svg)

    # 2. Vector Icons for Services
    # Web Dev
    with open(f'{icons_dir}/icon-web.svg', 'w', encoding='utf-8') as f:
        f.write('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#e8a31d" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>''')

    # Mobile Apps
    with open(f'{icons_dir}/icon-mobile.svg', 'w', encoding='utf-8') as f:
        f.write('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#e8a31d" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="2" width="14" height="20" rx="2.5" ry="2.5"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg>''')

    # Cloud Solutions
    with open(f'{icons_dir}/icon-cloud.svg', 'w', encoding='utf-8') as f:
        f.write('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#e8a31d" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"/></svg>''')

    # Data & Analytics
    with open(f'{icons_dir}/icon-analytics.svg', 'w', encoding='utf-8') as f:
        f.write('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#e8a31d" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/><polyline points="4 9 10 5 15 10 20 4"/><polyline points="16 4 20 4 20 8"/></svg>''')

    # Cybersecurity
    with open(f'{icons_dir}/icon-security.svg', 'w', encoding='utf-8') as f:
        f.write('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#e8a31d" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><circle cx="12" cy="11" r="2"/><path d="M12 13v3"/></svg>''')

    # IT Consulting
    with open(f'{icons_dir}/icon-consulting.svg', 'w', encoding='utf-8') as f:
        f.write('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#e8a31d" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>''')

    # 3. Vector Icons for Pillars
    # Innovation: Lightbulb
    with open(f'{icons_dir}/icon-innovation.svg', 'w', encoding='utf-8') as f:
        f.write('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#e8a31d" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18h6"/><path d="M10 22h4"/><path d="M12 2v2"/><path d="M4.93 4.93l1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="M17.66 6.34l1.41-1.41"/><path d="M15 14v-2a3 3 0 0 0-6 0v2"/></svg>''')

    # Impact: Community
    with open(f'{icons_dir}/icon-impact.svg', 'w', encoding='utf-8') as f:
        f.write('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#e8a31d" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>''')

    # 4. Vector Icons for Process
    # 01 Discover: Chat bubble
    with open(f'{icons_dir}/icon-discover.svg', 'w', encoding='utf-8') as f:
        f.write('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#e8a31d" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/><circle cx="8" cy="10" r="1" fill="#e8a31d"/><circle cx="12" cy="10" r="1" fill="#e8a31d"/><circle cx="16" cy="10" r="1" fill="#e8a31d"/></svg>''')

    # 02 Plan: Clipboard / notebook with pen
    with open(f'{icons_dir}/icon-plan.svg', 'w', encoding='utf-8') as f:
        f.write('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#e8a31d" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><line x1="10" y1="9" x2="8" y2="9"/></svg>''')

    # 03 Build: Code brackets
    with open(f'{icons_dir}/icon-build.svg', 'w', encoding='utf-8') as f:
        f.write('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#e8a31d" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/><line x1="14" y1="4" x2="10" y2="20"/></svg>''')

    # 04 Launch: Rocket
    with open(f'{icons_dir}/icon-launch.svg', 'w', encoding='utf-8') as f:
        f.write('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#e8a31d" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="M12 15l-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-2.05 11a22.77 22.77 0 0 1-3.95 2z"/><path d="M9 12l2 2"/></svg>''')

    # 5. Stats Icons
    # Projects
    with open(f'{icons_dir}/icon-projects.svg', 'w', encoding='utf-8') as f:
        f.write('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#e8a31d" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>''')

    # Happy Clients: Smile
    with open(f'{icons_dir}/icon-clients.svg', 'w', encoding='utf-8') as f:
        f.write('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#e8a31d" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/></svg>''')

    # Industries Served: Globe
    with open(f'{icons_dir}/icon-industries.svg', 'w', encoding='utf-8') as f:
        f.write('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#e8a31d" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>''')

    # Commitment: Award Medal
    with open(f'{icons_dir}/icon-commitment.svg', 'w', encoding='utf-8') as f:
        f.write('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#e8a31d" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg>''')

    print('All SVG icons generated in dist/assets/icons/')

if __name__ == '__main__':
    generate_svg_icons()
