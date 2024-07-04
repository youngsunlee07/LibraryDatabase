CREATE TABLE Publishers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE Classifications (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    parent_id INT,
    FOREIGN KEY (parent_id) REFERENCES Classifications(id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Authors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    user_type VARCHAR(50) NOT NULL CHECK (user_type IN ('Member', 'Librarian'))
);

CREATE TABLE Documents (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    document_type VARCHAR(50) NOT NULL CHECK (document_type IN ('Book', 'Journal Article', 'Magazine')),
    publisher_id INT,
    publication_year INT,
    classification_id INT,
    FOREIGN KEY (publisher_id) REFERENCES Publishers(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (classification_id) REFERENCES Classifications(id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Copies (
    id SERIAL PRIMARY KEY,
    document_id INT,
    location VARCHAR(255),
    is_borrowed BOOLEAN DEFAULT FALSE,
    borrowed_by INT,
    borrow_date DATE,
    due_date DATE,
    FOREIGN KEY (document_id) REFERENCES Documents(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (borrowed_by) REFERENCES Users(id) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE Books (
    document_id INT PRIMARY KEY,
    edition INT,
    FOREIGN KEY (document_id) REFERENCES Documents(id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE JournalArticles (
    document_id INT PRIMARY KEY,
    journal_title VARCHAR(255),
    issue_date DATE,
    FOREIGN KEY (document_id) REFERENCES Documents(id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Magazines (
    document_id INT PRIMARY KEY,
    issue_title VARCHAR(255),
    issue_date DATE,
    FOREIGN KEY (document_id) REFERENCES Documents(id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Keywords (
    id SERIAL PRIMARY KEY,
    keyword VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE DocumentClassifications (
    document_id INT,
    classification_id INT,
    PRIMARY KEY (document_id, classification_id),
    FOREIGN KEY (document_id) REFERENCES Documents(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (classification_id) REFERENCES Classifications(id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE DocumentAuthors (
    document_id INT,
    author_id INT,
    FOREIGN KEY (document_id) REFERENCES Documents(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (author_id) REFERENCES Authors(id) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (document_id, author_id)
);

CREATE TABLE DocumentKeywords (
    document_id INT,
    keyword_id INT,
    FOREIGN KEY (document_id) REFERENCES Documents(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (keyword_id) REFERENCES Keywords(id) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (document_id, keyword_id)
);

CREATE TABLE Citations (
    citing_document_id INT,
    cited_document_id INT,
    FOREIGN KEY (citing_document_id) REFERENCES Documents(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (cited_document_id) REFERENCES Documents(id) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (citing_document_id, cited_document_id)
);

CREATE TABLE BorrowRecords (
    id SERIAL PRIMARY KEY,
    member_id INT,
    document_id INT,
    borrow_date DATE NOT NULL,
    due_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (member_id) REFERENCES Users(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (document_id) REFERENCES Documents(id) ON DELETE CASCADE ON UPDATE CASCADE
);