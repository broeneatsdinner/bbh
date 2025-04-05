import csv
import os
import socket


def load_hosts(filename):
	hosts = []
	if not os.path.exists(filename):
		return hosts

	with open(filename, newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			hosts.append({
				"name": row["name"],
				"host": row["host"],
				"user": row["user"],
				"key": row["key"],
				"port": int(row["port"]),
				"description": row.get("description", "")
			})
	return hosts


def annotate_hosts_with_status(hosts):
	for h in hosts:
		try:
			socket.create_connection((h["host"], int(h["port"])), timeout=1).close()
			h["status"] = "Running"
		except Exception:
			h["status"] = "Offline"
	return hosts
