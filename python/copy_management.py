from database_connection import connect_db, close_db

def add_copy(document_id, location):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Copies (document_id, location) VALUES (%s, %s)", (document_id, location))
    conn.commit()

    print("Copy added successfully.")
    close_db(conn)

def delete_copy(copy_id):
    conn = connect_db()
    cursor = conn.cursor()
    
    try:
        # Disable autocommit to start a transaction
        conn.autocommit = False
        
        # Check if the copy exists
        cursor.execute("SELECT COUNT(*) FROM Copies WHERE id = %s", (copy_id,))
        copy_exists = cursor.fetchone()[0]
        
        if copy_exists == 0:
            print("Copy ID does not exist.")
            return

        # Delete row from Copies table
        cursor.execute("DELETE FROM Copies WHERE id = %s", (copy_id,))
        
        # Commit transaction
        conn.commit()
        
        print("Copy deleted successfully.")
    
    except Exception as e:
        # Rollback on error
        conn.rollback()
        print("Failed to delete copy:", e)
    
    finally:
        cursor.close()
        close_db(conn)

def list_copies(document_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id, location, is_borrowed FROM Copies WHERE document_id = %s", (document_id,))
    copies = cursor.fetchall()

    for copy in copies:
        status = "Borrowed" if copy[2] else "Available"
        print(f"Copy ID: {copy[0]}, Location: {copy[1]}, Status: {status}")

    close_db(conn)