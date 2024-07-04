from database_connection import connect_db, close_db
from document_search import search_documents
from borrow_return import borrow_document, return_document
from copy_management import add_copy, delete_copy, list_copies
from member_management import add_member, delete_member, modify_member
from classification_management import add_classification, delete_classification, modify_classification
from document_management import add_document, modify_document, delete_document

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Search Documents")
        print("2. Borrow Document")
        print("3. Return Document")
        print("4. Add Document")
        print("5. Delete Document")
        print("6. Modify Document")
        print("7. Add Copy")
        print("8. Delete Copy")
        print("9. List Copies")
        print("10. Add Member")
        print("11. Delete Member")
        print("12. Modify Member")
        print("13. Add Classification")
        print("14. Delete Classification")
        print("15. Modify Classification")
        print("16. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            query_string = input("Enter search query: ")
            search_documents(query_string)
        elif choice == '2':
            member_id = int(input("Enter your member ID: "))
            document_id = int(input("Enter the document ID: "))
            borrow_document(member_id, document_id)
        elif choice == '3':
            member_id = int(input("Enter your member ID: "))
            document_id = int(input("Enter the document ID: "))
            return_document(member_id, document_id)
        elif choice == '4':
            title = input("Enter title: ")
            document_type = input("Enter document type (Book, Journal Article, Magazine): ")
            publication_year = int(input("Enter publication year: "))
            classification_id = int(input("Enter classification ID: "))
            publisher_name = input("Enter publisher name: ")
            authors = input("Enter authors (comma-separated): ").split(',')
            keywords = input("Enter keywords (comma-separated): ").split(',')
            add_document(title, document_type, publication_year, classification_id, publisher_name, authors, keywords)
        elif choice == '5':
            document_id = int(input("Enter the document ID to delete: "))
            delete_document(document_id)
        elif choice == '6':
            document_id = int(input("Enter the document ID to modify: "))
            title = input("Enter new title (or press Enter to skip): ")
            document_type = input("Enter new document type (Book, Journal Article, Magazine) (or press Enter to skip): ")
            publication_year = input("Enter new publication year (or press Enter to skip): ")
            classification_id = input("Enter new classification ID (or press Enter to skip): ")
            modify_document(document_id, title if title else None, document_type if document_type else None, int(publication_year) if publication_year else None, int(classification_id) if classification_id else None)
        elif choice == '7':
            document_id = int(input("Enter the document ID: "))
            location = input("Enter the location: ")
            add_copy(document_id, location)
        elif choice == '8':
            copy_id = int(input("Enter the copy ID to delete: "))
            delete_copy(copy_id)
        elif choice == '9':
            document_id = int(input("Enter the document ID: "))
            list_copies(document_id)
        elif choice == '10':
            username = input("Enter username: ")
            password = input("Enter password: ")
            email = input("Enter email: ")
            user_type = input("Enter user type (Member or Librarian): ")
            add_member(username, password, email, user_type)
        elif choice == '11':
            user_id = int(input("Enter the user ID to delete: "))
            delete_member(user_id)
        elif choice == '12':
            user_id = int(input("Enter the user ID to modify: "))
            username = input("Enter new username (or press Enter to skip): ")
            password = input("Enter new password (or press Enter to skip): ")
            email = input("Enter new email (or press Enter to skip): ")
            user_type = input("Enter new user type (Member or Librarian) (or press Enter to skip): ")
            modify_member(user_id, username if username else None, password if password else None, email if email else None, user_type if user_type else None)
        elif choice == '13':
            name = input("Enter classification name: ")
            parent_id = input("Enter parent classification ID (or press Enter if none): ")
            parent_id = int(parent_id) if parent_id else None
            add_classification(name, parent_id)
        elif choice == '14':
            classification_id = int(input("Enter the classification ID to delete: "))
            delete_classification(classification_id)
        elif choice == '15':
            classification_id = int(input("Enter the classification ID to modify: "))
            name = input("Enter new classification name (or press Enter to skip): ")
            parent_id = input("Enter new parent classification ID (or press Enter to skip): ")
            parent_id = int(parent_id) if parent_id else None
            modify_classification(classification_id, name if name else None, parent_id)
        elif choice == '16':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
