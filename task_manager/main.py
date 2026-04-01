
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# Import database functions and constants
from database import (
    init_db, register_user, authenticate_user,
    fetch_tasks, add_task, update_task, delete_task,
    PRIORITIES, STATUSES
)

# Import styling constants and helper widgets
from style import (
    BG_DARK, BG_PANEL, BG_INPUT, ACCENT, ACCENT2,
    TEXT_LIGHT, TEXT_DIM, SUCCESS, DANGER,
    PRIORITY_COLORS, STATUS_COLORS,
    FONT_TITLE, FONT_HEADER, FONT_BODY, FONT_SMALL,
    styled_button, styled_entry, styled_label
)


# ─────────────────────────────────────────────
#  LOGIN / REGISTER WINDOW
# ─────────────────────────────────────────────

class LoginWindow(tk.Tk):
    """
    The application entry point.
    Presents a login form; on success it launches MainWindow.
    """

    def __init__(self):
        super().__init__()
        self.title("To Do – Sign In")
        self.geometry("420x520")
        self.resizable(False, False)
        self.configure(bg=BG_DARK)
        self._center_window(420, 520)
        self._build_ui()

    def _center_window(self, w, h):
        """Move the window to the screen centre."""
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) // 2
        y = (sh - h) // 2
        self.geometry(f"{w}x{h}+{x}+{y}")

    def _build_ui(self):
        # ── Logo / title area ──────────────────────────────────────────
        header = tk.Frame(self, bg=BG_DARK)
        header.pack(fill="x", pady=(40, 10))

        tk.Label(header, text="To Do", font=FONT_TITLE,
                 fg=ACCENT, bg=BG_DARK).pack()
        tk.Label(header, text="Your personal task universe",
                 font=FONT_SMALL, fg=TEXT_DIM, bg=BG_DARK).pack(pady=4)

        # ── Card ───────────────────────────────────────────────────────
        card = tk.Frame(self, bg=BG_PANEL, padx=32, pady=30)
        card.pack(fill="x", padx=32)

        # Tab buttons (Login / Register)
        tab_row = tk.Frame(card, bg=BG_PANEL)
        tab_row.pack(fill="x", pady=(0, 20))

        self._active_tab = tk.StringVar(value="login")

        self.btn_login_tab = tk.Button(
            tab_row, text="Sign In", font=FONT_BODY,
            bg=ACCENT, fg="#000000", relief="flat", bd=0, padx=16, pady=6,
            cursor="hand2", command=lambda: self._switch_tab("login")
        )
        self.btn_login_tab.pack(side="left", fill="x", expand=True)

        self.btn_reg_tab = tk.Button(
            tab_row, text="Register", font=FONT_BODY,
            bg=BG_INPUT, fg=TEXT_DIM, relief="flat", bd=0, padx=16, pady=6,
            cursor="hand2", command=lambda: self._switch_tab("register")
        )
        self.btn_reg_tab.pack(side="left", fill="x", expand=True)

        # ── Form fields ───────────────────────────────────────────────
        self.var_username = tk.StringVar()
        self.var_password = tk.StringVar()

        styled_label(card, "Username").pack(anchor="w")
        styled_entry(card, textvariable=self.var_username,
                     width=36).pack(fill="x", pady=(2, 10))

        styled_label(card, "Password").pack(anchor="w")
        styled_entry(card, textvariable=self.var_password,
                     width=36, show="●").pack(fill="x", pady=(2, 10))

        # Action button
        self.btn_action = styled_button(
            card, "Sign In", self._handle_action, fg="#000", padx=0, pady=10)
        self.btn_action.pack(fill="x", pady=(16, 0))

        # Feedback label
        self.lbl_feedback = tk.Label(card, text="", font=FONT_SMALL,
                                     fg=DANGER, bg=BG_PANEL, wraplength=320)
        self.lbl_feedback.pack(pady=(8, 0))

        self._switch_tab("login")

    def _switch_tab(self, tab: str):
        """Toggle between login and register views."""
        self._active_tab.set(tab)
        if tab == "login":
            self.btn_login_tab.config(bg=ACCENT, fg="#000")
            self.btn_reg_tab.config(bg=BG_INPUT, fg=TEXT_DIM)
            self.btn_action.config(text="Sign In")
        else:
            self.btn_login_tab.config(bg=BG_INPUT, fg=TEXT_DIM)
            self.btn_reg_tab.config(bg=ACCENT, fg="#000")
            self.email_label.pack(anchor="w")
            self.email_entry.pack(fill="x", pady=(2, 10))
            self.btn_action.config(text="Create Account")
        self.lbl_feedback.config(text="")

    def _handle_action(self):
        """Route to login or register based on active tab."""
        if self._active_tab.get() == "login":
            self._do_login()
        else:
            self._do_register()

    def _do_login(self):
        """Validate credentials and open the main window."""
        username = self.var_username.get().strip()
        password = self.var_password.get()

        if not username or not password:
            self.lbl_feedback.config(text="Please fill in all fields.")
            return

        user = authenticate_user(username, password)
        if user is None:
            self.lbl_feedback.config(text="Invalid username or password.")
        else:
            self.withdraw()                        # hide login window
            MainWindow(self, dict(user))           # open main app

    def _do_register(self):
        """Create a new user account."""
        username = self.var_username.get().strip()
        password = self.var_password.get()

        if not username or not password:
            self.lbl_feedback.config(
                text="Username and password are required.")
            return
        if len(password) < 6:
            self.lbl_feedback.config(
                text="Password must be at least 6 characters.")
            return

        success = register_user(username, password)
        if success:
            self.lbl_feedback.config(
                fg=SUCCESS, text="Account created! You can now sign in."
            )
            self._switch_tab("login")
            self.var_username.set(username)
            self.var_password.set("")
        else:
            self.lbl_feedback.config(fg=DANGER, text="Username already taken.")


# ─────────────────────────────────────────────
#  TASK FORM DIALOG (add / edit)
# ─────────────────────────────────────────────

class TaskDialog(tk.Toplevel):
    """
    Modal dialog for creating or editing a task.
    Pass *task* (dict) to pre-populate fields for editing.
    After the dialog closes, check .result for the form data dict,
    or None if the user cancelled.
    """

    def __init__(self, parent, title="New Task", task: dict = None):
        super().__init__(parent)
        self.title(title)
        self.configure(bg=BG_DARK)
        self.resizable(False, False)
        self.grab_set()          # make modal
        self.result = None

        w, h = 480, 540
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        self.geometry(f"{w}x{h}+{(sw-w)//2}+{(sh-h)//2}")

        self._task = task
        self._build_ui()

        if task:
            self._populate(task)

        self.wait_window()       # block until closed

    def _build_ui(self):
        card = tk.Frame(self, bg=BG_PANEL, padx=28, pady=24)
        card.pack(fill="both", expand=True, padx=16, pady=16)

        # ── Title field ───────────────────────────────────────────────
        styled_label(card, "Task Title *").pack(anchor="w")
        self.var_title = tk.StringVar()
        styled_entry(card, textvariable=self.var_title,
                     width=48).pack(fill="x", pady=(2, 12))

        # ── Description ───────────────────────────────────────────────
        styled_label(card, "Description").pack(anchor="w")
        self.txt_desc = tk.Text(
            card, height=5, bg=BG_INPUT, fg=TEXT_LIGHT,
            insertbackground=ACCENT, relief="flat", font=FONT_BODY,
            highlightthickness=1, highlightcolor=ACCENT,
            highlightbackground=TEXT_DIM, wrap="word"
        )
        self.txt_desc.pack(fill="x", pady=(2, 12))

        # ── Priority (radio buttons) ──────────────────────────────────
        styled_label(card, "Priority").pack(anchor="w")
        radio_row = tk.Frame(card, bg=BG_PANEL)
        radio_row.pack(fill="x", pady=(2, 12))
        self.var_priority = tk.StringVar(value="Medium")
        for p in PRIORITIES:
            bg, fg = PRIORITY_COLORS[p]
            tk.Radiobutton(
                radio_row, text=p, variable=self.var_priority, value=p,
                bg=BG_PANEL, fg=fg, selectcolor=bg,
                activebackground=BG_PANEL, activeforeground=fg,
                font=FONT_SMALL, indicatoron=True, cursor="hand2"
            ).pack(side="left", padx=(0, 12))

        # ── Status (dropdown) ─────────────────────────────────────────
        styled_label(card, "Status").pack(anchor="w")
        self.var_status = tk.StringVar(value="To Do")
        status_menu = ttk.Combobox(
            card, textvariable=self.var_status,
            values=STATUSES, state="readonly", font=FONT_BODY, width=20
        )
        status_menu.pack(anchor="w", pady=(2, 12))
        self._style_combobox()

        # ── Due date ─────────────────────────────────────────────────
        styled_label(card, "Due Date (YYYY-MM-DD)").pack(anchor="w")
        self.var_due = tk.StringVar()
        styled_entry(card, textvariable=self.var_due,
                     width=20).pack(anchor="w", pady=(2, 16))

        # ── Buttons ───────────────────────────────────────────────────
        btn_row = tk.Frame(card, bg=BG_PANEL)
        btn_row.pack(fill="x")
        styled_button(btn_row, "Save Task", self._save, padx=20,
                      pady=8).pack(side="right", padx=(8, 0))
        styled_button(btn_row, "Cancel", self.destroy,
                      bg=BG_INPUT, fg=TEXT_DIM, padx=20, pady=8).pack(side="right")

    def _style_combobox(self):
        """Apply dark theme to ttk.Combobox via Style."""
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "TCombobox",
            fieldbackground=BG_INPUT, background=BG_INPUT,
            foreground=TEXT_LIGHT, selectbackground=ACCENT2,
            selectforeground=TEXT_LIGHT, borderwidth=0
        )
        style.map("TCombobox", fieldbackground=[("readonly", BG_INPUT)])

    def _populate(self, task: dict):
        """Pre-fill form with existing task data for editing."""
        self.var_title.set(task.get("title", ""))
        self.txt_desc.insert("1.0", task.get("description", ""))
        self.var_priority.set(task.get("priority", "Medium"))
        self.var_status.set(task.get("status", "To Do"))
        self.var_due.set(task.get("due_date", ""))

    def _save(self):
        """Validate and store result."""
        title = self.var_title.get().strip()
        if not title:
            messagebox.showwarning(
                "Missing field", "Task title is required.", parent=self)
            return

        # Optional date format check
        due = self.var_due.get().strip()
        if due:
            try:
                datetime.strptime(due, "%Y-%m-%d")
            except ValueError:
                messagebox.showwarning("Invalid date",
                                       "Due date must be in YYYY-MM-DD format.", parent=self)
                return

        self.result = {
            "title":       title,
            "description": self.txt_desc.get("1.0", "end-1c").strip(),
            "priority":    self.var_priority.get(),
            "status":      self.var_status.get(),
            "due_date":    due,
        }
        self.destroy()


# ─────────────────────────────────────────────
#  MAIN APPLICATION WINDOW
# ─────────────────────────────────────────────

class MainWindow(tk.Toplevel):
    """
    The core task management interface.
    Displays the logged-in user's tasks, with controls to
    add, edit, delete, and filter them.
    """

    def __init__(self, login_win: LoginWindow, user: dict):
        super().__init__(login_win)
        self._login_win = login_win
        self._user = user         # dict with id, username, email

        self.title(f"To Do – {user['username']}")
        self.configure(bg=BG_DARK)
        self.protocol("WM_DELETE_WINDOW", self._on_close)

        w, h = 960, 650
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        self.geometry(f"{w}x{h}+{(sw-w)//2}+{(sh-h)//2}")

        self._build_ui()
        self._refresh_tasks()

    # ── UI construction ────────────────────────────────────────────────

    def _build_ui(self):
        # ── Top bar ───────────────────────────────────────────────────
        topbar = tk.Frame(self, bg=ACCENT2, padx=20, pady=12)
        topbar.pack(fill="x")

        tk.Label(topbar, text="To Do", font=FONT_HEADER,
                 fg=ACCENT, bg=ACCENT2).pack(side="left")

        tk.Label(topbar, text=f"Signed in as  {self._user['username']}",
                 font=FONT_SMALL, fg=TEXT_DIM, bg=ACCENT2).pack(side="left", padx=20)

        styled_button(topbar, "Sign Out", self._sign_out,
                      bg=DANGER, fg="#000", padx=12, pady=4,
                      font=FONT_SMALL).pack(side="right")

        # ── Toolbar (filters + add button) ────────────────────────────
        toolbar = tk.Frame(self, bg=BG_PANEL, padx=16, pady=10)
        toolbar.pack(fill="x")

        tk.Label(toolbar, text="Filter by Status:",
                 font=FONT_SMALL, fg=TEXT_DIM, bg=BG_PANEL).pack(side="left")
        self.var_filter_status = tk.StringVar(value="All")
        status_dd = ttk.Combobox(
            toolbar, textvariable=self.var_filter_status,
            values=["All"] + STATUSES, state="readonly",
            font=FONT_SMALL, width=12
        )
        status_dd.pack(side="left", padx=(4, 16))
        status_dd.bind("<<ComboboxSelected>>", lambda e: self._refresh_tasks())

        tk.Label(toolbar, text="Priority:",
                 font=FONT_SMALL, fg=TEXT_DIM, bg=BG_PANEL).pack(side="left")
        self.var_filter_priority = tk.StringVar(value="All")
        priority_dd = ttk.Combobox(
            toolbar, textvariable=self.var_filter_priority,
            values=["All"] + PRIORITIES, state="readonly",
            font=FONT_SMALL, width=10
        )
        priority_dd.pack(side="left", padx=(4, 0))
        priority_dd.bind("<<ComboboxSelected>>",
                         lambda e: self._refresh_tasks())

        styled_button(toolbar, "+ New Task", self._open_add_dialog,
                      fg="#000", padx=16, pady=4,
                      font=FONT_SMALL).pack(side="right")

        # ── Task list (canvas + scrollbar) ────────────────────────────
        list_frame = tk.Frame(self, bg=BG_DARK)
        list_frame.pack(fill="both", expand=True, padx=16, pady=12)

        self.canvas = tk.Canvas(list_frame, bg=BG_DARK,
                                highlightthickness=0, bd=0)
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical",
                                  command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg=BG_DARK)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all"))
        )
        self.canvas.create_window(
            (0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Mouse-wheel scrolling
        self.canvas.bind("<MouseWheel>", self._on_mousewheel)
        self.bind("<MouseWheel>", self._on_mousewheel)

        # ── Status bar ────────────────────────────────────────────────
        self.var_statusbar = tk.StringVar(value="Loading…")
        tk.Label(self, textvariable=self.var_statusbar,
                 font=FONT_SMALL, fg=TEXT_DIM,
                 bg=BG_DARK, anchor="w", padx=16).pack(fill="x", pady=(0, 6))

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    # ── Task list refresh ──────────────────────────────────────────────

    def _refresh_tasks(self):
        """Clear and redraw all task cards."""
        # Remove existing widgets
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        tasks = fetch_tasks(
            self._user["id"],
            self.var_filter_status.get(),
            self.var_filter_priority.get()
        )

        if not tasks:
            tk.Label(
                self.scrollable_frame,
                text="No tasks found. Click '+ New Task' to get started!",
                font=FONT_BODY, fg=TEXT_DIM, bg=BG_DARK
            ).pack(pady=40)
        else:
            for task in tasks:
                self._draw_task_card(dict(task))

        count = len(tasks)
        self.var_statusbar.set(
            f"Showing {count} task{'s' if count != 1 else ''}")

    def _draw_task_card(self, task: dict):
        """Render a single task as a styled card widget."""
        p_bg, p_fg = PRIORITY_COLORS[task["priority"]]
        s_bg, s_fg = STATUS_COLORS[task["status"]]

        # Card frame
        card = tk.Frame(
            self.scrollable_frame,
            bg=BG_PANEL, padx=16, pady=12,
            highlightthickness=1,
            highlightbackground=p_bg
        )
        card.pack(fill="x", pady=5, padx=2)

        # ── Header row ─────────────────────────────────────────────
        header_row = tk.Frame(card, bg=BG_PANEL)
        header_row.pack(fill="x")

        # Title
        tk.Label(
            header_row, text=task["title"],
            font=FONT_HEADER, fg=TEXT_LIGHT, bg=BG_PANEL,
            anchor="w"
        ).pack(side="left")

        # Priority badge
        tk.Label(
            header_row, text=f" {task['priority']} ",
            font=FONT_SMALL, fg=p_fg, bg=p_bg,
            padx=6, pady=2, relief="flat"
        ).pack(side="left", padx=8)

        # Status badge
        tk.Label(
            header_row, text=f" {task['status']} ",
            font=FONT_SMALL, fg=s_fg, bg=s_bg,
            padx=6, pady=2, relief="flat"
        ).pack(side="left")

        # ── Description ────────────────────────────────────────────
        desc = task.get("description", "").strip()
        if desc:
            tk.Label(
                card, text=desc[:180] + ("…" if len(desc) > 180 else ""),
                font=FONT_SMALL, fg=TEXT_DIM, bg=BG_PANEL,
                anchor="w", wraplength=680, justify="left"
            ).pack(fill="x", pady=(6, 0))

        # ── Footer row (meta + actions) ───────────────────────────
        footer_row = tk.Frame(card, bg=BG_PANEL)
        footer_row.pack(fill="x", pady=(8, 0))

        # Dates
        due_text = f"Due: {task['due_date']}" if task.get(
            "due_date") else "No due date"
        tk.Label(
            footer_row, text=f"{due_text}   ·   Created: {task['created_at'][:10]}",
            font=FONT_SMALL, fg=TEXT_DIM, bg=BG_PANEL
        ).pack(side="left")

        # Action buttons
        styled_button(
            footer_row, "Delete",
            lambda t=task: self._delete_task(t),
            bg="#3a1e1e", fg=DANGER, padx=10, pady=3, font=FONT_SMALL
        ).pack(side="right")

        styled_button(
            footer_row, "Edit",
            lambda t=task: self._open_edit_dialog(t),
            bg=ACCENT2, fg="#4fc3f7", padx=10, pady=3, font=FONT_SMALL
        ).pack(side="right", padx=(0, 6))

    # ── CRUD actions ──────────────────────────────────────────────────

    def _open_add_dialog(self):
        """Open the task creation dialog."""
        dlg = TaskDialog(self, title="New Task")
        if dlg.result:
            add_task(
                self._user["id"],
                dlg.result["title"],
                dlg.result["description"],
                dlg.result["priority"],
                dlg.result["status"],
                dlg.result["due_date"],
            )
            self._refresh_tasks()

    def _open_edit_dialog(self, task: dict):
        """Open the task editor pre-populated with *task*."""
        dlg = TaskDialog(self, title="Edit Task", task=task)
        if dlg.result:
            update_task(
                task["id"],
                dlg.result["title"],
                dlg.result["description"],
                dlg.result["priority"],
                dlg.result["status"],
                dlg.result["due_date"],
            )
            self._refresh_tasks()

    def _delete_task(self, task: dict):
        """Ask for confirmation then delete the task."""
        confirmed = messagebox.askyesno(
            "Delete Task",
            f"Permanently delete '{task['title']}'?",
            parent=self
        )
        if confirmed:
            delete_task(task["id"])
            self._refresh_tasks()

    # ── Session management ────────────────────────────────────────────

    def _sign_out(self):
        """Close the main window and return to the login screen."""
        self.destroy()
        self._login_win.deiconify()   # show login window again
        # clear password field for security
        self._login_win.var_password.set("")
        self._login_win.var_username.set("")

    def _on_close(self):
        """Handle the window close (X) button."""
        if messagebox.askyesno("Exit", "Exit To Do?", parent=self):
            self._login_win.destroy()   # quit entire app


# ─────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────

if __name__ == "__main__":
    init_db()            # ensure tables exist
    app = LoginWindow()
    app.mainloop()
