from database_connection import connect_db, close_db

def search_documents(query_string):
    conn = connect_db()
    cursor = conn.cursor()

    search_terms = query_string.split()
    like_clauses = []
    params = []

    for term in search_terms:
        pattern = f"%{term}%"
        # Add LIKE clauses for each search term
        like_clauses.append(
            "(d.title ILIKE %s OR a.name ILIKE %s OR c.name ILIKE %s OR k.keyword ILIKE %s OR d.document_type ILIKE %s OR CAST(d.publication_year AS TEXT) ILIKE %s)"
        )
        params.extend([pattern, pattern, pattern, pattern, pattern, pattern])

    query = f"""
    SELECT d.id, d.title, d.document_type, p.name as publisher, d.publication_year, c.name as classification,
           COUNT(*) OVER(PARTITION BY d.id) as match_count
    FROM documents d
    JOIN publishers p ON d.publisher_id = p.id
    JOIN classifications c ON d.classification_id = c.id
    LEFT JOIN documentauthors da ON d.id = da.document_id
    LEFT JOIN authors a ON da.author_id = a.id
    LEFT JOIN documentkeywords dk ON d.id = dk.document_id
    LEFT JOIN keywords k ON dk.keyword_id = k.id
    WHERE {' OR '.join(like_clauses)}
    ORDER BY match_count DESC, d.title
    """

    try:
        cursor.execute(query, params)
        results = cursor.fetchall()
        if results:
            for row in results:
                print(row)
        else:
            print("No results found.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        cursor.close()
        close_db(conn)
