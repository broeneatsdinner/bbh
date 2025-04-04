import csv
import socket

def load_hosts(path):
    try:
        with open(path, newline='') as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        return []

def is_ssh_up(host, port=22, timeout=1.5):
    try:
        with socket.create_connection((host, int(port)), timeout=timeout):
            return True
    except:
        return False

def annotate_hosts_with_status(hosts):
    for h in hosts:
        h["status"] = "Running" if is_ssh_up(h["host"], h.get("port", 22)) else "Offline"
    return hosts
