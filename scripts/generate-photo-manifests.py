#!/usr/bin/env python3
"""Regenerate assets/img/photos/{industry}/manifest.json from folder contents."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1] / 'assets' / 'img' / 'photos'
INDUSTRIES = ['retail', 'jewellery', 'hotel', 'restaurant', 'hospital']
EXCLUDE = re.compile(r'(necklace|rings|atmosphere|hero|blurry|manifest)', re.I)
EXT = re.compile(r'\.(png|jpe?g|webp|gif)$', re.I)


def score(name: str) -> int:
    n = name.lower()
    if 'pos' in n:
        return 0
    if 'dashboard' in n or 'availability' in n:
        return 1
    return 2


def main() -> int:
    for industry in INDUSTRIES:
        d = ROOT / industry
        if not d.is_dir():
            print(f'skip missing {industry}')
            continue
        images = []
        for f in d.iterdir():
            if not f.is_file() or not EXT.search(f.name) or EXCLUDE.search(f.name):
                continue
            images.append(
                {
                    'file': f.name,
                    'url': f'./assets/img/photos/{industry}/{f.name}',
                    'mtime': int(f.stat().st_mtime),
                }
            )
        images.sort(key=lambda x: (score(x['file']), x['file'].lower()))
        payload = {
            'ok': True,
            'industry': industry,
            'count': len(images),
            'images': images,
        }
        out = d / 'manifest.json'
        out.write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')
        print(f'{industry}: {len(images)} -> {out.relative_to(ROOT.parent.parent.parent)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
