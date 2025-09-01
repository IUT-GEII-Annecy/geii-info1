import os
import re
from shutil import copy2
from pathlib import Path

is_github_action = os.getenv("GITHUB_ACTIONS") == "true"

# Dossiers
if is_github_action:
    content_dir = Path("hugo-site/content/docs")
else:
    content_dir = Path("content/docs")
if not content_dir.exists():
    print(f"Content directory {content_dir} ... Creating it.")
    content_dir.mkdir(parents=True, exist_ok=True)

# Dossier pour les images statiques
if is_github_action:
    static_dir = Path("hugo-site/static/images")
else:
    static_dir = Path("static/images")
if not static_dir.exists():
    print(f"Static directory {static_dir} does not exist. Creating it.")
    static_dir.mkdir(parents=True, exist_ok=True)
else:
    print(f"Using existing static directory: {static_dir}")

# Dossier source des images
if is_github_action:
    img_src_dir = Path("obsidian-vault/Files")
else:
    img_src_dir = "Files"
if not os.path.exists(img_src_dir):
    print(f"Image source directory {img_src_dir} does not exist. Please check the path.")
    exit(1)

img_src_dir = "obsidian-vault/Files"

os.makedirs(static_dir, exist_ok=True)

# Regex
wikilink_re = re.compile(r"\[\[([^|\]]+)(\|([^\]]+))?\]\]")
img_re = re.compile(r'!\[(?!asciicast\])([^\]]+)\]\(([^)]+)\)')
asciicast = re.compile(r'!\[asciicast\]\((https?:\/\/[^)\/]+\/.*?)([^\/)]+)\.svg\)')
hint_re = re.compile(r'^>\s*\[!(\w+)\][-+]?\s?(.*)((?:\n>\s?.*)*)', re.MULTILINE | re.IGNORECASE)

def convert_checkboxes_to_shortcodes(content):
    # Convertir les cases à cocher Obsidian en shortcodes Hugo
    content = re.sub(r'- \[x\] (.+)', r'{{< checkbox checked="true" >}}\1{{< /checkbox >}}', content)
    content = re.sub(r'- \[ \] (.+)', r'{{< checkbox checked="false" >}}\1{{< /checkbox >}}', content)
    return content


#Ajoute le shortcode liste ul autour de l'ensemble des cases à cocher
def wrap_checkboxes_in_list(content):
    # Trouver toutes les cases à cocher et les envelopper dans une liste
    content = re.sub(r'(?:^{{< checkbox .*? >}}.*?{{< \/checkbox >}}.*\n?)+',
                      r'{{< ulcheck >}}\g<0>{{< /ulcheck >}}', content, flags=re.DOTALL)
    return content


def replace_hint(match):
    hint_type = match.group(1).lower()
    hint_text = match.group(2).strip()
    hint_details = match.group(3).strip()
    if hint_type == "todo":
        return f"> [!note]  \n> **À faire : {hint_text}**  \n{hint_details}"
    elif hint_type == "question": 
        hint_details = hint_details.replace('^> ', '', 1)  # Remove the first "> " from the details
        return f"{{{{< details \"Question : {hint_text}\" >}}}}\n{hint_details}\n{{{{< /details >}}}}"
    elif hint_type == "attention":
        return f"> [!note]  \n> **Cahier des charges : {hint_text}**  \n{hint_details}"
    else:
        return f"> [!{hint_type}]  \n> **{hint_text}**  \n{hint_details}"

def process_content(content):
    # Convert [[Page|Alias]] → [Alias](/cours/Page)
    content = wikilink_re.sub(lambda m: f"[{m.group(3) or m.group(1)}](/cours/{m.group(1)})", content)

    # Convert ![alt](path) → ![alt](/images/path)
    #content = img_re.sub(lambda m: f"![{m.group(1)}](/images/{os.path.basename(m.group(2))})", content)

    content = asciicast.sub(
    lambda m: f'<script src="{m.group(1)}{m.group(2)}.js" id="{m.group(2)}" async="true"></script>',content)



    return content

print("Starting conversion of Obsidian notes to Hugo format...")
print(f"Content directory: {content_dir}")
print(f"Static directory for images: {static_dir}")

for root, _, files in os.walk(content_dir):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(root, file)
            print(f"Processing file: {path}")
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
                print(f"Reading content from: {path}")

            # Convertir les hints et questions
            print("Converting hints and questions...")
            content = hint_re.sub(replace_hint, content)
            print("Hints and questions converted.")

            # Convertir les cases à cocher
            print("Converting checkboxes to shortcodes...") 
            content = convert_checkboxes_to_shortcodes(content)
            content = wrap_checkboxes_in_list(content)
            print("Checkboxes converted.")

            # Copier et corriger les images
            for alt_text, img_path in img_re.findall(content):
                full_img_path = os.path.join(img_src_dir, img_path)
                if os.path.exists(full_img_path):
                    copy2(full_img_path, static_dir)
                    print(f"Copied image: {full_img_path} → {static_dir}")
                    # Remplace uniquement l'URL dans la syntaxe Markdown
                    content = content.replace(f"({img_path})", f"(/images/{os.path.basename(img_path)})")
                else:
                    print(f"⚠ Image not found: {full_img_path}")

            # Transformer le contenu
            print("Processing links and asciicasts...")
            content = process_content(content)
            print("links and images done.")


            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

            print(f"Updated content written to: {path}")
