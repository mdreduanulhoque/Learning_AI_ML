"""
Q2. Create a class Book with the following attributes:
title
author
list of reviews

And add methods to:
add a new review
count reviews
display all reviews
"""
class Book:
    reviews = []
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def add_review(self, review):
        self.reviews.append(review)
        print("Review added.")
        print("Your review:", review)

    def count_reviews(self):
        print("The book has total", len(self.reviews), "reviews")

    def display_all_reviews(self):
        print(self.reviews)

b1 = Book("the f*ck", "me")
b1.add_review("WTF")
b1.add_review("f*ck off")
b1.add_review("get lost, bi*ch")

b1.count_reviews()
b1.display_all_reviews()
