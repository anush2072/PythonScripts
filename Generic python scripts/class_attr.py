'''
When logging objects in Python, it is common to see the string representation of the object, which is usually a memory address like 0x14f0456b0. 
However, it is often more useful to log the object's attributes instead of the object itself.
One way to achieve this is 
by using the logging module's string formatting feature to format the log message with the attributes you want to log. 

Here is an example: 
We define a Person class with two attributes name and age. 
We also define a __repr__ method to customize the string representation of the object. 
We create an instance of the Person class and log it using the logging.debug method.
     def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"
you can simplify the __repr__ method by using a loop to iterate over all the attributes
    def __repr__(self):
        attrs = []
        for attr_name, attr_value in self.__dict__.items():
            attrs.append(f"{attr_name}={attr_value}")
        return f"{self.__class__.__name__}({', '.join(attrs)})"
'''
import logging

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        attrs = []
        for attr_name, attr_value in self.__dict__.items():
            attrs.append(f"{attr_name}={attr_value}")
        return f"{self.__class__.__name__}({', '.join(attrs)})"

person = Person("John", 30)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

logging.debug("Person object: %s", person)
logging.debug("Person attributes: name=%s, age=%d", person.name, person.age)
