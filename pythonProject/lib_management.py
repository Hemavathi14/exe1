class LibraryManagement:
    def __init__(self,list): #properties of liberary
        self.book_list=list
        self.available_book_list = list[:]
        self.lend_books= {} #key -books value-usernamr
        #self.returnBooks = {}
    def AllBooks(self):
        for books in self.book_list:
            print(books)
    def AvailableBooks(self):
        for books in self.available_book_list:
            print(books)
    def LentBooks(self,name,user_book):
        if user_book  not in self.book_list:
            print(f"This {user_book} is Incorrect . Check the All Book list once again.... ")
        elif user_book in self.available_book_list:
            print(f"Here is your{user_book} book . Enjoy Reading.. ")
            self.available_book_list.remove(user_book)
            self.lend_books.update({user_book:name})
        else:
            print(f"This {user_book} is not Available .The Book is already taken by {self.lend_books[user_book]} ")

    def returnBooks(self,user_book):
        del self.lend_books[user_book]
        self.available_book_list.append(user_book)

if __name__ == "__main__":
    lib=LibraryManagement(["Atomic Habits","The Alchemist","The Secret","Art Of War","Energise Your Mind"])
    print("WELCOME TO THE LIBRARY.\n Enter an option")
    while True:
        print("1.Display Available Books\n2.Display All Books\n3.Borrow a Book\n4.Return a Book\n5.Quit")
        user_choice=int(input("Enter Your Choice:"))
        if user_choice == 1:
            lib.AvailableBooks()
        elif user_choice == 2:
            lib.AllBooks()
        elif user_choice==3:
            name = input("Enter Your Name:")
            user_book = input("Enter The Book Name:").title()
            lib.LentBooks(name,user_book)
        elif user_choice == 4:
            user_book = input("Enter The Book Name:").title()
            lib.returnBooks(user_book)
        else:
            break