#!/usr/bin/python3

import os
import shutil
import hashlib
from datetime import datetime

# File categories

FILE_TYPES = {
"Images": [".jpg", ".jpeg", ".png", ".gif"],
"Documents": [".pdf", ".txt", ".docx"],
"Videos": [".mp4", ".mkv", ".avi"],
"Music": [".mp3", ".wav"],
"Archives": [".zip", ".tar", ".gz"]
}

LOG_FILE = "organizer.log"

def log_action(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {message}\n")

def create_folders(base_path):
    for folder in FILE_TYPES.keys():
        path = os.path.join(base_path, folder)
if not os.path.exists(path):
    os.makedirs(path)
log_action(f"Created folder: {folder}")

def get_file_hash(file_path):
    hasher = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            while True:
                chunk = f.read(4096)
                if not chunk:
                    break
                hasher.update(chunk)
        return hasher.hexdigest()
    except:
        return None

def remove_duplicates(base_path):
    print("\nChecking duplicates...")
hashes = {}

```
for file in os.listdir(base_path):
    path = os.path.join(base_path, file)

    if os.path.isdir(path):
        continue

    file_hash = get_file_hash(path)
    if not file_hash:
        continue

    if file_hash in hashes:
        os.remove(path)
        print(f"Removed duplicate: {file}")
        log_action(f"Duplicate removed: {file}")
    else:
        hashes[file_hash] = file
```

def move_files(base_path):
    for file in os.listdir(base_path):
        file_path = os.path.join(base_path, file)

```
    if os.path.isdir(file_path):
        continue

    _, ext = os.path.splitext(file)

    moved = False

    for folder, extensions in FILE_TYPES.items():
        if ext.lower() in extensions:
            dest = os.path.join(base_path, folder, file)
            shutil.move(file_path, dest)
            print(f"Moved: {file} -> {folder}")
            log_action(f"Moved {file} to {folder}")
            moved = True
            break

    if not moved:
        other_folder = os.path.join(base_path, "Others")
        if not os.path.exists(other_folder):
            os.makedirs(other_folder)

        shutil.move(file_path, os.path.join(other_folder, file))
        print(f"Moved: {file} -> Others")
        log_action(f"Moved {file} to Others")
```

def show_summary(base_path):
print("\n===== SUMMARY =====")
for folder in FILE_TYPES.keys():
path = os.path.join(base_path, folder)
if os.path.exists(path):
print(f"{folder}: {len(os.listdir(path))} files")

```
other = os.path.join(base_path, "Others")
if os.path.exists(other):
    print(f"Others: {len(os.listdir(other))} files")
```

def main():
print("=== SMART FILE ORGANIZER ===")

```
path = input("Enter folder path: ")

if not os.path.exists(path):
    print("Invalid path!")
    return

print("\n1. Organize files")
print("2. Remove duplicates")
print("3. Both")

choice = input("Enter choice: ")

create_folders(path)

if choice == "1":
    move_files(path)

elif choice == "2":
    remove_duplicates(path)

elif choice == "3":
    remove_duplicates(path)
    move_files(path)

else:
    print("Invalid choice")
    return

show_summary(path)

print("\nDone! Check organizer.log")
```

if **name** == "**main**":
main()

