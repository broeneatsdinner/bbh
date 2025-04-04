import subprocess

def launch_ssh(host):
    cmd = [
        "ssh",
        "-i", host["key"],
        "-p", str(host["port"]),
        f"{host['user']}@{host['host']}"
    ]
    print(f"\nConnecting to {host['name']}...\n")
    subprocess.run(cmd)
