from typing import Dict, List, Union


name: str = "Muhammad Tayyab"

print(name.casefold())


def welcome(name: str) -> str:
    return f"{name}! Welcome to Python Land"


print(welcome("Muhammad Tayyab"))

marks: List[int] = [110, 115, 46, 43, 132, 120, 151]

student_info: Dict[str, Union[int, str]] = {
    "name": "Muhammad Tayyab", "roll_no": 2103508}
