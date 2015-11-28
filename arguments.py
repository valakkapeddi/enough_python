##

def print_the_thing(thing):
    print thing

print_the_thing('a thing')


# A parameter with * in front of it tells Python to accept a list of arguments
# It doesn't actually have to be called *args, but that's the convention.
# You can access things in the tuple parameter by index.
# The arguments need not all be the same type.
def takes_arg_tuple(*args):
    print args
    print args[0]
    print args[1]

takes_arg_tuple('a', 2)


# You can also mix regular parameters & tuple parameters (*args). Arguments are assigned to the regular
# parameters first, and whatever is lest is added to the tuple parameter.
# The tuple parameter (*args) always has to be the last parameter specified.
# Can you explain why?
def tuple_arg_sequence(an_arg, *args):
    print an_arg
    print args

tuple_arg_sequence('a', 2, 'asdfads')


# Python's neatest trick is that it can 'unpack' a tuple into a list of variables.
# This also works with lists, sets, and dictionaries (except each value there is a key-value pair).
def tuple_unpacking_args(*args):
    a, b = args
    print a
    print b

# As well as tuple parameters, Python also supports dictionary or 'keyword' arguments.
# Keyword arguments are accessed by  argument name as a string instead of via integer indexes.
# When using keyword arguments, sequence is not important.
def dict_args(**kwargs):
    print kwargs['alice']
    print kwargs['bob']

dict_args(bob=3, alice=5)

# You can mix regular parameters, argument tuples, and dictionary arguments, but sequence matters.
# Regular parameters have to go first, then your arg tuple, then your dictionary arguments.
def different_parameter_types(thing, *args, **kwargs):
    print thing
    print args
    print kwargs

different_parameter_types('thing is asdf', 3, 'something else', planet='earth', answer=42)

# Functions that belong to a class (methods) require at least one argument.
# This argument represents the current instance of the class.
# Python is whacky that way.
class KittyKat:
    def angry_noise(self):
        'hiss'
    def happy_noise(self):
        'purr'

cat = KittyKat()
print cat.angry_noise()
print cat.happy_noise()
