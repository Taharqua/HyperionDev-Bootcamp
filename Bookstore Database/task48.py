import sqlite3

db = sqlite3.connect('ebookstore')

cursor = db.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS ebookstore(id INTEGER PRIMARY KEY AUTOINCREMENT, 
    title TEXT, author TEXT, qty INTEGER)
''')

db.commit()

# Adding initial books and using auto increment to fill in the ID numbers

name1 = "A Tale of Two Cities"
author1 = "Charles Dickens"
qty1 = 30

firstbook = [(name1, author1, qty1)]

cursor.executemany(''' INSERT INTO ebookstore(title,author,qty) VALUES(?,?,?)''', firstbook)

db.commit()

cursor.execute(''' UPDATE SQLITE_SEQUENCE SET seq = 2999 WHERE name = 'ebookstore' ''')

cursor.execute(''' DELETE FROM ebookstore WHERE id between 1 AND 5''')

db.commit()

name1 = "A Tale of Two Cities"
author1 = "Charles Dickens"
qty1 = 30

name2 = "Harry Potter and the Philosopher's Stone"
author2 = "J.K. Rowling"
qty2 = 40

name3 = "The Lion, the Witch and the Wardrobe"
author3 = "C.S. Lewis"
qty3 = 25

name4 = "The Lord of the Rings"
author4 = "J.R.R. Tolkien"
qty4 = 37

name5 = "Alice in Wonderland"
author5 = "Lewis Carroll"
qty5 = 12

initialbooks_ = [(name1, author1, qty1), (name2, author2, qty2), (name3, author3, qty3), (name4, author4, qty4),
                 (name5, author5, qty5)]

cursor.executemany(''' INSERT INTO ebookstore(title,author,qty) VALUES(?,?,?)''', initialbooks_)

db.commit()

while True:
    try:
        menu = int(input('''Select one of the following Options below:
                        1 - Add book
                        2 - Update book information
                        3 - Delete books from the database
                        4 - Search the database to find a specific book
                        5 - Exit
                        : '''))
        # adding books - option 1
        if menu == 1:
            pass
            title_new = input("What is the title of the book? ")
            author_new = input("Who is the author")
            qty_new = input("how many books are being added? ")

            books_ = [(title_new, author_new, qty_new)]

            cursor.executemany(''' INSERT INTO ebookstore(title, author, qty) VALUES(?,?,?)''', books_)

            db.commit()

        elif menu == 2:
            pass
            while True:
                try:
                    id_update = input("What is the ID of the book you want to search for? ")
                    update_menu = int(input("Which would you to update? Please select a number for your selection."
                                            "\n1 - Title"
                                            "\n2 - Author"
                                            "\n3 - Quantity"
                                            "\n4 - Exit"))
                    if update_menu == 1:
                        update_title = input("What is the new title of the book? ").capitalize
                        cursor.execute(''' UPDATE student SET title = ? Where id = ?''', (update_title, id_update))
                    elif update_menu == 2:
                        update_author = input("Who is the new author of the book? ").capitalize
                        cursor.execute(''' UPDATE student SET author = ? Where id = ?''', (update_author, id_update))
                    elif update_menu == 3:
                        update_qty = input("What is the new quantity of the book?").lower
                        cursor.execute(''' UPDATE student SET qty = ? Where id = ?''', (update_qty, id_update))
                    elif update_menu == 4:
                        quit()
                    elif update_menu > 4:
                        print("Invalid response! Please enter a number\n")
                        continue
                    elif update_menu < 1:
                        print("Invalid response! Please enter a number\n")
                        continue
                except ValueError as val_error:
                    print("Invalid response! Please enter a number.\n")
                    continue

        # delete books - option 3

        # Using input to find the book

        elif menu == 3:
            pass
            id_delete = int(input("What is the id of the book you would like to delete? "))
            cursor.execute(''' DELETE FROM ebookstore WHERE id = ?''', (id_delete,))

        # Search books - option 4

        # Usinmg input to find the book

        elif menu == 4:
            pass
            title_search = int(input("What is the id of the book? "))
            cursor.execute(''' SELECT id, title, author, qty FROM ebookstore WHERE id = ? ''', (title_search,))
            book = cursor.fetchmany()
            print(book)

        elif menu == 5:
            exit()
        elif menu > 5:
            print("Sorry, you have entered an incorrect value.\n")
    except ValueError as val_error:
        print("Sorry, you have entered an incorrect value.\n")
        continue
