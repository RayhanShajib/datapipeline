# TaskFlow - Professional Task Manager

A modern, user-friendly task management application with secure user authentication, SQLite database storage, and an elegant dark-themed GUI built with Python and Tkinter.

## 🎯 Features

### User Authentication

- **Secure Registration**: Create accounts with username, password, and optional email
- **Password Hashing**: SHA-256 encryption for secure credential storage
- **User Login**: Quick authentication system
- **Session Management**: Easy sign in/out functionality

### Task Management

- **Create Tasks**: Add new tasks with title, description, priority, status, and due date
- **Edit Tasks**: Modify any task detail after creation
- **Delete Tasks**: Remove tasks with confirmation dialog
- **Task Organization**: Sort by priority (Low, Medium, High, Critical) and status (To Do, In Progress, Done)

### Smart Filtering

- **Filter by Status**: View tasks at specific stages
- **Filter by Priority**: Focus on what matters most
- **Real-time Updates**: Changes reflect immediately

### User Interface

- **Dark Theme**: Modern, eye-friendly design
- **Responsive Layout**: Scrollable task list with mouse-wheel support
- **Color-Coded Badges**: Visual indicators for priority and status
- **Modal Dialogs**: Smooth add/edit workflows
- **Professional Styling**: Consistent fonts, colors, and spacing

### Database

- **SQLite Storage**: Lightweight, file-based database
- **Relational Design**: Proper user-task relationships
- **Data Persistence**: All changes saved automatically
- **Timestamps**: Track when tasks were created and modified

## 📋 Project Structure

```
task_manager/
├── main.py                      # Complete application (809 lines)
├── README.md                    # This file
├── QUICKSTART.md                # Quick start guide
├── taskflow.db                  # SQLite database (auto-created)
└── __pycache__/                 # Python cache files
```

## 🚀 Getting Started

### System Requirements

- **Python**: 3.6 or higher
- **Tkinter**: Usually included with Python
- **SQLite3**: Included with Python standard library
- **OS**: Windows, macOS, or Linux

### Installation

1. **Verify Python Installation**:

   ```bash
   python --version
   # Should show Python 3.6+
   ```

2. **Verify Tkinter Availability**:

   ```bash
   python -c "import tkinter; print('Tkinter is installed')"
   ```

3. **Run the Application**:

   ```bash
   cd task_manager
   python main.py
   ```

   The application will create `taskflow.db` automatically on first run.

### Troubleshooting Installation

**Missing Tkinter?**

- **Ubuntu/Debian**:

  ```bash
  sudo apt-get install python3-tk
  ```

- **macOS**:
  Usually included. If missing, reinstall Python from python.org

- **Windows**:
  Tkinter is included in the Python installer. Reinstall Python and check "tcl/tk and IDLE" during setup

- **Fedora/CentOS**:
  ```bash
  sudo dnf install python3-tkinter
  ```

## 📖 Usage Guide

### First Launch

When you start the application, you'll see the **Sign In** screen.

### Creating an Account (Registration)

1. Click the **"Register"** tab
2. Enter a **Username** (unique)
3. Enter a **Password** (minimum 6 characters)
4. Optionally enter an **Email**
5. Click **"Create Account"**
6. Switch back to **"Sign In"** tab to log in

### Signing In

1. Enter your **Username**
2. Enter your **Password**
3. Click **"Sign In"**

### Task Management

#### Adding a Task

1. Click **"+ New Task"** button
2. Enter the task **Title** (required)
3. Add **Description** (optional)
4. Select **Priority**: Low, Medium, High, or Critical
5. Choose **Status**: To Do, In Progress, or Done
6. Enter **Due Date** in format: `YYYY-MM-DD` (optional)
7. Click **"Save Task"**

#### Editing a Task

1. Click the **"Edit"** button on a task card
2. Modify any fields
3. Click **"Save Task"**

#### Deleting a Task

1. Click the **"Delete"** button on a task card
2. Confirm the deletion in the popup
3. Task is permanently removed

#### Filtering Tasks

Use the dropdown filters at the top:

- **Filter by Status**: Show all, or only specific status
- **Filter by Priority**: Show all, or only specific priority
- Changes apply immediately

### Signing Out

1. Click **"Sign Out"** button (top right)
2. Returns to login screen
3. Your password is cleared for security

## 🎨 Design & Features

### Color Scheme

The application uses a professional dark theme:

| Element    | Color     | Usage                          |
| ---------- | --------- | ------------------------------ |
| Background | `#0f0f1a` | Main window                    |
| Panel      | `#1a1a2e` | Cards and sections             |
| Input      | `#16213e` | Text fields                    |
| Primary    | `#e94560` | Main actions (red-pink)        |
| Secondary  | `#0f3460` | Secondary elements (deep blue) |
| Text Light | `#eaeaea` | Primary text                   |
| Text Dim   | `#888899` | Muted text                     |
| Success    | `#2ecc71` | Positive indicators (green)    |
| Warning    | `#f39c12` | Medium priority (orange)       |
| Danger     | `#e74c3c` | High priority/delete (red)     |

### Priority Levels

| Level    | Color  | Use Case               |
| -------- | ------ | ---------------------- |
| Low      | Green  | Minor tasks, can wait  |
| Medium   | Orange | Standard tasks         |
| High     | Red    | Important tasks        |
| Critical | Pink   | Urgent, time-sensitive |

### Task Statuses

| Status      | Color | Meaning           |
| ----------- | ----- | ----------------- |
| To Do       | Blue  | Not started       |
| In Progress | Cyan  | Currently working |
| Done        | Green | Completed         |

## 💾 Database Schema

### Users Table

```sql
CREATE TABLE users (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    email    TEXT
)
```

**Fields:**

- `id`: Unique user identifier
- `username`: Login name (unique)
- `password`: SHA-256 hashed password
- `email`: Optional contact email

### Tasks Table

```sql
CREATE TABLE tasks (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id     INTEGER NOT NULL,
    title       TEXT NOT NULL,
    description TEXT,
    priority    TEXT DEFAULT 'Medium',
    status      TEXT DEFAULT 'To Do',
    due_date    TEXT,
    created_at  TEXT NOT NULL,
    updated_at  TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
```

**Fields:**

- `id`: Unique task identifier
- `user_id`: Linked user (foreign key)
- `title`: Task name (required)
- `description`: Detailed notes (optional)
- `priority`: Low/Medium/High/Critical
- `status`: To Do/In Progress/Done
- `due_date`: Deadline (YYYY-MM-DD format)
- `created_at`: Timestamp of creation
- `updated_at`: Timestamp of last modification

## 🔐 Security

### Password Storage

- Passwords are hashed using **SHA-256**
- Raw passwords never stored in database
- Hashes are salted (can be enhanced with bcrypt in future versions)

### Data Protection

- User tasks only visible to logged-in owner
- Foreign key constraints enforce data integrity
- No cross-user data access possible

### Best Practices

- Use strong passwords (8+ characters)
- Don't share credentials
- Database file (`taskflow.db`) should be backed up regularly

## 📚 Code Structure

### Main Components

**LoginWindow (Lines 240-380)**

- Registration tab with validation
- Login tab with authentication
- Beautiful dark-themed form
- Feedback messages for user actions

**TaskDialog (Lines 385-485)**

- Modal window for adding/editing tasks
- Form validation
- Date format checking
- Radio buttons for priority
- Dropdown for status

**MainWindow (Lines 490-809)**

- Core application interface
- Task list rendering
- Filter functionality
- CRUD operations
- Session management

**Database Functions (Lines 30-170)**

- Connection management
- User registration and authentication
- Task CRUD operations
- Query building with filters

**Styling Helpers (Lines 195-230)**

- Styled button, entry, label functions
- Consistent theming
- Component customization

## 🎯 Key Functions

### User Management

```python
register_user(username, password, email)    # Create account
authenticate_user(username, password)       # Login
hash_password(raw_password)                 # Secure hashing
```

### Task Operations

```python
add_task(user_id, title, description, priority, status, due_date)
update_task(task_id, title, description, priority, status, due_date)
delete_task(task_id)
fetch_tasks(user_id, status_filter, priority_filter)
```

## 💡 Tips & Tricks

### Productivity

1. **Start Focused**: Mark 3-5 high-priority tasks daily
2. **Use Due Dates**: Set deadlines to stay accountable
3. **Regular Review**: Check your task list weekly
4. **Update Status**: Keep "In Progress" accurate

### Best Practices

- Be specific with task titles
- Add descriptive details in description field
- Use Critical priority sparingly
- Delete completed tasks to reduce clutter
- Filter by priority to focus on important work

## 🐛 Troubleshooting

### Application won't start

**Problem**: ImportError with tkinter
**Solution**: Install tkinter (see Installation > Troubleshooting)

### Database errors

**Problem**: "database is locked" or "no such table"
**Solution**:

1. Close all instances of TaskFlow
2. Delete `taskflow.db`
3. Restart the application
4. Database will be recreated

### Can't log in

**Problem**: "Invalid username or password"
**Solution**:

1. Verify username spelling (case-sensitive)
2. Check password (no spaces before/after)
3. Ensure account was registered
4. Re-register if uncertain

### GUI freezes

**Problem**: Window becomes unresponsive
**Solution**:

1. Force quit the application (Ctrl+C in terminal)
2. Try restarting
3. Check system resources

### Dates not saving

**Problem**: Due date field appears empty
**Solution**:

1. Use exact format: `YYYY-MM-DD`
2. Example: `2024-12-31` not `12/31/2024`

## 🔧 Advanced Usage

### Command Line Options

Currently, the application doesn't support command-line arguments, but you can modify `main.py` to add:

- Direct login with arguments
- Database selection
- Custom theme

### Customization

To modify the application, edit these sections in `main.py`:

**Change Colors**:

```python
BG_DARK = "#0f0f1a"      # Modify color hex codes
ACCENT = "#e94560"
```

**Modify Fonts**:

```python
FONT_TITLE = ("Georgia", 22, "bold")
FONT_BODY = ("Helvetica", 11)
```

**Add Priorities**:

```python
PRIORITIES = ["Low", "Medium", "High", "Critical", "Urgent"]
```

**Add Statuses**:

```python
STATUSES = ["To Do", "In Progress", "Done", "Archived"]
```

## 📈 Scaling Considerations

### Current Capabilities

- Efficient for 100-500 tasks per user
- Fast filtering and searching
- SQLite handles data well for personal use

### For Larger Deployments

Consider these upgrades:

1. **Database**: PostgreSQL or MySQL for multi-user
2. **Backend**: REST API (Flask/Django)
3. **Frontend**: Web interface or mobile app
4. **Sync**: Cloud synchronization
5. **Sharing**: Team collaboration features

## 🔄 Data Management

### Backup Your Tasks

```bash
# Copy the database
cp taskflow.db taskflow_backup.db
```

### Restore from Backup

```bash
cp taskflow_backup.db taskflow.db
```

### Export Tasks

Currently manual, but you can query the database:

```bash
sqlite3 taskflow.db "SELECT * FROM tasks WHERE user_id=1;"
```

## 🚦 Performance Tips

1. **Regular Cleanup**: Delete completed tasks periodically
2. **Archive Old Tasks**: Move past due items to a separate status
3. **Use Filters**: Filter by status to reduce on-screen rendering
4. **Mouse Wheel**: Use mouse wheel for smooth scrolling

## 📝 Logs & Debugging

The application doesn't currently log to file, but you can:

1. **Check Console Output**: Run from terminal to see any errors
2. **Enable Debug**: Modify code to add print statements
3. **Database Inspection**: Use sqlite3 CLI to inspect data

```bash
# Open database in SQLite CLI
sqlite3 taskflow.db

# View users
.schema users
SELECT * FROM users;

# View tasks for user 1
SELECT * FROM tasks WHERE user_id=1;

# Exit
.quit
```

## 🤝 Contributing

This is an educational project. To enhance it:

1. Add test suite (unittest/pytest)
2. Implement search functionality
3. Add task categories/tags
4. Create export to CSV/PDF
5. Add task reminders

## 📜 Version History

### Version 1.0 (Current)

- ✅ User registration and authentication
- ✅ Full task CRUD operations
- ✅ Priority and status filtering
- ✅ Beautiful dark-themed GUI
- ✅ SQLite database integration
- ✅ Modal dialogs for add/edit
- ✅ Mouse wheel scrolling
- ✅ Task timestamps
- ✅ Responsive layout

### Future Versions

- [ ] Search functionality
- [ ] Task categories/tags
- [ ] Recurring tasks
- [ ] Task reminders/notifications
- [ ] Export to PDF/CSV
- [ ] Multiple themes
- [ ] Cloud sync
- [ ] Mobile app

## 📄 License

This project is provided for educational purposes as part of a Python programming course.

## 👨‍💻 Author

Created as a comprehensive Python learning project focusing on:

- Object-oriented programming
- Tkinter GUI development
- SQLite database operations
- User authentication
- Professional code organization

## 🆘 Support

For issues or questions:

1. **Check Troubleshooting section** above
2. **Review code comments** in main.py
3. **Inspect database** with sqlite3 CLI
4. **Test with fresh database**: Delete taskflow.db and restart

## 📞 Contact & Feedback

This is an educational project. Feel free to fork, modify, and improve!

### Learning Resources Used

- Python 3.6+ documentation
- Tkinter comprehensive guide
- SQLite3 Python module docs
- Design patterns and best practices

---

## Quick Reference Card

| Action           | Steps                                               |
| ---------------- | --------------------------------------------------- |
| **Register**     | Click Register tab → Fill form → Create Account     |
| **Login**        | Click Sign In tab → Enter credentials → Sign In     |
| **Add Task**     | + New Task → Fill form → Save Task                  |
| **Edit Task**    | Click Edit on task card → Modify fields → Save Task |
| **Delete Task**  | Click Delete on task card → Confirm                 |
| **Filter Tasks** | Use dropdowns at top → Changes apply instantly      |
| **Sign Out**     | Click Sign Out (top right) → Confirms logout        |
| **Close App**    | Close window → Confirms exit                        |

---

**Version**: 1.0  
**Last Updated**: 2024  
**Status**: Production Ready ✅

**Enjoy TaskFlow!** 🚀📋✅
