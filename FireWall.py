import socket
import platform
import datetime
import json

allowed_ip = "IP"
if platform.system() == "Windows":
    local_ip = socket.gethostbyname(socket.gethostname())
else:
    local_ip = socket.gethostbyname(socket.gethostname())

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((local_ip, 9999))

server_socket.listen(5)

print(f"Firewall started. Listening for connections on {local_ip}...")

log_file = open("firewall_log.json", "a")

while True:
    client_socket, client_address = server_socket.accept()
    
    client_ip = client_address[0]

    log_entry = {
        "timestamp": str(datetime.datetime.now()),
        "client_ip": client_ip,
        "status": ""
    }

    if client_ip == allowed_ip:
        print("Connection accepted from", client_ip)
        log_entry["status"] = "allowed"
        client_socket.send(b"Connection allowed by firewall.")
    else:
        print("Connection rejected from", client_ip)
        log_entry["status"] = "rejected"
        client_socket.send(b"Connection rejected by firewall.")
        client_socket.close()

    # Write log entry to file
    log_file.write(json.dumps(log_entry) + "\n")
    log_file.flush()  # Ensure writing to file immediately

log_file.close()
