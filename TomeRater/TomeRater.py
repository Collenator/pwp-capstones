class User(object):
    def __init__(self, name, email):
        #name and email are strings
        #books is an empty dictionary that we will add to later
        self.name = name
        self.email = email
        self.books = {} #dictionary that shows book read: personal rating of book

    def get_email(self):
        """
        returns email address
        """
        print (self.email)

    def change_email(self, address):
        """
        updates users email address, returns updated address
        """
        self.email = address
        print (f"{self.name}'s email address has been updated to: {self.email}")

    def read_book (self, book, rating=None):
        self.books.update({book:rating})

    def get_average_rating(self):
        sum = 0
        count = 0
        for book in self.books:
            if not self.books[book] == None:
                sum += self.books[book]
                count += 1
        self.average_rating = sum / count
        return self.average_rating

        #i dont think we need to return the average rating for the users ratings

    def __repr__(self):
        """
        Gives all of users information in one go
        """

        return f"{self.name}"

    def __eq__(self, other):
        """
        Sees if two users are equal by their name and email address. They are not equal if they dont have the same for both of these fields

        Output: True or False

        """
        if self.name == other.name and self.email == other.email:
            return True
        else:
            return False

class Book:
    ##could have a REPR here!
    def __init__(self, title, isbn):
        #tite is a string, isbn is an integer
        self.title = title
        self.isbn = isbn
        self.avg_rating = 0
        self.ratings = []

    def __hash__(self):
        return hash((self.title, self.isbn))

    def get_title(self):
        """
        prints out title of book
        """
        print (self.title)

    def get_isbn (self):
        """
        prints out isbn of book
        """
        print (self.isbn)

    def set_isbn (self, new_isbn):
        """
        updates new_isbn number
        """
        self.isbn = new_isbn

    def add_rating (self, rating):
        """
        takes in an integer between 1-4 and adds it to the books rating list
        """
        if rating >= 0 and rating <=4:
            self.ratings.append(rating)
        else:
            print ("INVALID RATING. Please enter a rating between 1-4")

    def get_average_rating(self):
        sum = 0
        for _ in range(len(self.ratings)):
            sum += self.ratings[_]
        self.avg_rating = sum / len(self.ratings)
        return self.avg_rating

    def __repr__(self):
        """
        Gives all of users information in one go
        """
        return f"{self.title}"


    def __eq__(self, other):
        """
        Sees if two books are equal by their title and isbn. They are not equal if they dont have the same for both of these fields

        Output: True or False

        """
        if self.title == other.title and self.isbn == other.isbn:
            return True
        else:
            return False

class Fiction(Book):
    def __init__(self, title, isbn, author):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        print(self.author)

    def __repr__ (self):
        return f"{self.title} by {self.author}"

class NonFiction(Book):
    def __init__(self, title, isbn, subject, level):
        super().__init__(title, isbn)
        #subject and string will both return strings
        self.subject = subject
        self.level = level

    def get_subject(self):
        print(self.subject)

    def get_level(self):
        print(self.level)

    def __repr__ (self):
        return f"{self.title} a {self.level} manual on {self.subject}"

class TomeRater:
    def __init__(self):
        self.users = {}#maps a user’s email to the corresponding User object
        self.books = {}#maps a book object to the # of users that have read it

    def create_book(self, title, isbn):
        #set it equal to a variable name so you can call it again
        new_book = Book(title, isbn)
        self.books.update({new_book: 0})
        return new_book

    def create_novel (self, title, isbn, author):
        #set it equal to a variable name so you can call it again
        return Fiction(title, isbn, author)

    def create_non_fiction(self,title, isbn, subject, level):
        #set it equal to a variable name so you can call it again
        return NonFiction(title, isbn, subject, level)

    def print_catalog(self):
        for book in self.books:
            print (book)

    def print_users(self):
        for user in self.users:
            print (user)

    def most_read_book(self):
        most_times_read = 0
        most_read_book = None
        for book, times_read in self.books.items():
            if times_read > most_times_read:
                times_read = most_times_read
                most_read_book = book
        return most_read_book

    def highest_rated_book(self):
        best_rating = 0
        highest_rated_book = None
        for book in self.books:
            if book.get_average_rating() > best_rating:
                book.get_average_rating()
                highest_rated_book = book
        return highest_rated_book

    def most_positive_user(self):
        best_rating = 0
        highest_average_user = None
        for user in self.users.values():
            if user.get_average_rating() > best_rating:
                user.get_average_rating()
                highest_average_user = user
        return highest_average_user

    def add_book_to_user(self, book, email, rating= None):
        if email in self.users:
            self.users[email].read_book(book, rating)
            if rating:
                book.add_rating(rating)
            if book not in self.books:
                self.books.update({book:1})
            else:
                update_count = self.books[book]
                update_count += 1
                self.books[book]= update_count
        else:
            print (f"No user with email: {email}")
        #check to see if book is in Tome_Rater
        if book not in self.books:
            self.books.update({book:1})

    def add_user (self, name, email, user_books = None):
    ###not sure about this function!!
        if email not in self.users:
            new_user = User(name, email)
            self.users.update({email:new_user})
        if user_books:
            for book in user_books:
                self.add_book_to_user(book, email)
        return new_user


if __name__ ==  "__main__":

    Tome_Rater = TomeRater()

    #Create some books:
    book1 = Tome_Rater.create_book("Society of Mind", 12345678)
    novel1 = Tome_Rater.create_novel("Alice In Wonderland", 12345, "Lewis Carroll")
    novel1.set_isbn(9781536831139)
    nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", 1929452, "Python", "beginner")
    nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", 11111938, "AI", "advanced")
    novel2 = Tome_Rater.create_novel("The Diamond Age", 10101010, "Neal Stephenson")
    novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", 10001000, "Ray Bradbury")

    #Create users:
    Tome_Rater.add_user("Alan Turing", "alan@turing.com")
    Tome_Rater.add_user("David Marr", "david@computation.org")
    Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])
    #Add a user with three books already read:

    #Add books to a user one by one, with ratings:
    Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
    Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
    Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
    Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
    Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

    Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
    Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
    Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)


    #Uncomment these to test your functions:
    Tome_Rater.print_catalog()
    Tome_Rater.print_users()

    print("Most positive user:")
    print(Tome_Rater.most_positive_user())
    print("Highest rated book:")
    print(Tome_Rater.highest_rated_book())
    print("Most read book:")
    print(Tome_Rater.most_read_book())
