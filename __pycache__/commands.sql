
-- create
CREATE TABLE BOOKS (
  bookId INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  author TEXT NOT NULL
);

-- insert
INSERT INTO BOOKS VALUES (0001, 'The Hobbit', 'J.R.R. Tolkien');
INSERT INTO BOOKS VALUES (0002, 'Dune', 'Frank Herbert');
INSERT INTO BOOKS VALUES (0003, 'Foundation', 'Isaac Asimov');

-- fetch 

-- \d books
SELECT * FROM BOOKS WHERE bookId = 0001;
SELECT * FROM BOOKS WHERE title = 'Dune';
SELECT * FROM BOOKS WHERE author = 'Isaac Asimov' AND bookId != 0001;