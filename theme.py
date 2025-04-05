# theme.py

from prompt_toolkit.styles import Style

APP_STYLE = Style.from_dict({
    "frame": "bg:#1e1e1e fg:#eeeeee",
    "border": "fg:#7c3aed",
    "title": "bg:#7c3aed fg:#ffffff bold",
    "header": "bold fg:#ffffff bg:#7c3aed",
    "footer": "fg:#888888 bg:#1e1e1e italic",
    "reverse": "bg:#7c3aed fg:#ffffff",
})
