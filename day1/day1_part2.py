from enum import Enum

written_nums: list[str] = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digits: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def open_file() -> list[str]:
    file_name = "day1/day1_test_part2.txt"

    with open(file_name, 'r') as file:
        data = file.readlines()
    
    return data


def find_written_nums(line) -> list:
    extract: list[str] = []
    index_list: list[str] = []
    for char in written_nums:
        if char in line:
            extract.append(char) # type: ignore
            index = line.find(char)
            print(index)
            if index != -1:
                line = line[:index] + line[index + len(char):] # type: ignore
                index_list.append(index)
    return [extract, index_list]
        

# def find_index(line: str) -> list[int]:
#     index_list: list[int] = []
#     for num in line_list:
#         index_list.append(line.index(num))


# def find_digits(line: str) -> list[list[int]]:
#     nums: list[int] = []
#     index_list: list[int] = []
#     for i in range(len(line)):
#         try:
#             if isinstance(int(line[i]), int):
#                 nums.append(int(line[i]))
#                 index_list.append(i)
#         except Exception:
#             continue

#     return [nums, index_list]






#############






def find_digits(line: str) -> list[int]:
    nums: list[int] = []
    # index_list: list[int] = []
    for i in range(len(line)):
        if (line[i].isdigit()):
            nums.append[int(line[i])] # type: ignore
        else:
            num = find_written_numbers(line[i:])
            if num != -1:
                nums.append(num)


            

    return nums

#############

def find_written_numbers(partial_line: str) -> int:
    for num in written_nums:
        n = partial_line.find(num)
        if n != -1:
            return digits[written_nums.index(num)]
    return -1











def find_nums(data: list[str]) -> int:
    final_nums = []
    for line in data:
        
        line_written_nums_list, index_written_nums_list = find_written_nums(line)
        
        digits, index_digits = find_digits(line)
        
        if min(index_written_nums_list) < min(index_digits):
            minor_index = min(index_written_nums_list)
        else:
            minor_index = min(index_digits)
        
        if max(index_written_nums_list) < max(index_digits):
            major_index = max(index_written_nums_list)
        else:
            major_index = max(index_digits)

        num = int(line[minor_index] + line[major_index])
        
        final_nums.append(num)
    
    return sum(final_nums)
    



data = open_file()
total_amount = find_nums(data)
print(total_amount)
