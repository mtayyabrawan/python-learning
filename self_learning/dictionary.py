# defining dicts
emptyDict = {}  # empty dict
studentInfo = {
    "name": "Muhammad Tayyab",
    "age": 20,
    "isAdult": True,
    "isStudent": True
}

print(studentInfo)
print(len(studentInfo))
print(type(studentInfo))
# retrieving
print(studentInfo["age"])
print(studentInfo.get("age"))
studentInfo["field"] = "Computer Science"
studentInfo[12.9] = "CGPA"
print(studentInfo)
print(studentInfo.get("surname"))  # return None
# print(studentInfo["surname"])  # return Error

# nested dicts
studentInfo = {
    "name": "Muhammad Tayyab",
    "age": 20,
    "city": "Khaur",
    "subjects": {
        "comp": 72,
        "phy": 63,
        "math": 70
    },
    "projects": ["INotebook", "IChat", "AMS System"]
}
print(studentInfo)
print(studentInfo["subjects"]["comp"])
print(studentInfo["projects"][0])
# dict methods
print(list(studentInfo.keys()))
print(list(studentInfo.values()))
print(list(studentInfo.items())[3][1]["comp"])
print(studentInfo.pop("age"))
print(studentInfo.update({"name": "Raza Awan"}))
print(studentInfo)
# print(studentInfo.clear())
