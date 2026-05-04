#!/usr/bin/python3

import socket

target = input("Enter target IP: ")
start_port = int(input("Start port: "))
end_port = int(input("End port: "))

print(f"\nScanning {target} from port {start_port} to {end_port}\n")

open_ports = []

for port in range(start_port, end_port + 1):
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

print("\nScan Complete")
print("Open Ports:", open_ports)

# Save result
with open("result.txt", "w") as f:
    for p in open_ports:
        f.write(str(p) + "\n")
