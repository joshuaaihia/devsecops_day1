import os
import time

folder = "."  # current directory

print("🔍 File Auditor Report")
print("=" * 40)

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    if os.path.isfile(filepath):
        size = os.path.getsize(filepath)
    if size > 1_000_000:
        print(f"⚠️ {filename} is larger than 1MB!")
        last_modified = time.ctime(os.path.getmtime(filepath))
        print(f"{filename} | {size} bytes | Last modified: {last_modified}")
