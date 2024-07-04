from database_connection import connect_db, close_db

def add_document(title, document_type, publication_year, classification_id, publisher_name, authors, keywords):
    conn = connect_db()
    cursor = conn.cursor()
    
    try:
        # Start transaction
        conn.autocommit = False
        
        # Find or add Publisher ID
        cursor.execute("SELECT id FROM publishers WHERE name = %s", (publisher_name,))
        publisher = cursor.fetchone()
        if publisher:
            publisher_id = publisher[0]
        else:
            cursor.execute("""
                INSERT INTO publishers (name) 
                VALUES (%s) 
                ON CONFLICT (name) DO NOTHING 
                RETURNING id
            """, (publisher_name,))
            publisher_result = cursor.fetchone()
            if publisher_result:
                publisher_id = publisher_result[0]
            else:
                cursor.execute("SELECT id FROM publishers WHERE name = %s", (publisher_name,))
                publisher_id = cursor.fetchone()[0]
        
        # Add Document
        cursor.execute("""
            INSERT INTO documents (title, document_type, publication_year, classification_id, publisher_id)
            VALUES (%s, %s, %s, %s, %s) RETURNING id
        """, (title, document_type, publication_year, classification_id, publisher_id))
        document_id = cursor.fetchone()[0]
        
        # Add Authors
        if isinstance(authors, str):
            authors = authors.split(",")
        for author in authors:
            author = author.strip()
            cursor.execute("SELECT id FROM authors WHERE name = %s", (author,))
            author_record = cursor.fetchone()
            if author_record:
                author_id = author_record[0]
            else:
                cursor.execute("INSERT INTO authors (name) VALUES (%s) RETURNING id", (author,))
                author_id = cursor.fetchone()[0]
            cursor.execute("INSERT INTO documentauthors (document_id, author_id) VALUES (%s, %s)", (document_id, author_id))
        
        # Add Keywords
        if isinstance(keywords, str):
            keywords = keywords.split(",")
        for keyword in keywords:
            keyword = keyword.strip()
            cursor.execute("SELECT id FROM keywords WHERE keyword = %s", (keyword,))
            keyword_record = cursor.fetchone()
            if keyword_record:
                keyword_id = keyword_record[0]
            else:
                cursor.execute("INSERT INTO keywords (keyword) VALUES (%s) RETURNING id", (keyword,))
                keyword_id = cursor.fetchone()[0]
            cursor.execute("INSERT INTO documentkeywords (document_id, keyword_id) VALUES (%s, %s)", (document_id, keyword_id))
        
        # Add document type specific details
        if document_type == 'Book':
            edition = int(input("Enter the edition of the book: "))
            cursor.execute("INSERT INTO books (document_id, edition) VALUES (%s, %s)", (document_id, edition))
        elif document_type == 'Journal Article':
            journal_title = input("Enter the journal title: ")
            issue_date = input("Enter the issue date (YYYY-MM-DD): ")
            cursor.execute("INSERT INTO journalarticles (document_id, journal_title, issue_date) VALUES (%s, %s, %s)", (document_id, journal_title, issue_date))
        elif document_type == 'Magazine':
            issue_title = input("Enter the issue title: ")
            issue_date = input("Enter the issue date (YYYY-MM-DD): ")
            cursor.execute("INSERT INTO magazines (document_id, issue_title, issue_date) VALUES (%s, %s, %s)", (document_id, issue_title, issue_date))
        
        # Commit transaction
        conn.commit()
        print("Document added successfully!")
    
    except Exception as e:
        # Rollback on error
        conn.rollback()
        print("Failed to add document:", e)
    
    finally:
        cursor.close()
        close_db(conn)

def modify_document(document_id, new_title=None, new_document_type=None, new_publication_year=None, new_classification_id=None):
    conn = connect_db()
    cursor = conn.cursor()
    
    try:
        # Disable autocommit to start a transaction
        conn.autocommit = False
        
        # Fetch existing row from database
        cursor.execute("SELECT * FROM Documents WHERE id = %s", (document_id,))
        document = cursor.fetchone()
        if not document:
            print("Document not found")
            return

        # Use existing values if new values are not provided
        new_title = new_title if new_title is not None else document[1]
        new_document_type = new_document_type if new_document_type is not None else document[2]
        new_publication_year = new_publication_year if new_publication_year is not None else document[4]
        new_classification_id = new_classification_id if new_classification_id is not None else document[5]
        
        # Update row in Documents table
        cursor.execute("""
            UPDATE Documents
            SET title = %s, document_type = %s, publication_year = %s, classification_id = %s
            WHERE id = %s
        """, (new_title, new_document_type, new_publication_year, new_classification_id, document_id))
        
        # Commit transaction
        conn.commit()
        
        print("Document modified successfully!")
    
    except Exception as e:
        # Rollback on error
        conn.rollback()
        print("Failed to modify document:", e)
    
    finally:
        cursor.close()
        close_db(conn)

def delete_document(document_id):
    conn = connect_db()
    cursor = conn.cursor()
    
    try:
        # Disable autocommit to start a transaction
        conn.autocommit = False
        
        # Check if the document exists
        cursor.execute("SELECT COUNT(*) FROM Documents WHERE id = %s", (document_id,))
        document_exists = cursor.fetchone()[0]
        
        if document_exists == 0:
            print("Document ID does not exist.")
            return

        # Delete row from Documents table
        cursor.execute("DELETE FROM Documents WHERE id = %s", (document_id,))
        
        # Commit transaction
        conn.commit()
        
        print("Document and related data deleted successfully!")
    
    except Exception as e:
        # Rollback on error
        conn.rollback()
        print("Failed to delete document:", e)
    
    finally:
        cursor.close()
        close_db(conn) 