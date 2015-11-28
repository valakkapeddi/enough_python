# A decorator is a function for 'making' functions out of other functions.
# To write a decorator, create a function that takes a function as an argument
# Create a function inside your decorator that calls the function you passed in, doing whatever extra
# work you need it to do, and then return the inner function.
# This is similar to Javascript
def add_logging(func):
    def inner():
        print 'calling ' + func.__name__
        func()
        print 'done calling.'
    return inner

def a_function():
    print 'i am a function.'

decorated = add_logging(a_function)
decorated()

# The @ operator is Python's cool shorthand for applying a decorator to a function.
# The effect is the same as if you'd called the decorator, supplying your function as an arg;
# for instance: add_logging(a_decorated_function)
@add_logging
def a_decorated_function():
    print 'i am a decorated function.'

a_decorated_function()

# You can decorate a function with arguments. For this, only the inner function & function being decorated
# need to know about the arguments.
def add_logging2(func):
    def inner(an_argument):
        print 'calling ' + func.__name__ + ' with argument ' + an_argument
        func(an_argument)
        print 'done calling.'
    return inner

@add_logging2
def another_decorated_function(name):
    print 'hello, ' + name

another_decorated_function('you!')

# You can write a decorator for methods with any number of arguments by passing in an argument tuple
def add_logging_to_anything(func):
    def inner(*args):
        print 'calling ' + func.__name__
        func(*args)
        print 'done calling.'
    return inner

@add_logging_to_anything
def no_arg_decorated_function():
    print 'called with no args'

@add_logging_to_anything
def one_arg_decorated_function(argument):
    print 'called with argument ' + argument

@add_logging_to_anything
def three_arg_decorated_function(first_arg, second_arg, third_arg):
    print 'called with first: ' + first_arg + ', second: ' + second_arg + ', and third: ' + third_arg

no_arg_decorated_function()
one_arg_decorated_function('a')
three_arg_decorated_function('a', 'b', 'c')

# You can pass arguments into decorators to change the way the decorator works, but it's a bit more complex
# You need to make another function to wrap the decorator in that takes the arguments.
def person_says(person_name):
    def person_says_decorator(func):
        def inner():
            print person_name + ' says:'
            func()
        return inner
    return person_says_decorator

@person_says('bob')
def say_hello():
    print 'hello'

@person_says('alice')
def say_hi():
    print 'hi'

@person_says('bob')
def also_says_hi():
    print 'hi'

say_hello()
say_hi()
also_says_hi()
