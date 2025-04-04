def select_host(hosts):
    print("\nAvailable Hosts:\n")
    for i, h in enumerate(hosts):
        status_icon = "🟢" if h.get("status") == "Running" else "⚫"
        print(f"{i+1}) {status_icon} {h['name']:12} {h['user']}@{h['host']}:{h['port']}  --- {h.get('description', '')}")
    print("0) Cancel\n")

    try:
        choice = int(input("Select a host: "))
        if 1 <= choice <= len(hosts):
            return hosts[choice - 1]
    except ValueError:
        pass
    return None
