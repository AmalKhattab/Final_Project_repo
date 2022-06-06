from book import Book
from borrowing_Order import Borrowing_Order
from client import Client
from librarian import Librarian
from datetime import date


clients = []
librarians = []
books = []
borrowed_orders = []
books.append(Book(1, "Harry Potter and the Philosopher’s Stone", "J.K. Rowling", "You Should Read At Least Once In your Life", True))
books.append(Book(2, "1984", "George Orwell", "You Should Read At Least Once In your Life", False))
books.append(Book(3, "To Kill a Mockingbird", "Harper Lee", "You Should Read At Least Once In your Life", True))

def total_borrowed_books():
    count = 0
    for book in range(len(books)):
        if books[book].get_status() == False:
            count = count + 1
    return count


def total_available_books():
    count = 0
    for book in range(0, len(books)):
        if books[book].get_status() == True:
            count = count + 1
    return count



def total_borrowed_orders():
    return len(borrowed_orders)

# print(total_borrowed_orders())

def check_book_id(book_id):
    exist = False
    for book in range(len(books)):
        if book_id == int(books[book].get_id()):
            exist = True
            break
    return exist

def check_book_status(book_id):
    for book in range(len(books)):
        if book_id == int(books[book].get_id()) and books[book].get_status() == False:
            return books[book]
        else:
            return True



def check_client_id_no(client_id_no):
    exist = False
    for client in range(len(clients)):
        if client_id_no == int(clients[client].get_id_no()):
            exist = True
            break
    return exist


def borrow_book(book_id,client_id_no):
    check_book_id(book_id)
    check_book_status(book_id)
    check_client_id_no(client_id_no)

    if not check_book_id(int(book_id)):
        print("Sorry, The book which you want is not exist")


    elif not check_book_status(int(book_id)):
        print("Sorry, The book which you want is already borrowed")

    elif not check_client_id_no(int(client_id_no)):
        print("Sorry, No user with this id number")

    else:
        print("Borrowing order is completed successfully")


def return_book(book_id):
    check_book_id(book_id)
    check_book_status(book_id)

    if check_book_id(int(book_id)):
        if check_book_status(int(book_id)):
            print("The book is returned successfully")
    else:
        print("Sorry, There is no book with this id")

while True:
    print("-------------------------------------------------------------------------")
    for book in range(len(books)):
        print("name = " + books[book].get_title() + " Status = " + books[book].get_status() + "\n")
    print("========================Welcome to our library ================================")
    choice = int(input("1.Add Client\n2.Add Librarian\n3.Borrow book\n4.Return Book\n5.Exit\nWhat do you want to do? :"))
    if choice == 1:
        print(" To add new client: ")
        clients.append(Client(input("add new id "), input("enter your full name "), input("enter your age "),
                              input("enter your id_number "), input("enter your phone_number ")))
    elif choice == 2:
        print(" To add new librarian")
        librarians.append(Librarian(input("add new id "), input("enter your full name "), input("enter your age "),
                                   input("enter your id_number "), input("enter your employee_type ")))

    elif choice == 3:
        book_id = input("Enter book id, please: ")
        client_id_no = input("Enter client id number, please: ")
        borrow_book(book_id,client_id_no)

    elif choice == 4:
        book_id = input("Enter book id, please: ")
        return_book(book_id)

    elif choice == 5:
        exit()
    else:
        print("Error, Such choice")
