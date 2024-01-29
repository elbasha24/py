# sets are collection on un-indexed objects, no duplicate, no order
# Create an empty set
my_set = set()

# Add elements to a set
my_set.add(1)
my_set.add(2)
my_set.add(3)


# Remove elements from a set
my_set.remove(2)

# Check if an element is in a set
print(1 in my_set)

# Loop through a set
for x in my_set:
  print(x)


    # add(element): Adds an element to the set.
    # clear(): Removes all elements from the set.
    # copy(): Returns a shallow copy of the set.
    # difference(set): Returns a new set containing the difference between the set and another set(s).
    # difference_update(set): Removes all elements from the set that are also present in another set(s).
    # discard(element): Removes the specified element from the set.
    # intersection(set): Returns a new set containing the intersection of the set and another set(s).
    # intersection_update(set): Updates the set with the intersection of itself and another set(s).
    # isdisjoint(set): Returns True if the set has no elements in common with another set; otherwise, returns False.
    # issubset(set): Returns True if the set is a subset of another set; otherwise, returns False.
    # issuperset(set): Returns True if the set is a superset of another set; otherwise, returns False.
    # pop(): Removes and returns an arbitrary element from the set.
    # remove(element): Removes the specified element from the set. Raises a KeyError if the element is not found.
    # symmetric_difference(set): Returns a new set containing the symmetric difference between the set and another set.
    # union(set): Returns a new set containing the union of the set and another set(s).
