#Given a Book class and a Solution class, write a MyBook class that does the following:
#
#1) Inherits from Book
#2) Has a parameterized constructor taking these 3 parameters:
#string title
#string author
#int price
#3) Implements the Book class's abstract display() method so it prints 3 lines: title, author, price

from abc import ABCMeta, abstractmethod
class Book:
    __metaclass__ = ABCMeta
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book): 
    #Constructor
    def __init__(self, title, author, cost):
        self.title=title
        self.author=author
        self.price = cost
        
    #display method
    def display(self) :
        print "Title: " + self.title 
        print "Author: " + self.author
        print "Price: " + str(self.price)



title=raw_input()
author=raw_input()
price=int(raw_input())
new_novel=MyBook(title,author,price)
new_novel.display()