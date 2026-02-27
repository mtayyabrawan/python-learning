"""
Write a python function to remove a given word from a list and strip it at the same
time.
"""


def remove_word(words_list, word):
    n = []
    words_list.remove(word)
    for w in words_list:
        n.append(w.replace(word, "").strip())
    return n


w_list = ["Tayyab", "Raza", "Ali", "Jaleel", "Ahmed Ali"]

print(remove_word(w_list, "Ali"))
