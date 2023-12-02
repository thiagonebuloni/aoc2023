with open("day1_input.txt", 'r') as file:
    data = file.readlines()

nums = []
for line in data:
    i = 0
    n = []
    for char in line:
        try:
            num = char
            if isinstance(int(num), int):
                n.append(num)
        except:
            continue
    nums.append(int(n[0] + n[-1]))
    
print(sum(nums))
