import os, re
from shutil import copy2

content_dir = "hugo-site/content/cours"
static_dir = "hugo-site/static/images"
os.makedirs(static_dir, exist_ok=True)

link_re = re.compile(r"\[\[([^|\]]+)(\|([^\]]+))?\]\]")

for root, _, files in os.walk(content_dir):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            content = link_re.sub(lambda m: f"[{m.group(3) or m.group(1)}](/cours/{m.group(1)})", content)

            for img_path in re.findall(r'!\[.*?\]\((.*?)\)', content):
                full_img_path = os.path.join(root, img_path)
                if os.path.exists(full_img_path):
                    copy2(full_img_path, static_dir)

            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
