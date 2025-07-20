# game_db.py
import sqlite3
from datetime import datetime

# Initialize DB and create table if it doesn't exist
def init_db():
    conn = sqlite3.connect("game_results.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS game_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            game TEXT NOT NULL,
            result TEXT NOT NULL,
            played_on TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Insert a game result into the DB
def save_result(game_name, result):
    conn = sqlite3.connect("game_results.db")
    cursor = conn.cursor()
    played_on = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO game_results (game, result, played_on) VALUES (?, ?, ?)",
                   (game_name, result, played_on))
    conn.commit()
    conn.close()

# Retrieve all game results (optional for leaderboard/history)
def get_results():
    conn = sqlite3.connect("game_results.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM game_results ORDER BY played_on DESC")
    results = cursor.fetchall()
    conn.close()
    return results
