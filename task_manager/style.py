"""
To Do Styling Module
Contains all UI styling constants, colors, fonts, and helper widgets
for the To Do task management application.
"""

import tkinter as tk


# ─────────────────────────────────────────────
#  COLOR PALETTE
# ─────────────────────────────────────────────

# Dark-mode palette
BG_DARK = "#0f0f1a"       # main background
BG_PANEL = "#1a1a2e"      # card / panel
BG_INPUT = "#16213e"      # input fields
ACCENT = "#e94560"        # primary accent (red-pink)
ACCENT2 = "#0f3460"       # secondary accent (deep blue)
TEXT_LIGHT = "#eaeaea"    # primary text
TEXT_DIM = "#888899"      # muted text
SUCCESS = "#2ecc71"       # green
WARNING = "#f39c12"       # orange
DANGER = "#e74c3c"        # red


# ─────────────────────────────────────────────
#  BADGE COLORS (By Priority & Status)
# ─────────────────────────────────────────────

# Priority badge colours: {priority: (background, foreground)}
PRIORITY_COLORS = {
    "Low":      ("#1e3a2f", SUCCESS),
    "Medium":   ("#3a2e1e", WARNING),
    "High":     ("#3a1e1e", DANGER),
    "Critical": (ACCENT,    "#ffffff"),
}

# Status badge colours: {status: (background, foreground)}
STATUS_COLORS = {
    "To Do":       ("#2a2a3e", TEXT_DIM),
    "In Progress": (ACCENT2,  "#4fc3f7"),
    "Done":        ("#1e3a2f", SUCCESS),
}


# ─────────────────────────────────────────────
#  FONT DEFINITIONS
# ─────────────────────────────────────────────

FONT_TITLE = ("Georgia", 22, "bold")      # Large titles
FONT_HEADER = ("Georgia", 14, "bold")     # Section headers
FONT_BODY = ("Helvetica", 11)             # Regular text
FONT_SMALL = ("Helvetica", 9)             # Small text
FONT_MONO = ("Courier", 10)               # Monospace (code)


# ─────────────────────────────────────────────
#  HELPER WIDGETS
# ─────────────────────────────────────────────

def styled_button(parent, text, command, bg=ACCENT, fg="#ffffff",
                  padx=18, pady=8, font=FONT_BODY):
    """
    Create a flat, styled button with consistent appearance.

    Args:
        parent: Parent widget
        text (str): Button label text
        command: Callback function when clicked
        bg (str): Background color (default: ACCENT red)
        fg (str): Foreground/text color (default: white)
        padx (int): Horizontal padding
        pady (int): Vertical padding
        font: Font tuple (default: FONT_BODY)

    Returns:
        tk.Button: A styled button widget
    """
    btn = tk.Button(
        parent, text=text, command=command,
        bg=bg, fg=fg, activebackground=DANGER, activeforeground="#ffffff",
        relief="flat", cursor="hand2", font=font,
        padx=padx, pady=pady, bd=0
    )
    return btn


def styled_entry(parent, textvariable=None, width=30, show=None):
    """
    Create a styled text entry field.

    Args:
        parent: Parent widget
        textvariable: Tk StringVar for binding (optional)
        width (int): Field width in characters
        show (str): Character to show instead of input (e.g., "*" for passwords)

    Returns:
        tk.Entry: A styled entry widget
    """
    kw = dict(
        bg=BG_INPUT, fg=TEXT_LIGHT, insertbackground=ACCENT,
        relief="flat", font=FONT_BODY, width=width,
        highlightthickness=1, highlightcolor=ACCENT,
        highlightbackground=TEXT_DIM
    )
    if textvariable:
        kw["textvariable"] = textvariable
    if show:
        kw["show"] = show
    return tk.Entry(parent, **kw)


def styled_label(parent, text, font=FONT_BODY, fg=TEXT_LIGHT, bg=BG_PANEL):
    """
    Create a styled label widget.

    Args:
        parent: Parent widget
        text (str): Label text
        font: Font tuple (default: FONT_BODY)
        fg (str): Foreground/text color (default: TEXT_LIGHT)
        bg (str): Background color (default: BG_PANEL)

    Returns:
        tk.Label: A styled label widget
    """
    return tk.Label(parent, text=text, font=font, fg=fg, bg=bg)


# ─────────────────────────────────────────────
#  STYLE UTILITIES
# ─────────────────────────────────────────────

def get_priority_colors(priority: str) -> tuple:
    """
    Get background and foreground colors for a priority level.

    Args:
        priority (str): Priority level ("Low", "Medium", "High", "Critical")

    Returns:
        tuple: (background_color, foreground_color)
    """
    return PRIORITY_COLORS.get(priority, ("#2a2a3e", TEXT_DIM))


def get_status_colors(status: str) -> tuple:
    """
    Get background and foreground colors for a status.

    Args:
        status (str): Status ("To Do", "In Progress", "Done")

    Returns:
        tuple: (background_color, foreground_color)
    """
    return STATUS_COLORS.get(status, ("#2a2a3e", TEXT_DIM))
