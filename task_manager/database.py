"""
To Do Database Module
Handles all database operations including connection management,
user authentication, and task CRUD operations.
"""

import sqlite3
import hashlib
from datetime import datetime
from pathlib import Path


# ─────────────────────────────────────────────
#  DATABASE CONFIGURATION
# ─────────────────────────────────────────────

# Use absolute path for database file
DB_FILE = str(Path(__file__).parent / "taskflow.db")

# Priority levels available for tasks
PRIORITIES = ["Low", "Medium", "High", "Critical"]

# Task status options
STATUSES = ["To Do", "In Progress", "Done"]


# ─────────────────────────────────────────────
#  CONNECTION MANAGEMENT
# ─────────────────────────────────────────────

def get_connection():
    """
    Return a new SQLite connection with row_factory set.

    The row_factory makes rows behave like dictionaries,
    allowing access to columns by name.

    Returns:
        sqlite3.Connection: A new database connection
    """
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row   # rows act like dicts
    return conn


# ─────────────────────────────────────────────
#  DATABASE INITIALIZATION
# ─────────────────────────────────────────────

def init_db():
    """
    Create the database tables if they don't already exist.

    Tables created:
        users – stores login credentials
        tasks – stores tasks, linked to a user via user_id

    This function is idempotent and safe to call multiple times.
    """
    conn = get_connection()
    cur = conn.cursor()

    # Users table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT    NOT NULL UNIQUE,
            password TEXT    NOT NULL,
            email    TEXT
        )
    """)

    # Tasks table – each task belongs to one user
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id     INTEGER NOT NULL,
            title       TEXT    NOT NULL,
            description TEXT,
            priority    TEXT    DEFAULT 'Medium',
            status      TEXT    DEFAULT 'To Do',
            due_date    TEXT,
            created_at  TEXT    NOT NULL,
            updated_at  TEXT    NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    conn.commit()
    conn.close()


# ─────────────────────────────────────────────
#  PASSWORD HASHING
# ─────────────────────────────────────────────

def hash_password(raw_password: str) -> str:
    """
    Hash a password using SHA-256.

    Args:
        raw_password (str): The plaintext password to hash

    Returns:
        str: The SHA-256 hex digest of the password
    """
    return hashlib.sha256(raw_password.encode()).hexdigest()


# ─────────────────────────────────────────────
#  USER MANAGEMENT
# ─────────────────────────────────────────────

def register_user(username: str, password: str, email: str = "") -> bool:
    """
    Insert a new user record into the database.

    Args:
        username (str): The desired username (must be unique)
        password (str): The plaintext password (will be hashed)
        email (str, optional): The user's email address. Defaults to "".

    Returns:
        bool: True if registration succeeded, False if username already exists
    """
    try:
        conn = get_connection()
        conn.execute(
            "INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
            (username.strip(), hash_password(password), email.strip())
        )
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False   # duplicate username


def authenticate_user(username: str, password: str):
    """
    Check user credentials and return user information on success.

    Args:
        username (str): The username to authenticate
        password (str): The plaintext password to verify

    Returns:
        sqlite3.Row or None: The user row if credentials match, None otherwise
    """
    conn = get_connection()
    user = conn.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username.strip(), hash_password(password))
    ).fetchone()
    conn.close()
    return user


# ─────────────────────────────────────────────
#  TASK OPERATIONS (CRUD)
# ─────────────────────────────────────────────

def fetch_tasks(user_id: int, status_filter: str = "All", priority_filter: str = "All") -> list:
    """
    Retrieve all tasks for a user with optional filtering.

    Args:
        user_id (int): The user ID to fetch tasks for
        status_filter (str, optional): Filter by status ("To Do", "In Progress", "Done", or "All")
        priority_filter (str, optional): Filter by priority ("Low", "Medium", "High", "Critical", or "All")

    Returns:
        list: A list of task rows (sqlite3.Row objects), sorted by priority then by creation date
    """
    query = "SELECT * FROM tasks WHERE user_id = ?"
    params = [user_id]

    if status_filter != "All":
        query += " AND status = ?"
        params.append(status_filter)

    if priority_filter != "All":
        query += " AND priority = ?"
        params.append(priority_filter)

    query += " ORDER BY CASE priority WHEN 'Critical' THEN 1 WHEN 'High' THEN 2 WHEN 'Medium' THEN 3 ELSE 4 END, created_at DESC"

    conn = get_connection()
    tasks = conn.execute(query, params).fetchall()
    conn.close()
    return tasks


def add_task(user_id: int, title: str, description: str, priority: str, status: str, due_date: str) -> int:
    """
    Create a new task for a user.

    Args:
        user_id (int): The ID of the user who owns this task
        title (str): The task title
        description (str): The task description
        priority (str): The task priority ("Low", "Medium", "High", or "Critical")
        status (str): The task status ("To Do", "In Progress", or "Done")
        due_date (str): The due date in format YYYY-MM-DD

    Returns:
        int: The ID of the newly created task
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = get_connection()
    cur = conn.execute(
        """INSERT INTO tasks (user_id, title, description, priority, status, due_date, created_at, updated_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (user_id, title.strip(), description.strip(),
         priority, status, due_date.strip(), now, now)
    )
    new_id = cur.lastrowid
    conn.commit()
    conn.close()
    return new_id


def update_task(task_id: int, title: str, description: str, priority: str, status: str, due_date: str):
    """
    Update an existing task with new information.

    Args:
        task_id (int): The ID of the task to update
        title (str): The new task title
        description (str): The new task description
        priority (str): The new priority level
        status (str): The new status
        due_date (str): The new due date
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = get_connection()
    conn.execute(
        """UPDATE tasks
           SET title=?, description=?, priority=?, status=?, due_date=?, updated_at=?
           WHERE id=?""",
        (title.strip(), description.strip(), priority,
         status, due_date.strip(), now, task_id)
    )
    conn.commit()
    conn.close()


def delete_task(task_id: int):
    """
    Permanently remove a task from the database.

    Args:
        task_id (int): The ID of the task to delete
    """
    conn = get_connection()
    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
