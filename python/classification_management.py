from database_connection import connect_db, close_db

def add_classification(name, parent_id=None):
    conn = connect_db()
    cursor = conn.cursor()

    if parent_id:
        cursor.execute("INSERT INTO Classifications (name, parent_id) VALUES (%s, %s)", (name, parent_id))
    else:
        cursor.execute("INSERT INTO Classifications (name) VALUES (%s)", (name,))
    
    conn.commit()
    print("Classification added successfully.")
    close_db(conn)

def delete_classification(classification_id):
    conn = connect_db()
    cursor = conn.cursor()

    # Check if the classification_id exists
    cursor.execute("SELECT 1 FROM Classifications WHERE id = %s", (classification_id,))
    if cursor.fetchone() is None:
        print("Classification ID does not exist.")
        close_db(conn)
        return

    # Delete the classification if it exists
    cursor.execute("DELETE FROM Classifications WHERE id = %s", (classification_id,))
    conn.commit()
    print("Classification deleted successfully.")
    close_db(conn)

def modify_classification(classification_id, name=None, parent_id=None):
    conn = connect_db()
    cursor = conn.cursor()

    if name:
        cursor.execute("UPDATE Classifications SET name = %s WHERE id = %s", (name, classification_id))
    if parent_id is not None:
        cursor.execute("UPDATE Classifications SET parent_id = %s WHERE id = %s", (parent_id, classification_id))

    conn.commit()
    print("Classification modified successfully.")
    close_db(conn)