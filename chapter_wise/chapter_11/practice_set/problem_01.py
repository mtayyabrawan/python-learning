"""
Create a class (2-D vector) and use it to create another class representing a 3-D
vector.
"""


class Vector2D:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"{self.i}i + {self.j}j")


class Vector3D(Vector2D):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"{self.i}i + {self.j}j + {self.k}k")


vec2 = Vector2D(2, 4)
vec3 = Vector3D(6, 4, 8)
vec2.show()
vec3.show()
