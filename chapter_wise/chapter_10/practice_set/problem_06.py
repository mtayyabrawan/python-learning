"""
Can you change the self-parameter inside a class to something else (say
“harry”). Try changing self to “slf” or “harry” and see the effects. No
"""


class Demo:
    def __init__(harry):
        harry.name = "Demo"


print(Demo().name)
