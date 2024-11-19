'''
Write a library class witth no_of_books as two instance variables.Write a program to create a libray class and show how you can print all books,add a book and get the number of books using different methods>Show that your progarm doesn't persist the books after the program  is stopped!

'''
class libray:
  def __init__(self):
    self.no_of_books=0
    self.books=[]

  def addBook(self,book):
    self.books.append(book)
    self.no_of_books=len(self.books)

  def showInfo(self):
    print(f"The  libray has {self.no_of_books} books.The books are")
    for book in self.books:
      print(book)

l1=libray()
l1.addBook("harry Potter")
l1.addBook("self care")
l1.showInfo()
