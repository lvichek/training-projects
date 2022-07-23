import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password"
)

mycursor = connection.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS library;")
connection.commit()

mycursor.execute("USE library;")
connection.commit()

# create tables

mycursor.execute("CREATE TABLE IF NOT EXISTS authors \
    (author_id INT AUTO_INCREMENT PRIMARY KEY, \
    first_name VARCHAR(50), \
    last_name VARCHAR(50), \
    birth_year INT, \
    birth_country VARCHAR(30) \
    );")

mycursor.execute("CREATE TABLE IF NOT EXISTS books \
    (book_id INT AUTO_INCREMENT PRIMARY KEY, \
    title VARCHAR(50) NOT NULL, \
    author_id INT NOT NULL, \
        FOREIGN KEY (author_id) REFERENCES authors(author_id), \
    pagecount INT, \
    year INT, \
    genre VARCHAR(50) \
    );")

mycursor.execute("CREATE TABLE IF NOT EXISTS readers \
    (reader_id INT AUTO_INCREMENT PRIMARY KEY, \
    first_name VARCHAR(50), \
    last_name VARCHAR(50), \
    birth_date INT, \
    adress VARCHAR(50) \
    );")

mycursor.execute("CREATE TABLE IF NOT EXISTS repository \
    (book_id INT NOT NULL, \
        FOREIGN KEY (book_id) REFERENCES books(book_id), \
    total_copies INT, \
    stock_copies INT, \
    borrowed_copies INT \
    );")    

mycursor.execute("CREATE TABLE IF NOT EXISTS borrowed_books \
    (book_id INT, \
        FOREIGN KEY (book_id) REFERENCES books(book_id), \
    reader_id INT, \
        FOREIGN KEY (reader_id) REFERENCES readers(reader_id), \
    borrow_date INT, \
    return_date INT \
    );")   

#connection.commit()   

# test data insertion

insert_author = ("INSERT INTO authors \
    (first_name, last_name, birth_year, birth_country) \
    VALUES ('Thomas', 'Pynchon', 1937, 'USA');")

mycursor.execute(insert_author) 
connection.commit()    

insert_book = ("INSERT INTO books \
    (title, author_id, pagecount, year, genre) \
    VALUES ( 'Gravitys Rainbow', 1, 760, 1973, 'mess');")

mycursor.execute(insert_book) 
connection.commit()      

insert_reader = ("INSERT INTO readers  \
    (first_name, last_name, birth_date, adress) \
    VALUES ( 'yana', 'lvichek', '1998', 'home');")

mycursor.execute(insert_reader) 
connection.commit()  


mycursor.close()
connection.close()