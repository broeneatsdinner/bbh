# theme.py

from prompt_toolkit.styles import Style

APP_STYLE = Style.from_dict({
	"frame": "bg:#1e1e1e fg:#eeeeee",
	"border": "fg:#444444",              # Outer frame border
	"divider": "fg:#444444",             # Divider line under header
	"title": "fg:#aaaaaa bold",          # Title in top border
	"reverse": "bg:#7c3aed fg:#ffffff",  # Highlighted row
	"footer": "fg:#888888 italic",       # Footer help text
})
