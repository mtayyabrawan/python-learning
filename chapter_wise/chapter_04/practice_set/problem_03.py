"""
Check that a tuple type cannot be changed in python.
"""

random_tup = ("Muhammad Tayyab", False, 78, "Mango", "Attock")

random_tup[0] = "Abdullah"  # Gives error
