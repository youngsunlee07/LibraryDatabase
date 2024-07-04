INSERT INTO Users (id, username, password, email, user_type) VALUES 
(1, 'user1', 'password1', 'user1@example.com', 'Member'),
(2, 'user2', 'password2', 'user2@example.com', 'Librarian'),
(3, 'user3', 'password3', 'user3@example.com', 'Member'),
(4, 'user4', 'password4', 'user4@example.com', 'Member'),
(5, 'user5', 'password5', 'user5@example.com', 'Librarian'),
(6, 'user6', 'password6', 'user6@example.com', 'Member'),
(7, 'user7', 'password7', 'user7@example.com', 'Member'),
(8, 'user8', 'password8', 'user8@example.com', 'Librarian'),
(9, 'user9', 'password9', 'user9@example.com', 'Member'),
(10, 'user10', 'password10', 'user10@example.com', 'Member');

INSERT INTO publishers (id, name) VALUES 
(1, 'Publisher1'),
(2, 'Publisher2'),
(3, 'Publisher3'),
(4, 'Publisher4'),
(5, 'Publisher5'),
(6, 'Publisher6'),
(7, 'Publisher7'),
(8, 'Publisher8'),
(9, 'Publisher9'),
(10, 'Publisher10');

INSERT INTO classifications (id, name, parent_id) VALUES 
(1, 'Fiction', NULL),
(2, 'Non-Fiction', NULL),
(3, 'Science Fiction', 1),
(4, 'Fantasy', 1),
(5, 'Biography', 2),
(6, 'History', 2),
(7, 'Technology', 2),
(8, 'Children', 1),
(9, 'Adventure', 1),
(10, 'Mystery', 1);

INSERT INTO authors (id, name) VALUES 
(1, 'Author1'),
(2, 'Author2'),
(3, 'Author3'),
(4, 'Author4'),
(5, 'Author5'),
(6, 'Author6'),
(7, 'Author7'),
(8, 'Author8'),
(9, 'Author9'),
(10, 'Author10');

INSERT INTO documents (id, title, document_type, publisher_id, publication_year, classification_id) VALUES 
(1, 'Document1', 'Book', 1, 2020, 1),
(2, 'Document2', 'Journal Article', 2, 2021, 2),
(3, 'Document3', 'Magazine', 3, 2019, 3),
(4, 'Document4', 'Book', 4, 2022, 4),
(5, 'Document5', 'Journal Article', 5, 2018, 5),
(6, 'Document6', 'Magazine', 6, 2017, 6),
(7, 'Document7', 'Book', 7, 2023, 7),
(8, 'Document8', 'Journal Article', 8, 2020, 8),
(9, 'Document9', 'Magazine', 9, 2021, 9),
(10, 'Document10', 'Book', 10, 2019, 10);

INSERT INTO copies (document_id, location, is_borrowed, borrowed_by, borrow_date, due_date) VALUES 
(1, 'Location1', FALSE, NULL, NULL, NULL),
(2, 'Location2', FALSE, NULL, NULL, NULL),
(3, 'Location3', TRUE, 1, '2023-01-01', '2023-01-15'),
(4, 'Location4', TRUE, 2, '2023-02-01', '2023-02-15'),
(5, 'Location5', FALSE, NULL, NULL, NULL),
(6, 'Location6', TRUE, 3, '2023-03-01', '2023-03-15'),
(7, 'Location7', FALSE, NULL, NULL, NULL),
(8, 'Location8', TRUE, 4, '2023-04-01', '2023-04-15'),
(9, 'Location9', FALSE, NULL, NULL, NULL),
(10, 'Location10', TRUE, 5, '2023-05-01', '2023-05-15');

INSERT INTO books (document_id, edition) VALUES 
(1, 1),
(4, 2),
(7, 1),
(10, 3);

INSERT INTO journalarticles (document_id, journal_title, issue_date) VALUES 
(2, 'Journal1', '2021-01-01'),
(5, 'Journal2', '2018-02-01'),
(8, 'Journal3', '2020-03-01');

INSERT INTO magazines (document_id, issue_title, issue_date) VALUES 
(3, 'Magazine1', '2019-01-01'),
(6, 'Magazine2', '2017-02-01'),
(9, 'Magazine3', '2021-03-01');

INSERT INTO documentauthors (document_id, author_id) VALUES 
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);

INSERT INTO documentclassifications (document_id, publisher_id) VALUES 
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);

INSERT INTO keywords (id, keyword) VALUES 
(1, 'Keyword1'),
(2, 'Keyword2'),
(3, 'Keyword3'),
(4, 'Keyword4'),
(5, 'Keyword5'),
(6, 'Keyword6'),
(7, 'Keyword7'),
(8, 'Keyword8'),
(9, 'Keyword9'),
(10, 'Keyword10');

INSERT INTO documentkeywords (document_id, keyword_id) VALUES 
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);

INSERT INTO citations (citing_document_id, cited_document_id) VALUES 
(1, 2),
(2, 3),
(3, 4),
(4, 5),
(5, 6),
(6, 7),
(7, 8),
(8, 9),
(9, 10),
(10, 1);

INSERT INTO borrowrecords (id, member_id, document_id, borrow_date, due_date, return_date) VALUES 
(1, 1, 3, '2023-01-01', '2023-01-15', NULL),
(2, 2, 4, '2023-02-01', '2023-02-15', NULL),
(3, 3, 6, '2023-03-01', '2023-03-15', NULL),
(4, 4, 8, '2023-04-01', '2023-04-15', NULL),
(5, 5, 10, '2023-05-01', '2023-05-15', NULL),
(6, 1, 7, '2023-06-01', '2023-06-15', NULL),
(7, 2, 9, '2023-07-01', '2023-07-15', NULL),
(8, 3, 2, '2023-08-01', '2023-08-15', NULL),
(9, 4, 5, '2023-09-01', '2023-09-15', NULL),
(10, 5, 1, '2023-10-01', '2023-10-15', NULL);

-- Sequence Value Synchronization
SELECT setval(pg_get_serial_sequence('publishers', 'id'), COALESCE(MAX(id), 1) + 1, false) FROM publishers;
SELECT setval(pg_get_serial_sequence('documents', 'id'), COALESCE(MAX(id), 1) + 1, false) FROM documents;
SELECT setval(pg_get_serial_sequence('authors', 'id'), COALESCE(MAX(id), 1) + 1, false) FROM authors;
SELECT setval(pg_get_serial_sequence('keywords', 'id'), COALESCE(MAX(id), 1) + 1, false) FROM keywords;
SELECT setval(pg_get_serial_sequence('users', 'id'), COALESCE(MAX(id), 1) + 1, false) FROM users;
SELECT setval(pg_get_serial_sequence('copies', 'id'), COALESCE(MAX(id), 1) + 1, false) FROM copies;
SELECT setval(pg_get_serial_sequence('borrowrecords', 'id'), COALESCE(MAX(id), 1) + 1, false) FROM borrowrecords; 
SELECT setval(pg_get_serial_sequence('classifications', 'id'), COALESCE(MAX(id), 1) + 1, false) FROM classifications;
