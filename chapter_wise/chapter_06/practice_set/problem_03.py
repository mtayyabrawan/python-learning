"""
A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
to detect these spams.
"""

sp1, sp2, sp3, sp4 = "make a lot of money", "buy now", "subscribe this", " click this"

message = input("Enter your message here : ").lower()

if sp1 in message or sp2 in message or sp3 in message or sp4 in message:
    print("Message is a spam")
else:
    print("Real Message")
