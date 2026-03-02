"""
Write a program to generate multiplication tables from 2 to 20 and write it to the
different files. Place these files in a folder for a 13 – year old.
"""

from os import listdir, mkdir


DIR_NAME = "Multiplication-Tables"

dir_content = listdir("./")

if (dir_content.count(DIR_NAME) <= 0):
    mkdir(DIR_NAME)


def gen_table(num):
    print(f"Generating Multiplication table of {num}")
    table = []
    for i in range(1, 11):
        table.append(f"{num} X {i} = {num*i}")
    return table


def generate_file_name(table_val):
    return f"./{DIR_NAME}/Multiplication-Table-Of-{table_val[:table_val.find("X")].strip()}.txt"


def store_in_file(table):
    with open(generate_file_name(table[0]), "w") as table_file:
        table_file.write("\n".join(table))


def generate_tables(start=2, end=10):
    for i in range(start, end+1):
        store_in_file(gen_table(i))


generate_tables(end=20)
