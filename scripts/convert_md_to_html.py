"""
convert_md_to_html.py — Chuyển tất cả file .md trong outputs/ thành .html để xem trong browser.
Dùng: python3 scripts/convert_md_to_html.py
"""
import markdown
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIRS = [
    os.path.join(BASE_DIR, "outputs", "research"),
    os.path.join(BASE_DIR, "outputs", "blog"),
]

CSS = """
<style>
  body { font-family: 'Segoe UI', sans-serif; max-width: 900px; margin: 40px auto; padding: 0 24px; color: #222; line-height: 1.7; }
  h1 { color: #1a3c6e; border-bottom: 3px solid #1a3c6e; padding-bottom: 10px; }
  h2 { color: #1a3c6e; margin-top: 36px; border-left: 4px solid #f0a500; padding-left: 12px; }
  h3 { color: #333; margin-top: 24px; }
  table { border-collapse: collapse; width: 100%; margin: 16px 0; font-size: 14px; }
  th { background: #1a3c6e; color: white; padding: 10px 12px; text-align: left; }
  td { padding: 9px 12px; border-bottom: 1px solid #e0e0e0; }
  tr:nth-child(even) { background: #f7f9fc; }
  blockquote { background: #f0f4ff; border-left: 4px solid #1a3c6e; margin: 16px 0; padding: 12px 16px; border-radius: 4px; }
  code { background: #f4f4f4; padding: 2px 6px; border-radius: 3px; font-size: 13px; }
  pre { background: #f4f4f4; padding: 16px; border-radius: 6px; overflow-x: auto; }
  ul, ol { padding-left: 24px; } li { margin: 4px 0; }
  strong { color: #1a3c6e; }
  .back { display: inline-block; margin-bottom: 24px; background: #1a3c6e; color: white; padding: 8px 16px; border-radius: 4px; text-decoration: none; font-size: 14px; }
</style>
"""

converted = []

for folder in OUTPUT_DIRS:
    if not os.path.exists(folder):
        continue
    for fname in sorted(os.listdir(folder)):
        if not fname.endswith(".md"):
            continue
        fpath = os.path.join(folder, fname)
        with open(fpath, encoding="utf-8") as f:
            text = f.read()
        body = markdown.markdown(text, extensions=["tables", "fenced_code", "nl2br"])
        title = fname.replace(".md", "").replace("_", " ").replace("-", " ").title()
        out_path = fpath.replace(".md", ".html")
        index_rel = os.path.relpath(os.path.join(BASE_DIR, "outputs", "index.html"), folder).replace("\\", "/")
        html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  {CSS}
</head>
<body>
  <a href="{index_rel}" class="back">← Trang chủ</a>
  {body}
</body>
</html>"""
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        converted.append((fname, out_path))
        print(f"OK: {os.path.relpath(out_path, BASE_DIR)}")

# Tạo index.html tổng hợp
ICONS = {"research": "🔍", "blog": "✍️"}
sections = {}
for fname, fpath in converted:
    folder_name = os.path.basename(os.path.dirname(fpath))
    sections.setdefault(folder_name, []).append((fname, fpath))

cards_html = ""
for folder_name, items in sections.items():
    icon = ICONS.get(folder_name, "📄")
    label = "Nghiên cứu" if folder_name == "research" else "Bài viết Blog"
    cards_html += f"<h2>{icon} {label}</h2>"
    for fname, fpath in items:
        title = fname.replace(".html", "").replace("_", " ").replace("-", " ").title()
        rel = os.path.relpath(fpath, os.path.join(BASE_DIR, "outputs")).replace("\\", "/")
        cards_html += f"""
    <a href="{rel}" style="text-decoration:none;">
      <div style="background:white;border-radius:8px;padding:16px 20px;margin:10px 0;box-shadow:0 2px 8px rgba(0,0,0,0.08);border-left:4px solid #1a3c6e;">
        <div style="font-weight:600;color:#1a3c6e;">{title}</div>
      </div>
    </a>"""

index_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>Outputs — Cầu trục rót thép</title>
  <style>
    body {{ font-family: 'Segoe UI', sans-serif; max-width: 700px; margin: 50px auto; padding: 0 24px; background: #f5f7fa; }}
    h1 {{ color: #1a3c6e; }} h2 {{ color: #333; margin-top: 32px; font-size: 16px; text-transform: uppercase; letter-spacing: 1px; }}
  </style>
</head>
<body>
  <h1>Marketing Outputs</h1>
  <p style="color:#666;">Cầu trục rót thép — kết quả từ Sub Agents</p>
  {cards_html}
</body>
</html>"""

index_path = os.path.join(BASE_DIR, "outputs", "index.html")
with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html)
print(f"OK: outputs/index.html ({len(converted)} files)")
