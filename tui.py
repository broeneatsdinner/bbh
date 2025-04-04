# tui.py
from prompt_toolkit.shortcuts import radiolist_dialog
from prompt_toolkit.styles import Style

def select_host(hosts, use_simple=False):
    if use_simple:
        return _simple_menu(hosts)

    choices = []
    for h in hosts:
        status_icon = "🟢" if h.get("status") == "Running" else "⚫"
        label = f"{status_icon} {h['name']:15} {h['user']}@{h['host']}:{h['port']}"
        choices.append((h, label))

    result = radiolist_dialog(
        title="bbh - Server Selector",
        text="Select a server to SSH into:",
        values=choices,
        style=Style.from_dict({
            "dialog": "bg:#1e1e1e",
            "dialog.body": "bg:#1e1e1e",
            "dialog frame.label": "bg:#5f00af bold",
            "button": "bg:#333333",
            "focused button": "bg:#5f00af",
        }),
    ).run()

    return result


def _simple_menu(hosts):
    print("\nAvailable SSH Hosts:\n")
    for i, h in enumerate(hosts):
        status_icon = "🟢" if h.get("status") == "Running" else "⚫"
        print(f"{i+1}) {status_icon} {h['name']:12} {h['user']}@{h['host']}:{h['port']}")
    print("0) Cancel\n")

    try:
        choice = int(input("Select a host: "))
        if 1 <= choice <= len(hosts):
            return hosts[choice - 1]
    except ValueError:
        pass
    return None
