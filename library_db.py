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
    first_name VARCHAR(50) NOT NULL, \
    last_name VARCHAR(50) NOT NULL, \
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
    first_name VARCHAR(50) NOT NULL, \
    last_name VARCHAR(50) NOT NULL, \
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
    VALUES (%s, %s, %s, %s);")
authors_list = [('Thomas', 'Pynchon', 1937, 'USA'),\
                ('Emily', 'Bronte', 1818, 'England'), \
                ('Donna', 'Tartt', 1963, 'USA'),\
                ('David', 'Foster Wallace', 1962, 'USA'), \
                ('Mishima', 'Yukio', 1925, 'Japan'), \
                ('Mark', 'Danielewski', 1966, 'USA'),
                ('David', 'Foster Wallace', 1962, 'USA')]

for author in authors_list:
     mycursor.execute(insert_author, author) 
connection.commit()    

insert_book = ("INSERT INTO books \
    (title, author_id, pagecount, year, genre) \
    VALUES ( %s, %s, %s, %s, %s);")

book_list = [('Gravitys Rainbow', 1, 760, 1973, 'mess'), 
             ('Wuthering Heights', 2, 500, 1847, 'tragedy'),
             ('The secret history', 3, 544, 1992, 'dark academia'), 
             ('Infinite jest', 4, 1079, 1996, 'post-postmodernism'),
             ('Confessions of a Mask', 5, 254, 1949, 'novel'),
             ('House of Leaves', 6, 709, 2000, 'horror'),
             ('The Temple of the Golden Pavilion', 5, 247, 1956, 'novel'),]  

for book in book_list:
     mycursor.execute(insert_book, book) 
connection.commit()      

insert_reader = ("INSERT INTO readers  \
    (first_name, last_name, birth_date, adress) \
    VALUES ( %s, %s, %s, %s);")

reader_list = [('yana', 'lvichek', 1998, 'home'),\
               ('kuzya', 'the cat', 2007, 'under the table'),\
               ('odysseus', 'son of laertes', 1000, 'ithaca'),\
               ('sherlock', 'holmes', 1800, '221b baker st'),\
               ('kaedehara', 'kazuha', 2021, 'inazuma'),\
               ('sugimoto', 'saichi', 1790, 'hokkaido'),\
               ('lordik', 'puding', 1999, 'meadow'),\
               ('dasha', 'detali mashin', 1997, 'aerospace faculty supremacy'),\
               ('polina', 'the main theatre gal', 534, 'saint p'),\
               ('liquorice', 'langley soryu', 333, 'my computer'), \
               ('sofia', 'albedovna', 534, 'dragonspine'),\
               ('scatch', 'marbh', 1666, 'dark autumn woods with spiders'), \
               ('anya', 'whilde oscar', 1854, 'ireland'), \
               ('anya', 'sputnik', 2002, 'on the shore'), \
               ('steshi', 'the catalogue of ships', 1768, 'mysterious mansion')               ]

for reader in reader_list:
    mycursor.execute(insert_reader, reader)

connection.commit()  


mycursor.close()
connection.close()