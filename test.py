from enum import Enum

class written_nums(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9


line: str = "onetwothree"
lista = ["one", "two", "three"]

extract = []
for i in written_nums:
    if i in line:
        extract.append(i)
        index = line.find(i)
        if index != -1:
            line = line[:index] + line[index + len(i):]
    print(line)
