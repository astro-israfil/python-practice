person = {
    "name": "Israfil",
    "age": 20,
    "isProgrammer": True,
    "friends": ["Abdullah", "Omar", "Osman"]
}

print(person.items())
print(person.values())
print(person.get("name"))
print(person.get("profession"))

person.update({
    "isProgrammer": False, 
    "name": "Khalid"
})

print(person)


isProgrammer = person.pop("isProgrammer")

print(isProgrammer)
print(person)