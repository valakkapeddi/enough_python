__author__ = 'paladin'

## Defining a class
class MyClass:
    # Methods, or functions that are part of a class, are required to have 'self' as the first parameter.
    # Unlike a lot of other languages, python methods can't automatically see the other members of that class.
    # Passing 'self' is how you make the current object available to the scope of the method.

    # For example, if I have a method called 'a_method' that I want to be able to call from other methods in the class,
    # I can only do it by passing in 'self'.
    def a_method(self):
        print 'MyClass.a_method called'

    def another_method(self):
        print 'MyClass.another_method called - calling a_method.'
        self.a_method()

    # Methods prefixed by a single underscore _ are considered 'private' methods in Python.
    # Mostly, this is just convention - nothing prevents you from calling an object's private method from another class.
    def _a_private_method(self):
        print 'MyClass.a_private_method called'

    # However, 'private' class members aren't visible to code outside the script where the class is defined.
    # So if you were to import this class into an another script, '_a_private_method' wouldn't be visible directly,
    # and you would only be able to run this code if another, non-private method of the class called it.
    def calls_private_method(self):
        print 'MyClass.calls_private_method called - calling a_private_method'
        self._a_private_method()

    # Methods prefixed by __double_underscores (but not suffixed) are also treated specially. Python 'mangles' the names
    # of these methods by prefixing the name of the class, so '_a_mangled_method' becomes _MyClass__a_mangled_method.
    def __a_mangled_method(self):
        print 'MyClass._MyClass__a_mangled_method called.'


## Using classes

# You create an object of a class in Python by 'calling' the class.
my_object = MyClass()

# You can then call instance methods of this object.
my_object.a_method()
my_object.another_method()

# Note that Python's 'private' methods are just a convention - nothing exists to prevent you from calling the private
# methods of an object from anywhere in the same script where the object was defined.
my_object._a_private_method()
my_object._MyClass__a_mangled_method()


## 'Magic' methods.
# Methods prefixed *and* suffixed by __double_underscores__ are 'magic' methods that we do not call directly - they
# automatically get called by Python in certain situations. Some examples include __init__ and __str__.
class RpgMonster:

    # The __init__ method is automatically called when you create an object in Python. You can add parameters to the
    # __init__ method, which will allow you to create objects initialized with particular values.
    # Note, however, that if you create an init method for your class, you're required to pass values in when you create
    # the object.
    def __init__(self, name, hit_points, treasure):
        self._name = name
        self._hitPoints = hit_points
        self._treasure = treasure

    # The __str__ method is called automatically when you try to convert an object into a string - for example, if you
    # try to print the object. Write a __str__ method for your object when you want it to produce human-readable output
    # intead of gobbledeygook that just tells you the object's type and reference.
    # Comment out the __str__ method to see what that looks like!
    def __str__(self):
        return 'This is a %s monster with %d hitpoints, carrying %s' % (self._name, self._hitPoints, self._treasure)

#monster = RpgMonster() # - will not work, because you need to pass in three arguments.
monster = RpgMonster('mysterious shadow', 2, 'copper sword') # calls the __init__ method.
print monster # calls __str__.




