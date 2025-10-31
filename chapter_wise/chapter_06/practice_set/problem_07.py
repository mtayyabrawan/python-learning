"""
Write a program to find out whether a given post is talking about 'Tayyab' or not.
"""

post = input("Enter post content : ").lower()

if "tayyab" in post:
    print("Post is about you tayyab")
else:
    print("No post is not about you")
