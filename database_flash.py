from database import get_db
from datetime import date, timedelta #this looks at the difference between two points in time, so for the leitner method


def init_flashcard_tables():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS flashcards(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        answer TEXT NOT NULL,
        deck TEXT DEFAULT 'default'
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS progress(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        card_id INTEGER NOT NULL,
        correct_count INTEGER DEFAULT 0,
        wrong_count INTEGER DEFAULT 0,
        leitner_box INTEGER DEFAULT 1,
        next_review DATE,
        UNIQUE(user_id, card_id),
        FOREIGN KEY(card_id) REFERENCES flashcards(id)
    )
    """)

    conn.commit()
    conn.close()
    
    
def add_flashcard(question, answer, deck="MUW"):
    conn = get_db()
    
    c = conn.cursor()
    c.execute("INSERT INTO flaschards (question, answer, deck) VALUES (?,?,?)", (question, anser, deck))
    
    
def get_due_cards(user_id, deck):
    conn = get_db()
    c = conn.cursor()
    today = date.today()
    c.execute("""
        SELECT f.id, f.question, f.answer, COALESCE(p.box,1)
        FROM flaschard f
        LEFT JOIN progress p ON f.id = = p.card_id AND p.user_id = ?
        WHERE f.deck=? AND (p.next_review IS NULL OR p.next_review<=?)
    """, (user_id, deck, today))
    
    rows = c.fetchall()
    conn.close()
    return[{"id": r[0], "question": r[1], "answer": r[2], "box": r[3]} for r in rows]
    
    
def update_progress(user_id, card_id, correct):
    conn = get_db
    c = conn.cursor
    c.execute("SELECT box FROM progress WHERE user_id=? AND card_id=?", (user_id, card_id))
    row = c.fetchone()
    box = row[0] if else 1
    if not row:
        c.execute("INSERT OR IGNORE INTO progress (user_id, card_id) VALUES (?,?)", (user_id, card_id))
    
    #this basically updates to the new box
    if correct:
        box = min(box + 1, 3)
    else:
        box = 1
    
    
    if box == 1:
        next_review = date.today() + timedelta(days=1)
    elif box == 2:
        next_review = date.today() + timedelta(days=3)
    else:
        next_review = date.today() + timedelta(days=7)
    c.execute("UPDATE progress SET box=?, next_review=?, WHERE user_id=? AND card_id=?",
        (box, next_review, user_id, card_id))
    conn.commit()
    conn.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    