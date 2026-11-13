"""Build index.html from src/template.html, src/sheet.css and data/courses.json.
Run: python3 build.py"""
import json, pathlib
root = pathlib.Path(__file__).parent
tpl = (root/'src/template.html').read_text()
css = (root/'src/sheet.css').read_text()
data = json.loads((root/'data/courses.json').read_text())
for c in data:
    c['at'] = max((s.get('at') or 0) for s in c['sheets'])
js = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
out = tpl.replace('/*SHEETCSS*/', css).replace('"__DATA__"', js)
(root/'index.html').write_text(out)
print('index.html', len(out), 'bytes;', ', '.join(f"{c['code']}: {len(c['sheets'])}" for c in data))
