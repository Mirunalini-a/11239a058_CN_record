# Sample ARP table
arp_table = {
    "192.168.1.1": "AA:BB:CC:DD:EE:01",
    "192.168.1.2": "AA:BB:CC:DD:EE:02",
    "192.168.1.3": "AA:BB:CC:DD:EE:03"
}

# ARP: IP -> MAC
ip = input("Enter IP address: ")
if ip in arp_table:
    print("MAC Address:", arp_table[ip])
else:
    print("IP not found")

# RARP: MAC -> IP
mac = input("Enter MAC address: ")
found = False
for key, value in arp_table.items():
    if value == mac:
        print("IP Address:", key)
        found = True
        break

if not found:
    print("MAC not found")