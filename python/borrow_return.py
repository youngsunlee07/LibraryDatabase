from datetime import datetime, timedelta
from database_connection import connect_db, close_db

MAX_BORROW_LIMIT = 5  # Maximum number of documents a member can borrow

def borrow_document(member_id, document_id):
    conn = connect_db()
    cursor = conn.cursor()

    try:
        # Start transaction
        conn.autocommit = False

        # Check the number of documents currently borrowed
        cursor.execute("SELECT COUNT(*) FROM Copies WHERE borrowed_by = %s AND is_borrowed = TRUE", (member_id,))
        current_borrowed_count = cursor.fetchone()[0]

        if current_borrowed_count >= MAX_BORROW_LIMIT:
            print("You have reached the maximum borrow limit.")
            close_db(conn)
            return

        # Check if there are available copies to borrow
        cursor.execute("SELECT id FROM Copies WHERE document_id = %s AND is_borrowed = FALSE LIMIT 1", (document_id,))
        copy = cursor.fetchone()

        if not copy:
            print("No available copies for this document.")
        else:
            copy_id = copy[0]
            borrow_date = datetime.now()
            due_date = borrow_date + timedelta(days=14)  # Example: Borrow for 2 weeks
            cursor.execute("""
                UPDATE Copies 
                SET is_borrowed = TRUE, borrowed_by = %s, borrow_date = %s, due_date = %s 
                WHERE id = %s
            """, (member_id, borrow_date, due_date, copy_id))
            
            cursor.execute("""
                INSERT INTO BorrowRecords (member_id, document_id, borrow_date, due_date) 
                VALUES (%s, %s, %s, %s)
            """, (member_id, document_id, borrow_date, due_date))
            
            conn.commit()
            print("Document borrowed successfully.")
    except Exception as e:
        conn.rollback()
        print("Failed to borrow document:", e)
    finally:
        cursor.close()
        close_db(conn)

def return_document(member_id, document_id):
    conn = connect_db()
    cursor = conn.cursor()

    try:
        # Start transaction
        conn.autocommit = False

        # Check if the member has borrowed this document
        cursor.execute("""
            SELECT COUNT(*) 
            FROM Copies 
            WHERE document_id = %s AND borrowed_by = %s
        """, (document_id, member_id))
        borrowed_count = cursor.fetchone()[0]

        if borrowed_count == 0:
            print("The user has not borrowed this document.")
            close_db(conn)
            return

        # Process document return
        cursor.execute("""
            UPDATE Copies 
            SET is_borrowed = FALSE, borrowed_by = NULL, borrow_date = NULL, due_date = NULL 
            WHERE document_id = %s AND borrowed_by = %s
        """, (document_id, member_id))

        cursor.execute("""
            UPDATE BorrowRecords 
            SET return_date = %s 
            WHERE member_id = %s AND document_id = %s AND return_date IS NULL
        """, (datetime.now(), member_id, document_id))

        conn.commit()
        print("Document returned successfully.")
    except Exception as e:
        conn.rollback()
        print("Failed to return document:", e)
    finally:
        cursor.close()
        close_db(conn)
