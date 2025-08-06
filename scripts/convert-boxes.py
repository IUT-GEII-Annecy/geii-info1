import re
from pathlib import Path

# Dossier des fichiers Markdown
input_dir = Path("content")  # adapte selon ton projet

# Types de callouts reconnus
callout_types = ["tip", "info", "note", "warning", "danger", "quote"]

# Regex pour détecter les callouts Obsidian
callout_pattern = re.compile(r'^> \[!(\w+)\](?:- (.*))?', re.IGNORECASE)

def process_markdown(file_path):
    lines = file_path.read_text(encoding="utf-8").splitlines()
    output_lines = []
    i = 0
    while i < len(lines):
        match = callout_pattern.match(lines[i])
        if match:
            callout_type = match.group(1).lower()
            title = match.group(2) or callout_type.capitalize()

            if callout_type not in callout_types:
                output_lines.append(lines[i])
                i += 1
                continue

            # Commencer un bloc HTML
            output_lines.append(f'<div class="callout {callout_type}">')
            output_lines.append(f'<div class="callout-title">{title}</div>')
            output_lines.append('<div class="callout-content">')

            # Ajouter les lignes suivantes du callout
            i += 1
            while i < len(lines) and lines[i].startswith("> "):
                content = lines[i][2:]
                output_lines.append(content)
                i += 1

            output_lines.append('</div></div>')  # Fin du bloc callout
        else:
            output_lines.append(lines[i])
            i += 1

    file_path.write_text("\n".join(output_lines), encoding="utf-8")

# Appliquer à tous les fichiers Markdown
for md_file in input_dir.rglob("*.md"):
    process_markdown(md_file)
