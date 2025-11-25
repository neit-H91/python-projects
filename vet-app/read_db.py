import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Get all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

for table_name in tables:
    table = table_name[0]
    print(f"\nTable: {table}")
    # Print schema
    cursor.execute(f"PRAGMA table_info({table});")
    schema = cursor.fetchall()
    print("Schema:")
    for col in schema:
        print(f"  {col[1]} ({col[2]})")
    # Print data
    print(f"SELECT * FROM {table};")
    # cursor.execute(f"SELECT * FROM {table};")
    # rows = cursor.fetchall()
    # if rows:
    #     print("Data:")
    #     for row in rows:
    #         print(f"  {row}")
    # else:
    #     print("  No data.")

