from database_connection import connect_db, close_db

def add_member(username, password, email, user_type):
    conn = connect_db()
    cursor = conn.cursor()
    
    try:
        # Disable autocommit to start a transaction
        conn.autocommit = False

        # Insert new user into Users table
        cursor.execute("INSERT INTO Users (username, password, email, user_type) VALUES (%s, %s, %s, %s)", 
                       (username, password, email, user_type))
        
        # Commit transaction
        conn.commit()
        
        print("Member added successfully.")
    
    except Exception as e:
        # Rollback on error
        conn.rollback()
        print("Failed to add member:", e)
    
    finally:
        cursor.close()
        close_db(conn)

def modify_member(user_id, username=None, password=None, email=None, user_type=None):
    conn = connect_db()
    cursor = conn.cursor()

    try:
        # Check if the user exists
        cursor.execute("SELECT COUNT(*) FROM Users WHERE id = %s", (user_id,))
        user_exists = cursor.fetchone()[0]

        if user_exists == 0:
            print("User ID does not exist.")
            return

        # Update fields if provided
        if username:
            cursor.execute("UPDATE Users SET username = %s WHERE id = %s", (username, user_id))
        if password:
            cursor.execute("UPDATE Users SET password = %s WHERE id = %s", (password, user_id))
        if email:
            cursor.execute("UPDATE Users SET email = %s WHERE id = %s", (email, user_id))
        if user_type:
            cursor.execute("UPDATE Users SET user_type = %s WHERE id = %s", (user_type, user_id))

        conn.commit()
        print("Member modified successfully.")

    except Exception as e:
        # Rollback on error
        conn.rollback()
        print("Failed to modify member:", e)

    finally:
        cursor.close()
        close_db(conn)

def delete_member(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    
    try:
        # Disable autocommit to start a transaction
        conn.autocommit = False
        
        # Check if the user exists
        cursor.execute("SELECT COUNT(*) FROM Users WHERE id = %s", (user_id,))
        user_exists = cursor.fetchone()[0]
        
        if user_exists == 0:
            print("User ID does not exist.")
            return

        # Delete row from Users table
        cursor.execute("DELETE FROM Users WHERE id = %s", (user_id,))
        
        # Commit transaction
        conn.commit()
        
        print("Member deleted successfully.")
    
    except Exception as e:
        # Rollback on error
        conn.rollback()
        print("Failed to delete member:", e)
    
    finally:
        cursor.close()
        close_db(conn)