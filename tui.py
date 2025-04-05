from prompt_toolkit import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import Layout, HSplit, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.styles import Style
from prompt_toolkit.widgets import Box, Frame
from theme import APP_STYLE

class HostSelector:
    def __init__(self, hosts):
        self.hosts = hosts
        self.selected_index = 0
        self.kb = self._create_keybindings()
        self.result = None
        self.cancelled = False

        header_line = (
            f"{'':2}{'NAME':18} {'HOST':18} {'PORT':5}  {'USER':10} {'KEY'}\n"
        )
        footer_line = " ↑/↓ or j/k = navigate   ⏎ = connect   q or Esc = cancel "

        header_text = FormattedTextControl(text=header_line, style="class:header")
        footer_text = FormattedTextControl(text=footer_line, style="class:footer")

        self.control = FormattedTextControl(
            text=self._get_display_text,
            focusable=True,
            key_bindings=self.kb,
        )

        self.window = Window(content=self.control, always_hide_cursor=False)

        self.container = Frame(
            HSplit([
                Window(content=header_text, height=1, dont_extend_height=True),
                Box(self.window, padding=1),
                Window(content=footer_text, height=1, dont_extend_height=True),
            ]),
            title="bbh --- Server Selector",
            style="class:frame",  # ✅ Clean, valid class
        )

        self.layout = Layout(self.container)

        self.app = Application(
            layout=self.layout,
            key_bindings=self.kb,
            style=APP_STYLE,
            full_screen=True,
        )

    def _get_display_text(self):
        lines = []
        for i, h in enumerate(self.hosts):
            is_selected = (i == self.selected_index)
            status_icon = "🟢" if h.get("status") == "Running" else "⚫"
            name = h["name"]
            host = h["host"]
            port = str(h["port"])
            user = h["user"]
            key = h["key"].split("/")[-1]
            line = f"{status_icon}  {name:18} {host:18} {port:5}  {user:10} {key}\n"
            lines.append(("reverse" if is_selected else "", line))
        return lines

    def _create_keybindings(self):
        kb = KeyBindings()

        @kb.add("down")
        @kb.add("j")
        def _(event):
            self.selected_index = (self.selected_index + 1) % len(self.hosts)

        @kb.add("up")
        @kb.add("k")
        def _(event):
            self.selected_index = (self.selected_index - 1) % len(self.hosts)

        @kb.add("enter")
        def _(event):
            self.result = self.hosts[self.selected_index]
            event.app.exit()

        @kb.add("escape")
        @kb.add("q")
        def _(event):
            self.cancelled = True
            event.app.exit()

        return kb

    def run(self):
        self.app.run()
        return None if self.cancelled else self.result


def select_host(hosts, use_simple=False):
    if use_simple:
        return _simple_menu(hosts)
    return HostSelector(hosts).run()


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
