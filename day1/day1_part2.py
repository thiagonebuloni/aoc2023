from enum import Enum

written_nums: list[str] = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digits: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

day1_input = "day1/day1_input.txt"
day1_test = "day1/day1_test.txt"
day1_part2_test = "day1/day1_test_part2.txt"

def open_file() -> list[str]:
    file_name = day1_part2_test

    with open(file_name, 'r') as file:
        data = file.readlines()
    
    return data


def find_written_numbers(partial_line: str) -> list[int]:
    for num in written_nums:
        n = partial_line[:len(num)].find(num)
        if n != -1:
            return [digits[written_nums.index(num)], n + len(num)]
    return [-1, -1]

    
def find_digits(line: str) -> int:
    nums: list[int] = []
    # index_list: list[int] = []
    i = 0
    while i < len(line):
        if (line[i].isdigit()):
            nums.append(int(line[i]))
            i += 1
        else:
            num, index = find_written_numbers(line[i:])
            if num != -1:
                nums.append(num)
                i += index
            else:
                i += 1
    first = str(nums[0])
    last = str(nums[-1])
    n = int(''.join([first, last]))
    return int(n)


data = open_file()
total_amount = 0
for line in data:
    amount = find_digits(line)
    total_amount += amount

print(total_amount)

