import time
class library:
    global dikt
    dikt ={}
    def __init__(self,name,books):
        self.libraryname = name
        self.books = books
    def print_books(self):
        i = 1
        print("The books available in library are : ")
        for item in self.books:
            print(f"{i}.) {item.upper()}")
            i+= 1
    def add_book(self,name,book_name):
        self.books.append(book_name)
    def rent_book(self,name_of_person,book_name):

        self.books.remove(book_name)
        dikt[book_name]=name_of_person+" borrowed the book on " +time.asctime(time.localtime(time.time()))
    def details(self):
        print(dikt)
    def book_return(self,book):
        self.books.append(book)
        dikt.pop(book)

books = ["and then there were none","silent patient","murder in orient express","da vinci code","kite runner","thousand splendid suns",
           "sapiens","yogi","shoe dog","wings on fire","harry potter","three point zero"]
libb = library("myshelf",books)

print("Welcome to my shelf:\n Enter 1 to see the list of books available \n Enter 2 to donate a book \n Enter 3 to borrow a book \n Enter 4 to return a book \n Enter 5 to see the detail of book borrower\n Enter any other number or key to exit the library")
while 1 :


        opinion = int(input("Please enter one number : "))
        if opinion == 1 :
            libb.print_books()
        elif opinion == 2:
            name = input("Please enter your name here : ")
            bookname = input("Please enter the name of the book you want to donate : ")
            libb.add_book(name,bookname)
            print(f"Thank You {name} for your donation")
        elif opinion == 3 :
            borrower_name = input("Please enter your name :")
            book_borrowed = input("Enter the name of the book you want to borrow : ")
            libb.rent_book(borrower_name,book_borrowed)
        elif opinion == 4  :
            return_book = input("Enter the name of book you want to return : ")
            libb.book_return(return_book)
        elif opinion == 5 :
            libb.details()
        else :
            break
        print("**********************************************************************")
        print("1--list of books available \n2--donate \n3--borrow \n4--return \n5--see the detail of borrower")




