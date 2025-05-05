# create a file "practice.txt" and add this data ....

with open("practice.txt", "w") as file:
    file.writelines(
        [
            "Hi everyone\n",
            "we are learning File I/O\n",
            "using Java.\n",
            "I like programming in Java.\n",
        ],
    )
    file.close()

# WAF to replace all java occurrences with python


def replaceInFile(old, new, filename):
    with open(filename, "r") as file:
        data = file.read()
        data = data.replace(old, new)
        file.close()
        with open(filename, "w") as file:
            file.write(data)
            file.close()


replaceInFile("Python", "JavaScript", "practice.txt")


# search if the word a specific word exist in file or not


def searchWord(word, filename):
    with open(filename, "r") as file:
        data = file.read()
        file.close()
        if data.find(word) >= 0:
            return (
                f"'{word}' is present at index {data.find(word)} of file '{filename}'"
            )
        else:
            return f"'{word}' not found in file '{filename}'"


print(searchWord("learning", "practice.txt"))


# WAF to find line of the file does a specific word occur first


def searchLine(word, filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        file.close()
        for line in enumerate(lines):
            if line[1].find(word) >= 0:
                return f"'{word}' found on line no. {line[0]+1} at index {line[1].find(word)} of file '{filename}'"
        return f"'{word}' not found in file '{filename}'"


print(searchLine("learning", "practice.txt"))

# count even numbers from the numbers in file separated with commas

with open("numbers.txt", "r") as file:
    numbers = file.read()
    file.close()
    numbers = numbers.split(",")
    evenCount = 0
    for number in numbers:
        if int(number) % 2 == 0:
            evenCount += 1
    print(f"Even number count : {evenCount}")
