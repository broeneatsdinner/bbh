from utils import load_hosts, annotate_hosts_with_status
from tui import select_host
from launcher import launch_ssh

def main():
    hosts = load_hosts("hosts.csv")
    if not hosts:
        print("No hosts found. You can copy hosts_config.csv to hosts.csv and edit it.")
        return

    hosts = annotate_hosts_with_status(hosts)
    selected = select_host(hosts)
    if selected:
        launch_ssh(selected)
    else:
        print("No host selected.")

if __name__ == "__main__":
    main()
