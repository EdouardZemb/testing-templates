#!/usr/bin/env python3
import re
from pathlib import Path

YAML_PATH = Path('standards/references.yaml')
REQUIRED_FIELDS = {"key", "title", "identifier", "link", "tokens"}
ALLOWED_STATUS = {"published", "withdrawn", "superseded", "draft", "deprecated"}

pattern_entry = re.compile(r'^-\s+key:\s*(.*)$')
pattern_field = re.compile(r'^\s{2}([a-zA-Z_]+):\s*(.*)$')
pattern_token = re.compile(r'^\s{4}-\s*(.*)$')

errors = []
entries = []

if not YAML_PATH.exists():
    errors.append("standards/references.yaml introuvable")
else:
    current = None
    for raw in YAML_PATH.read_text().splitlines():
        if not raw.strip() or raw.strip().startswith('#'):
            continue
        m_entry = pattern_entry.match(raw)
        if m_entry:
            if current:
                entries.append(current)
            current = {"tokens": []}
            current['key'] = m_entry.group(1).strip('"')
            continue
        if current is None:
            continue
        m_field = pattern_field.match(raw)
        if m_field:
            field, value = m_field.groups()
            value = value.strip()
            if field == 'tokens':
                current['tokens'] = []
            elif value:
                current[field] = value.strip('"')
            else:
                current[field] = ""
            continue
        m_token = pattern_token.match(raw)
        if m_token:
            token = m_token.group(1).strip().strip('"')
            current.setdefault('tokens', []).append(token)
            continue
    if current:
        entries.append(current)

    seen = set()
    for idx, entry in enumerate(entries, 1):
        missing = REQUIRED_FIELDS - entry.keys()
        if missing:
            errors.append(f"Entrée #{idx} (key={entry.get('key')}) : champs manquants {sorted(missing)}")
        key = entry.get('key')
        if key in seen:
            errors.append(f"Clé dupliquée : {key}")
        else:
            seen.add(key)
        link = entry.get('link')
        if link and not link.startswith('http'):
            errors.append(f"Entrée {key} : lien invalide {link}")
        status = entry.get('status')
        if status and status not in ALLOWED_STATUS:
            errors.append(f"Entrée {key} : statut '{status}' non reconnu. Autorisés: {sorted(ALLOWED_STATUS)}")
        if not isinstance(entry.get('tokens'), list):
            errors.append(f"Entrée {key} : 'tokens' doit être une liste")

if errors:
    for err in errors:
        print(f"::error::{err}")
    raise SystemExit(1)

print("Validation de standards/references.yaml OK")
