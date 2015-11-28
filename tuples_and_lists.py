# Tuples in Python are a collection type that can contain any object, including other tuples.
# Tuples will not led you add, remove, or change objects inside them.
a_tuple = (('hello', 'goodbye'), 1, 'a', 9.3, 'asdf')
print a_tuple

# Tuples can be accessed by index. Forward indexes start at 0 for the first element, and so on.
print a_tuple[3]

# You can access items inside nested tuples by indexing to the nested tuple, and then indexing within it.
print a_tuple[0][1]

# You can use 'negative' indexes in Python, which just counts backwards from the end of the tuple.
# Note: Unlike forward indexes, which start at 0 for the first element,
# negative indexes start at -1 for the last element.
print a_tuple[-1]
print a_tuple[4]
print a_tuple[-2]
print a_tuple[3]

# Slice notation is Python's cool syntax for getting part of a list by using an index like [start_index:end_index].
# The end_index is not inclusive - in other words, you will get elements starting at start_index, and just before
# the end-index that you specify.
print a_tuple[2:4]
print a_tuple[2:5]

# If you don't provide a start or end index, get everything between what you specify from/to beginning/end of the list.
print a_tuple[:2]
print a_tuple[3:]

# In addition to using indexes, you can access the elements of a tuple one at a time using a for-loop.
for each in a_tuple:
    print each

# This even works for slices of tuples.
for each in a_tuple[3:]:
    print each

# You can also access a tuple's elements one-at-a-time outside of a for-loop using iterators. An iterator starts at
# the first element in the list, and gets you the next element every time you access it, like this:
an_iterator_for_a_tuple = iter(a_tuple) # this gets an iterator for a tuple.
print an_iterator_for_a_tuple.next()
print an_iterator_for_a_tuple.next()

# You can for-loop over the elements of an iterator, but this will only give you access to the elements that haven't
# already been iterated over - in other words, whatever's "left" after previous calls to 'next'.

for each in an_iterator_for_a_tuple:
    print each

# You can test whether a tuple contains an element with the 'in' keyword.
print 9.3 in a_tuple # true
print 10 in a_tuple # false

# Tuple unpacking is a really cool feature in python that lets you assign a tuple to a bunch of variables
a, b = ('a', 'b')
print a
print b

# The reverse, called tuple packing, also works. Every time you assign a comma-seperated list of values
# to something, Python assumes that you mean to assign a tuple.
ab = 'a', 'b'
print ab

# This allows you to use some really cool syntax, like
a, b = b, a
print a
print b


# Lists are like tuples, but you can add, remove, or change items.
# Lists are accessed just like tuples, by index. Unpacking and slicing work just like with tuples.
a_list = [['hello', 'goodbye'], 1, 'a', 9.3, 'asdf']
print a_list

# You can add new elements to a list
a_list.append('thing 1')
a_list.append('thing 2')
print a_list

# You can remove elements from a list by index
del a_list[6]
print a_list

# You can remove the first occurrence of a certain item from a list
a_list.remove('thing 1')

# But if you have the same object twice in a list, only the first occurance is deleted.
a_list.append('a')
print a_list
a_list.remove('a')
print a_list

# You can modify items in a list
a_list[3] = 9.5

# You can 'extend' a list by adding another list (or tuple) to it.
another_list = ['a', 'b']
print another_list

another_list.extend(['c','d'])
print another_list

another_list.extend(('e','f'))
print another_list
