#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,re,yaml
ROOT=Path(__file__).resolve().parents[1]
VERSION=(ROOT/'VERSION').read_text(encoding='utf-8').strip()
MAX_FILES=160; MAX_BYTES=650000
REQUIRED=['00_START_HERE.md','MASTER_PROMPT.md','RUNTIME_MANIFEST.yaml','README.md','VERSION','LICENSE','RELEASE_NOTES-v0.3.0.md','FILE_MANIFEST.json','config/output-profiles.yaml','demo/virtue7-reference-implementation/demo-manifest.yaml']
FORBIDDEN_NAMES={'__MACOSX','.DS_Store','__pycache__'}

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    failures=[]
    for r in REQUIRED:
        if not (ROOT/r).exists(): failures.append('Missing required file: '+r)
    if VERSION!='0.3.0': failures.append('VERSION must be 0.3.0.')
    all_files=[p for p in ROOT.rglob('*') if p.is_file() and p.name!='FILE_MANIFEST.json' and '__pycache__' not in p.parts and p.suffix!='.pyc']
    for p in ROOT.rglob('*'):
        if any(part in FORBIDDEN_NAMES or part.startswith('._') for part in p.parts): failures.append('Forbidden metadata path: '+p.relative_to(ROOT).as_posix())
    if len(all_files)>MAX_FILES: failures.append(f'File limit exceeded: {len(all_files)} > {MAX_FILES}')
    size=sum(p.stat().st_size for p in all_files)
    if size>MAX_BYTES: failures.append(f'Size limit exceeded: {size} > {MAX_BYTES}')
    # Generic white-label checks: no embedded creator-profile identity records,
    # personal property registries, or creator-named kernel templates in the core.
    identity_path_markers=['public-baseline','creator-profile/properties','creator-profile/team']
    for p in all_files:
        rel=p.relative_to(ROOT).as_posix().lower()
        if any(marker in rel for marker in identity_path_markers):
            failures.append('Person-specific identity path in generic bundle: '+rel)
        if p.suffix.lower() in {'.md','.yaml','.yml','.json','.txt'}:
            text=p.read_text(encoding='utf-8',errors='ignore')
            if re.search(r'(?im)^creator_name:\s*(?![\[<{])\S+', text):
                failures.append('Hard-coded creator identity in '+rel)

    # v0.3 runtime behaviour checks.
    required_contract = {
        '00_START_HERE.md': ['Freestyle writing', 'Every produced artifact remains **Draft**', 'PDF', 'timezone'],
        'MASTER_PROMPT.md': ['## Freestyle intake', '## Artifact lifecycle', '## Delivery and file format', '## Locale and timezone'],
        'config/runtime.yaml': ['artifact_lifecycle:', 'file_delivery:', 'context_resolution:', 'freestyle:'],
        'capabilities/writing/manifest.yaml': ['freestyle:', 'capabilities/writing/routes/freestyle.md'],
        'README.md': ['Human-directed revision', 'Voice, location, and language', 'Output and export'],
    }
    for rel, needles in required_contract.items():
        text=(ROOT/rel).read_text(encoding='utf-8',errors='ignore') if (ROOT/rel).exists() else ''
        for needle in needles:
            if needle not in text: failures.append(f'Missing v0.3 runtime contract in {rel}: {needle}')

    # Generic reference safety: block direct imitation prompts and identity-linked test naming.
    unsafe_patterns=[r'(?i)in the style of\s+[A-Z]', r'(?i)write like\s+[A-Z]', r'(?i)sound like\s+[A-Z]']
    for p in all_files:
        rel=p.relative_to(ROOT).as_posix()
        if 'hig' in rel.lower(): failures.append('Residual identity-linked test naming: '+rel)
        if p.suffix.lower() in {'.md','.yaml','.yml','.json','.txt'}:
            text=p.read_text(encoding='utf-8',errors='ignore')
            for pattern in unsafe_patterns:
                if re.search(pattern,text): failures.append('Direct identity-imitation prompt in '+rel)

    manifest=json.loads((ROOT/'FILE_MANIFEST.json').read_text(encoding='utf-8')) if (ROOT/'FILE_MANIFEST.json').exists() else {}
    if manifest.get('version')!=VERSION: failures.append('Manifest version mismatch.')
    records={x['path']:x for x in manifest.get('files',[])}
    for p in all_files:
        rel=p.relative_to(ROOT).as_posix(); rec=records.get(rel)
        if not rec: failures.append('Missing manifest record: '+rel)
        elif rec.get('bytes')!=p.stat().st_size or rec.get('sha256')!=digest(p): failures.append('Manifest mismatch: '+rel)
    # core must not contain Virtue demo concept outside permitted root/reference documentation
    allowed_prefix='demo/virtue7-reference-implementation/'
    for p in all_files:
        rel=p.relative_to(ROOT).as_posix()
        if rel.startswith(allowed_prefix) or rel in {'README.md','00_START_HERE.md','CHANGELOG.md','RELEASE_NOTES-v0.3.0.md','GITHUB_RELEASE_CHECKLIST.md','MASTER_PROMPT.md','capabilities/review/routes/virtue7-demo.md'}: continue
        if p.suffix.lower() in {'.md','.yaml','.yml','.json'} and 'Pride → Humility' in p.read_text(encoding='utf-8',errors='ignore'):
            failures.append('Demo content leaked outside isolated demo: '+rel)
    if failures:
        print('Bundle validation failed:'); [print('- '+x) for x in failures]; return 1
    print('Bundle validation passed.'); print(f'Version: {VERSION}'); print(f'Files: {len(all_files)+1}'); print(f'Uncompressed bytes: {size+(ROOT/"FILE_MANIFEST.json").stat().st_size}')
    return 0
if __name__=='__main__': raise SystemExit(main())
