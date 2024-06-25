my_tuple = (1, 2, 3, 4, 5)

# Accessing tuple
print(my_tuple[1])
print(my_tuple[0 : 3])


# creating empty tuple
empty_tuple = ()
print(type(empty_tuple), empty_tuple)

# creating single element tuple
single_element_tuple = (1,)
print(type(single_element_tuple), single_element_tuple)

# tuple unpacking
t = (1, 2, 3, 5, 5)

a, b, c, d, e = t

print(a, b, c, d, e)



# membership checking

is_member = 5 in my_tuple

print(is_member)