my_set = {1, 4, 5, 5, 7, 9}

print(my_set)

my_set.add(15)
print(my_set)

my_set.remove(5)
print(my_set)

# remove an element of set
poped_item = my_set.pop()
print(poped_item)
print(my_set)


# remove a specific element of set if it is a memeber of set
my_set.discard(15)
print(my_set)



another_set = {3, 8, 9}

union_set = my_set.union(another_set)
print(union_set)

intersection_set = my_set.intersection(another_set)
print(intersection_set)

print(intersection_set.issubset(my_set))
print(my_set.issuperset(intersection_set))