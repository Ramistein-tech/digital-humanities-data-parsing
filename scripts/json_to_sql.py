#!/usr/bin/env python3
"""
JSON Metadata Parser & SQLite Exporter for Artifact Records
Author: Rami Izzeddin
"""

import json
import sqlite3
import pandas as pd

def process_dh_json():
    # Sample unformatted JSON dataset of historical artifacts
    raw_json_data = """[
        {"artifact_id": "ART-001", "name": "Corinthian Capital", "period": "Roman", "site": "Qanawat"},
        {"artifact_id": "ART-002", "name": "Basalt Inscription", "period": "Nabataean", "site": "Seeia"},
        {"artifact_id": "ART-003", "name": "Bronze Coin", "period": "Hellenistic", "site": "Damascus"}
    ]"""
    
    records = json.loads(raw_json_data)
    
    # Load into Pandas DataFrame for cleaning and summary
    df = pd.DataFrame(records)
    print("=== Extracted Artifact DataFrame ===")
    print(df[['artifact_id', 'name', 'period', 'site']])
    
    # Export directly to SQLite relational storage
    conn = sqlite3.connect("artifacts_database.db")
    df.to_sql("artifacts", conn, if_exists="replace", index=False)
    conn.close()
    
    print("\n[SUCCESS] Extracted JSON records successfully exported to SQLite table 'artifacts'.")

if __name__ == "__main__":
    process_dh_json()
