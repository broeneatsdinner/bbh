import subprocess


def launch_ssh(host):
	host_str = f"{host['user']}@{host['host']}"
	cmd = ["ssh", "-i", host["key"], "-p", str(host["port"]), host_str]
	print(f"Connecting to: {host_str}")
	subprocess.run(cmd)
