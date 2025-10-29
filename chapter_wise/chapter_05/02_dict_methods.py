"""
Dictionary Methods
"""

user_info = {
    "username": "mtayyabrawan",
    "password": "12345678",
    "isVerified": True,
    "role": "admin",
}

print(user_info.keys())  # returns list of all keys of the dictionary

print(user_info.values())  # returns list of all values of the dictionary

print(
    user_info.items()
)  # returns list of set of each key values pairs of the dictionary

print(user_info.pop("password"))  # removes items with gien key

print(user_info)

print(user_info.popitem())  # removes last item from the list

print(user_info)

user_info.update(
    {"password": "87654321", "email": "tayyab@example.com"}
)  # updates the list with given list

print(user_info)

user_info.clear()  # clears the dictionary

print(user_info)
