"""
 Write a python program to rename a file to “renamed_by_python.txt.
"""

from shutil import move


move("rename_file.txt", "renamed_by_python.txt")
