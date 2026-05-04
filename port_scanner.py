#!/usr/bin/python3`
# port_scanner.py

import socket
import threading
from queue import Queue

target = input("Enter target IP or hostname: ")
start_port = int(input("Start port: "))
end_port = int(input("End port: "))

queue = Queue()
open_ports = []

def scan_port(port):
try:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(0.5)
result = s.connect_ex((target, port))
if result == 0:
print(f"[OPEN] Port {port}")
open_ports.append(port)
s.close()
except:
pass

def worker():
while not queue.empty():
port = queue.get()
scan_port(port)
queue.task_done()

for port in range(start_port, end_port + 1):
queue.put(port)

threads = []
for _ in range(50):
t = threading.Thread(target=worker)
t.start()
threads.append(t)

queue.join()

print("\nScan Complete")
print("Open Ports:", open_ports)

# Save result

with open("port_results.txt", "w") as f:
for p in open_ports:
f.write(f"{p}\n")

