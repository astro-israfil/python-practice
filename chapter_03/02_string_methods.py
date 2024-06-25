greeting = "hello world"

print(greeting.capitalize())
print(greeting.upper())
print(greeting.lower())
print(greeting.title())
print(greeting.startswith("hello"))
print(greeting.endswith("world"))
print(greeting.count("l"))
print("1443545".isdigit())
print("Israfil".isalpha())

print(greeting.split(" "))
print(greeting.replace("world", "python"))

print(greeting.index("world"))
print(greeting.find("world"))

greeting1 = "         hello"

print(greeting1.lstrip())

greeting2 = "world     "
print(greeting2.rstrip())