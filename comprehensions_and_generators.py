# Comprehension syntax is a readable way of applying transforms to collection - i.e., creating new collections
# that are modified versions of the original. This doesn't change the original collection.

# For instance, given an original list like the below that contains both ints and strings:
a_list = [1, 2, 3, 4, 'a', 'b', 'c']
print(a_list)

# You can use a comprehension to filter the list, pulling out only the integers.
ints_list = [element for element in a_list if isinstance(element, int)]
print(ints_list)

# Comprehensions work by running the code inside the []'s for each element in the list - this code gets
# executed immediately when the comprehension is declared. For large collections, this may not be what you want.
# Generators are sort of like comprehensions in that they can transform collections into other collections, but
# unlike comprehensions, the generator expression gets executed only when you access its elements with an iterator
# or a for-loop.
ints_comprehension = (element for element in a_list if isinstance(element, int))

print(ints_comprehension) # note that it doens't print a list - just the comprehension object.

# You can access the elements of a comprehension using an iterator, or a for loop.
print(next(ints_comprehension))
print(next(ints_comprehension))

for each in ints_comprehension:
    print(each)

