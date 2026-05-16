import sqlite3
from datetime import datetime

DB_PATH = "chat_history.db"

def init_db():

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS chats (
        chat_id TEXT PRIMARY KEY,
        chat_name TEXT,
        created_at TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id TEXT,
        role TEXT,
        content TEXT,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()

def create_chat(chat_id, chat_name):

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute(
        "INSERT INTO chats VALUES (?, ?, ?)",
        (chat_id, chat_name, datetime.now().isoformat())
    )

    conn.commit()
    conn.close()

def add_message(chat_id, role, content):

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        INSERT INTO messages (chat_id, role, content, timestamp)
        VALUES (?, ?, ?, ?)
    """, (chat_id, role, content, datetime.now().isoformat()))

    conn.commit()
    conn.close()

def get_chats():

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("SELECT chat_id, chat_name FROM chats")

    chats = c.fetchall()

    conn.close()

    return chats

def get_messages(chat_id):

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        SELECT role, content
        FROM messages
        WHERE chat_id=?
        ORDER BY id ASC
    """, (chat_id,))

    messages = c.fetchall()

    conn.close()

    return [
        {"role": r, "content": m}
        for r, m in messages
    ]

def rename_chat(chat_id, new_name):

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        UPDATE chats
        SET chat_name = ?
        WHERE chat_id = ?
    """, (new_name, chat_id))

    conn.commit()
    conn.close()