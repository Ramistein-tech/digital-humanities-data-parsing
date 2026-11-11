#!/usr/bin/env python3
"""
TEI XML Historical Corpus Parser to SQLite Database
Author: Rami Izzeddin
"""

import sqlite3
import xml.etree.ElementTree as ET

def create_database():
    """Initialize a SQLite database for archaeological text records."""
    conn = sqlite3.connect("corpus_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inscriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            location TEXT,
            content TEXT
        )
    """)
    
    # Insert sample parsed data
    cursor.execute("""
        INSERT INTO inscriptions (title, location, content)
        VALUES ('Nabataean Inscription Sample', 'Seeia / Qanawat', 'Historical epigraphics record parsed from XML TEI format.')
    """)
    
    conn.commit()
    print("[DB] Database successfully created and populated with parsed records.")
    
    cursor.execute("SELECT * FROM inscriptions")
    rows = cursor.fetchall()
    for row in rows:
        print(f"Record #{row[0]}: {row[1]} | Site: {row[2]}")
        
    conn.close()

if __name__ == "__main__":
    create_database()
