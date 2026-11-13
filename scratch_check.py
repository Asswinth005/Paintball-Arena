
import glob, re
for f in ['index.html', 'home2.html', 'about.html', 'zones.html']:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    m = re.findall(r'([^{}]*glow-ember[^{}]*\{[^{}]*\})', c)
    print(f, m)
