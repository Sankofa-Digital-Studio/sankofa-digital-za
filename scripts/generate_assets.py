import os

def create_africa_map():
    points = [
        # North coast
        (100, 30), (140, 20), (180, 22), (210, 35), (230, 40), (250, 65),
        # Red Sea / Horn of Africa
        (240, 95), (265, 115), (290, 140), (280, 160), (250, 175),
        # East coast
        (235, 195), (230, 220), (220, 255), (200, 290),
        # South Africa / Cape
        (175, 330), (150, 340), (135, 325),
        # West coast south to bight
        (120, 290), (115, 250), (120, 215), (100, 200), (70, 195),
        # Gulf of Guinea / West Africa bulge
        (50, 190), (30, 180), (15, 165), (10, 140), (15, 110), (35, 85),
        # Northwest / Morocco
        (60, 50), (85, 40), (100, 30)
    ]

    def point_inside_polygon(x, y, poly):
        n = len(poly)
        inside = False
        p1x, p1y = poly[0]
        for i in range(n + 1):
            p2x, p2y = poly[i % n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y
        return inside

    dots = []
    grid_spacing = 8
    for y in range(25, 340, grid_spacing):
        for x in range(15, 290, grid_spacing):
            if point_inside_polygon(x, y, points):
                dots.append((x, y))

    madagascar_points = [(260, 240), (275, 235), (285, 270), (270, 295), (255, 265)]
    for y in range(235, 295, grid_spacing):
        for x in range(255, 285, grid_spacing):
            if point_inside_polygon(x, y, madagascar_points):
                dots.append((x, y))

    path_d = 'M ' + ' L '.join(f'{x},{y}' for x, y in points) + ' Z'

    lines = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 310 360" fill="none" role="img" aria-label="African continent digital network map">',
        '  <defs>',
        '    <filter id="africaGlow" x="-30%" y="-30%" width="160%" height="160%">',
        '      <feGaussianBlur stdDeviation="3" result="blur" />',
        '      <feMerge>',
        '        <feMergeNode in="blur" />',
        '        <feMergeNode in="SourceGraphic" />',
        '      </feMerge>',
        '    </filter>',
        '  </defs>',
        f'  <path d="{path_d}" stroke="rgba(232,163,29,0.28)" stroke-width="1.2" stroke-dasharray="3 3" fill="rgba(232,163,29,0.03)" />',
        '  <path d="M 260,240 L 275,235 L 285,270 L 270,295 L 255,265 Z" stroke="rgba(232,163,29,0.28)" stroke-width="1.2" stroke-dasharray="3 3" fill="rgba(232,163,29,0.03)" />',
        '  <g fill="#e8a31d">'
    ]

    hubs = [(165, 330), (55, 160), (250, 170), (210, 50), (35, 140)]
    for i in range(len(hubs)):
        for j in range(i+1, len(hubs)):
            x1, y1 = hubs[i]
            x2, y2 = hubs[j]
            lines.append(f'    <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="rgba(255,215,0,0.3)" stroke-width="0.8" stroke-dasharray="3 4" />')

    for x, y in dots:
        is_hub = any(abs(x - hx) < 10 and abs(y - hy) < 10 for hx, hy in hubs)
        if is_hub:
            lines.append(f'    <circle cx="{x}" cy="{y}" r="3.2" fill="#ffd54f" filter="url(#africaGlow)" />')
            lines.append(f'    <circle cx="{x}" cy="{y}" r="6" stroke="rgba(255,213,79,0.4)" stroke-width="0.8" fill="none" />')
        else:
            op = 0.45 + ((x * 11 + y * 17) % 50) / 100.0
            r = 1.9 if ((x + y) % 3 == 0) else 1.35
            lines.append(f'    <circle cx="{x}" cy="{y}" r="{r}" opacity="{op:.2f}" fill="#e8a31d" />')

    lines.append('  </g>')
    lines.append('</svg>')

    os.makedirs('dist/assets/icons', exist_ok=True)
    with open('dist/assets/icons/africa-map.svg', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print('Generated dist/assets/icons/africa-map.svg')

if __name__ == '__main__':
    create_africa_map()
