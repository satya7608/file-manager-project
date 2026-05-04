#!/usr/bin/python3

import difflib
import sys

# Command database

COMMANDS = {
"list files": "ls -l",
"show hidden files": "ls -a",
"current directory": "pwd",
"check disk space": "df -h",
"check memory usage": "free -m",
"show processes": "ps aux",
"kill process": "kill <pid>",
"system uptime": "uptime",
"network info": "ifconfig",
"check internet": "ping google.com",
"create file": "touch filename",
"delete file": "rm filename",
"copy file": "cp source dest",
"move file": "mv source dest",
"search text": "grep 'text' file",
"show file content": "cat filename",
"edit file": "vim filename",
"find file": "find . -name filename",
"download file": "wget url",
"check cpu usage": "top"
}

history = []

def show_menu():
print("\n===== SMART LINUX COMMAND RECOMMENDER =====")
print("1. Get command suggestion")
print("2. Show history")
print("3. Exit")

def recommend_command(user_input):
keys = list(COMMANDS.keys())
match = difflib.get_close_matches(user_input, keys, n=3, cutoff=0.3)

```
if match:
    print("\nBest Matches:\n")
    for m in match:
        print(f"Task: {m}")
        print(f"Command: {COMMANDS[m]}")
        print("-" * 30)
        history.append((m, COMMANDS[m]))
else:
    print("No matching command found!")
```

def show_history():
if not history:
print("\nNo history available.")
return

```
print("\n===== HISTORY =====")
for i, (task, cmd) in enumerate(history, 1):
    print(f"{i}. {task} -> {cmd}")
```

def execute_command(cmd):
choice = input("\nDo you want to execute this command? (y/n): ")
if choice.lower() == 'y':
print("\nExecuting...\n")
import os
os.system(cmd)

def main():
while True:
show_menu()
choice = input("\nEnter choice: ")

```
    if choice == '1':
        user_input = input("\nEnter your task: ").lower()
        keys = list(COMMANDS.keys())
        match = difflib.get_close_matches(user_input, keys, n=1, cutoff=0.4)

        if match:
            task = match[0]
            cmd = COMMANDS[task]
            print(f"\nSuggested Command:\n{cmd}")
            history.append((task, cmd))
            execute_command(cmd)
        else:
            print("No suggestion found!")

    elif choice == '2':
        show_history()

    elif choice == '3':
        print("Exiting...")
        sys.exit()

    else:
        print("Invalid choice!")
```

if **name** == "**main**":
main()

