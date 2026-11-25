from pathlib import Path

# Automatically detect current folder
folder = Path(__file__).resolve().parent

# Old and new Histats URLs
old_url = b"//sstatic1.histats.com/0.gif?4997348"
new_url = b"//sstatic1.histats.com/0.gif?48"

html_files = [
    p for p in folder.rglob("*")
    if p.is_file() and p.suffix.lower() in (".html", ".htm")
]

print("Working Folder:", folder)
print("HTML Files Found:", len(html_files))

modified = 0
skipped = 0
errors = 0

for file_path in html_files:
    try:
        html = file_path.read_bytes()

        if old_url not in html:
            print("NOT FOUND:", file_path.name)
            skipped += 1
            continue

        updated_html = html.replace(old_url, new_url)

        file_path.write_bytes(updated_html)

        print("SUCCESS:", file_path.name)
        modified += 1

    except Exception as e:
        print("ERROR:", file_path.name, e)
        errors += 1

print("\n========== RESULT ==========")
print("Found   :", len(html_files))
print("Modified:", modified)
print("Skipped :", skipped)
print("Errors  :", errors)
print("============================")

input("\nPress Enter to exit...")