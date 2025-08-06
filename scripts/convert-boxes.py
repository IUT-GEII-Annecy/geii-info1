import re
from pathlib import Path

# Dossier des fichiers Markdown
input_dir = Path("hugo-site/content")  # adapte selon ton projet

# Types de callouts reconnus
callout_types = ["tip", "info", "note", "warning", "danger", "quote", "todo"]

# Regex pour détecter les callouts Obsidian
callout_pattern = re.compile(r'^> \[!(\w+)\]\s*([+-]?)\s*(.*)?$', re.IGNORECASE)

def process_markdown(file_path):
    lines = file_path.read_text(encoding="utf-8").splitlines()
    output_lines = []
    i = 0
    while i < len(lines):
        match = callout_pattern.match(lines[i])
        
        if match:
            callout_type = match.group(1).lower()
            retractable = match.group(2) == "+" or match.group(2) == "-"
            opened = match.group(2) == "+"
            callout_title = match.group(3) or callout_type.capitalize()

            print(f"Processing callout: {callout_type}, retractable: {retractable}, title: {callout_title}") # Debugging output

            if callout_type not in callout_types:
                output_lines.append(lines[i])
                i += 1
                continue


            # Commencer un bloc shortcode Hugo
            if retractable:
                output_lines.append(f'{{{{< callout type="{callout_type}" title="{callout_title}" retractable="true" open="{opened}" >}}}}')
            else:
                output_lines.append(f'{{{{< callout type="{callout_type}" title="{callout_title}" >}}}}')

            # Ajouter les lignes suivantes du callout
            i += 1
            while i < len(lines) and lines[i].startswith("> "):
                content = lines[i][2:]
                output_lines.append(content)
                i += 1

            # Fin du bloc shortcode
            output_lines.append(f'{{{{< /callout >}}}}')

        else:
            output_lines.append(lines[i])
            i += 1

    file_path.write_text("\n".join(output_lines), encoding="utf-8")

def convert_checkboxes_to_shortcodes(file_path):
    content = file_path.read_text(encoding="utf-8")
    # Convertir les cases à cocher Obsidian en shortcodes Hugo
    content = re.sub(r'- \[x\] (.+)', r'{{< checkbox checked="true" >}}\1{{< /checkbox >}}', content)
    content = re.sub(r'- \[ \] (.+)', r'{{< checkbox checked="false" >}}\1{{< /checkbox >}}', content)
    file_path.write_text(content, encoding="utf-8")


# Appliquer à tous les fichiers Markdown
for md_file in input_dir.rglob("*.md"):
    process_markdown(md_file)
    convert_checkboxes_to_shortcodes(md_file)
