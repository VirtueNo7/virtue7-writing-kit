#!/usr/bin/env python3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
EXPECTED="""# What are we doing now?

1. **Chat**
2. **Create content**
3. **Automate a task**

Or tell me what you want to make or do."""
text=(ROOT/'00_START_HERE.md').read_text(encoding='utf-8')
start=text.split('<!-- BOOT_MENU_START -->',1)[1].split('<!-- BOOT_MENU_END -->',1)[0].strip()
fail=[]
if start != EXPECTED: fail.append('Boot menu does not match the exact v0.5.0 contract.')
for token in ['Build an agent','Find a ' + 'boun' + 'ty']:
    if token.lower() in start.lower(): fail.append(f'Removed boot entry still present: {token}')
if fail:
    print('Boot contract failed:'); [print('- '+x) for x in fail]; raise SystemExit(1)
print('Boot contract passed.')
