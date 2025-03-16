# defining string
str1 = "HelloWorld"
str1 = "HelloWorld"
str1 = """HelloWorld"""
# defining multiline strings
multiStr = """
Lorem ipsum dolor sit amet, consectetur adipisicing elit. Atque repellendus culpa commodi earum cumque voluptatum nobis officia rem nostrum consequatur? Reprehenderit sed quibusdam, est suscipit minima qui error dolor et natus, quo molestias. Laborum ipsa eum dolorum pariatur totam numquam voluptatum, error ex doloribus quia modi dolores maxime accusantium enim, molestiae laudantium, atque beatae necessitatibus aperiam eaque quidem? Omnis esse rem adipisci temporibus quidem. Ullam veniam fugiat incidunt? Ab assumenda tempore perspiciatis omnis, iusto totam id nemo consequatur vitae vero, veritatis aperiam minima sed, ullam nulla laudantium eaque. Reiciendis rem sit aspernatur ducimus distinctio natus. Voluptatum beatae ipsa doloribus aperiam.
"""
# using escape sequence in strs
str2 = "This str is using escape sequence of new line \n and tab space \t for formatting str"
# operations on strings
# concatenation
firstStr, secondStr = "Hello", "World"
finalStr = firstStr + secondStr
print(finalStr)
finalStr = firstStr + " " + secondStr
print(finalStr)
# repetition
finalStr = firstStr * 4
print(finalStr)
# finding length
finalStrLen = len(finalStr)
print(finalStrLen)
# indexing in str
firstChar = finalStr[0]
print(firstChar)
lastchar = finalStr[-1]
print(lastchar)
midChar = finalStr[finalStrLen//2]
print(midChar)
# slicing
string = "this is string that can be sliced."
# 0 to 7 index but slicing doest not include value of ending index
substr = string[:7]
print(substr)
substr = string[8:]  # index 8 to len(string)
print(substr)
substr = string[5:10]  # 5 to 10
print(substr)
substr = string[-11:-6]
print(substr)
# string methods
newstr = "built in methods of strings in python"
# return True of that string is ending with given substr
print(newstr.endswith("on"))
print(newstr.capitalize())
print(newstr.upper())
print(newstr.lower())
name = "Muhammad"
print("My name is {0}".format(name))
print(".".join(["my", "name", "is", "muhammad", 'tayyab']))
print(newstr.index("str"))
print(newstr.replace("string", "list"))
print(newstr.center(100, " "))
print(newstr.title().istitle())
print(newstr.title())
print(newstr.count("i"))
