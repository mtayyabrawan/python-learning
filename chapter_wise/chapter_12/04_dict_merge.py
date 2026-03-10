from typing import Dict, Union


type StudentDict = Dict[str, Union[str, int]]
type MarksDict = Dict[str,  int]

st: StudentDict = {"name": "Muhamamd Tayyab", "age": 21}
marks: MarksDict = {"math": 132, "computer": 151}

print(st | marks)

st |= marks

print(st)


with (open("file_1.txt", "w") as f1, open("file_2.txt", "w") as f2):
    f1.write("Hello World in File 1")
    f2.write("Hello World in File 2")
