# Sets are collections of unique items. If the same item is added multiple times to a set, it only appears once.
# To be put into a set, an object must be of a 'hashable' type.
# We'll discuss this further later, but numbers & strings qualify..
a_set = {3,'a',5, 3, 'a'}
print(a_set)

# You can iterate over sets, but cannot access their members with an index.
for each in a_set:
    print(each)
# a_set[0] # Won't work.

# Python sets allow you to do cool set operations, like unions, composed of elements in either set...
union_set = {'a', 'b', 'c'} | {1, 2, 3}
print(union_set)

#  ... Intersections of sets, composed of elements present in both sets
intersection_set = {1, 2, 3, 4} & {3, 4, 5, 6}
print(intersection_set)

#  ... Set difference, which is the list of elements present in the right-hand set, but not in the left
# Extra elements in the right-hand set aren't part of the difference.
difference_set = {1, 2, 3, 4} - {2, 4, 5, 6}

# ... Exclusive-or of sets, which is the set of elements which are NOT present in both sets.
xor_set = {1, 2, 3, 4} ^ {2, 4, 5, 6}

# You can add items to and remove items from sets.
another_set = {'a', 1, 'b', 2}
print(another_set)
another_set.add('c')
print(another_set)
another_set.remove(1)
print(another_set)
