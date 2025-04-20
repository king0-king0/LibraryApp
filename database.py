# database.py
from datetime import datetime
import sqlite3

class databaseManeger():
    def __init__(self):
        self.connect = sqlite3.connect("library.db", check_same_thread=False)
        self.cursor = self.connect.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_name TEXT NOT NULL,
                book_name TEXT NOT NULL,
                book_code TEXT NOT NULL,
                borrow_date TEXT NOT NULL,
                return_book INTEGER
            )
        """)
        self.connect.commit()
    
    def add_book(self, student_name, book_name, book_code):
        try:
            borrow_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.cursor.execute("""
                INSERT INTO books (student_name, book_name, book_code, borrow_date)
                VALUES (?, ?, ?, ?)
            """, (student_name, book_name, book_code, borrow_date))
            self.connect.commit()
        except Exception as e:
            print(f"Error adding book: {e}")
        self.show()

    def show(self):
        # This will show all records from the 'books' table.
        self.cursor.execute("SELECT * FROM books")
        for row in self.cursor.fetchall():
            print(row)