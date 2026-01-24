import sqlite3
from hashing_pass import hash_password, check_password

def get_db():
    return sqlite3.connect("arabify.db", check_same_thread = False )
    
    

    

def create_db():
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()
    print("Successfully created db and user table")
    
    
    
def create_user(email, username, password):
    conn = get_db()
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            "INSERT INTO users (email, username, password_hash) VALUES (?, ?, ?)",
            (email, username, hash_password(password))
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()
        
        
        
def authenticate_user(email, password):
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT id, email, username, password_hash FROM users WHERE email = ?",
        (email,)
    )
    
    user = cursor.fetchone()
    conn.close()
    
    if user check_password(password, user[3]):
        return {
            "id": user[0],
            "email": user[1],
            "username": user[2]
        }
    return None
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
