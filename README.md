# Project Name: Library Database Management System

## Overview
Library Management System is a simple console-based application for managing books and members in a library using PostgreSQL and Python. It includes functionalities such as document search, borrowing, returning, copy management, member management, and email notifications for overdue books.

## Main Features
1. Document Search
2. Document Borrowing and Returning
3. Adding, Editing, and Deleting Documents
4. Adding, Deleting and Listing Copies
5. Adding, Editing, and Deleting Members
6. Adding, Editing, and Deleting Classifications
7. Email Notifications for Overdue Books

## Installation
1. Clone this project locally.
```bash
git clone https://github.com/youngsunlee07/LibraryDatabase.git
```

2. Move to the project directory.
``` bash
cd LibraryDatabase
``` 

3. Install the required packages.
```bash
pip install -r requirements.txt
```

## Usage
1. Modify database_connection.py with your database connection information. 

2. Set up email credentials  
- In overdue_management.py, replace the placeholders with your actual email address and password. 

```bash
from_email = "your_email@gmail.com"
from_password = "your_email_password" 
```

3. Run the Scheduler 
- Execute the 'scheduler.py' file to set up email notifications for overdue books.

```bash
python scheduler.py
```

4. Run the Main Program 
- After running 'scheduler.py', execute the 'main.py' file in a separate terminal.

```bash
python main.py 
```

5. Follow the on-screen menu to select and perform the required tasks.

## File Descriptions
- main.py: Provides the user interface and executes the main functionalities.
- scheduler.py: Runs a scheduler that sends email notifications for overdue books at a specified time daily.
- database_connection.py: Contains database connection settings.
- document_search.py: Includes document search functionality.
- borrow_return.py: Handles document borrowing and returning functionalities.
- copy_management.py: Manages adding, deleting, and listing document copies.
- member_management.py: Manages adding, editing, and deleting members.
- classification_management.py: Manages adding, editing, and deleting classifications.
- document_management.py: Manages adding, editing, and deleting documents.
- schema.sql: Contains the database schema, defining tables and relationships.
- ER_diagram.jpg: An image file of the database ER diagram, visually showing the relationships between tables.
- insert_sample.sql: An SQL file with sample data for initializing the database.

## Database Setup
### PostgreSQL Sequence Value Synchronization
To synchronize sequence values in the database, run the following commands. This updates sequence values after inserting sample data to ensure new records have the correct ID values.

```bash 
SELECT setval(pg_get_serial_sequence('publishers', 'id'), COALESCE(MAX(id), 1) + 1, false) FROM publishers;
SELECT setval(pg_get_serial_sequence('documents', 'id'), COALESCE(MAX(id), 1) + 1, false) FROM documents;
SELECT setval(pg_get_serial_sequence('authors', 'id'), COALESCE(MAX(id), 1) + 1, false) FROM authors;
SELECT setval(pg_get_serial_sequence('keywords', 'id'), COALESCE(MAX(id), 1) + 1, false) FROM keywords;
SELECT setval(pg_get_serial_sequence('users', 'id'), COALESCE(MAX(id), 1) + 1, false) FROM users;
SELECT setval(pg_get_serial_sequence('copies', 'id'), COALESCE(MAX(id), 1) + 1, false) FROM copies;
SELECT setval(pg_get_serial_sequence('borrowrecords', 'id'), COALESCE(MAX(id), 1) + 1, false) FROM borrowrecords;
SELECT setval(pg_get_serial_sequence('classifications', 'id'), COALESCE(MAX(id), 1) + 1, false) FROM classifications;
```
These commands are included in the sample_data.sql file and can be executed after inserting sample data.

## Contact
For any inquiries, please contact: youngsun.lee07@gmail.com 
