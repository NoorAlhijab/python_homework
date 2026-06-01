# Task  1
# Create a New SQLite Database
import sqlite3
try:
    with sqlite3.connect("../db/magazines.db") as conn: 
        print("Database created and connected successfully.")
        # Turns on the foreign key constraint
        conn.execute("PRAGMA foreign_keys = 1") 
        cursor = conn.cursor()

# Task 2
# Define Database Structure
# Create table 
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS publishers (
        publisher_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE       
        )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS magazines (
       magazine_id INTEGER PRIMARY KEY,
       name TEXT NOT NULL UNIQUE,
       publisher_id INTEGER,
       FOREIGN KEY (publisher_id) REFERENCES publishers (publisher_id)        
        )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscribers (
        subscriber_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT NOT NULL
        )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscriptions (
        subscription_id INTEGER PRIMARY KEY,
        expiration_date TEXT NOT NULL,
        subscriber_id INTEGER,
        magazine_id INTEGER,
        FOREIGN KEY (subscriber_id) REFERENCES subscribers (subscriber_id),
        FOREIGN KEY (magazine_id) REFERENCES magazines (magazine_id)        
        )
    """)
    print("Tables created successfully.")

except Exception as e:
    print(f"Error connecting to database:{e}")

# Task 3
# Populate Tables with Data
def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

def add_magazine(cursor, name, publisher_id):
    try:
        cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id))
    except sqlite3.IntegrityError:
        print(f"{name} already exists or invalid publisher_id.")

def add_subscriber(cursor, name, address):
    try:
        cursor.execute("SELECT * FROM subscribers WHERE name = ? AND  address = ?",
         (name, address))
        result = cursor.fetchone()
        if result:
            print(f"{name} and {address} already exists")
            return
        cursor.execute(" INSERT INTO subscribers (name, address) VALUES(?, ?)", (name, address))
    except Exception as e:
        print(f" Error adding {name} and {address}: {e}")

def add_subscription(cursor, expiration_date, subscriber_id, magazine_id):
    try:
        cursor.execute("SELECT * FROM subscriptions WHERE subscriber_id = ? AND  magazine_id = ?", (subscriber_id, magazine_id))
        result = cursor.fetchone()
        if result:
            print("Subscription already exists")
            return
        cursor.execute("INSERT INTO subscriptions (expiration_date, subscriber_id, magazine_id) VALUES(?, ?, ?)", (expiration_date, subscriber_id, magazine_id))
    except Exception as e:
        print(f"Error ocurred: {e}")


add_publisher(cursor, "Hearst Magazines")
add_publisher(cursor, "Condé Nast")
add_publisher(cursor, "Dotdash Meredith")

add_magazine(cursor, "Esquire", 1)
add_magazine(cursor, "Vogue", 2)
add_magazine(cursor, "People", 3)

add_subscriber(cursor, "Alice", "Silver Lake Blvd, LA")
add_subscriber(cursor, "Bob", "Denver, CO")
add_subscriber(cursor, "Charlie", "Desert Horizon Pl, LV")

add_subscription(cursor, "2026-02-12", 1, 1)
add_subscription(cursor, "2026-08-02", 2, 2)
add_subscription(cursor, "2027-06-06", 3, 3)

conn.commit()
print("Data inserted successfully.")

# Task 4
# Write SQL Queries
# Write a query to retrieve all information from the subscribers table.
cursor.execute("SELECT * FROM subscribers")
records = cursor.fetchall()
for record in records:
    print(record)

# Write a query to retrieve all magazines sorted by name.
cursor.execute("SELECT * FROM magazines ORDER BY name")
records = cursor.fetchall()
for record in records:
    print(record)

# Write a query to find magazines for a particular publisher.
cursor.execute( """
    SELECT
    magazines.name          
    FROM magazines 
    JOIN publishers 
    ON magazines.publisher_id = publishers.publisher_id 
    WHERE publishers.name = 'Condé Nast'
""")
records = cursor.fetchall()
for record in records:
    print(record[0])
