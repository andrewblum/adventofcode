#  day 1
# file = open('advent_input.txt')

# l = file.read().split()

# for n in l: 
#     for n2 in l:
#         if str(2020 - int(n) - int(n2)) in l: 
#             print('FOUND')
#             print(n)
#             print(n2)
#             print(2020 - int(n) - int(n2))
#             print((2020 - int(n) - int(n2)) * int(n) * int(n2))




# day 2
# from collections import Counter

# file = open('advent_input.txt')
# lines = file.readlines()
# valid = 0
# for line in lines: 
#     line = line.strip().split(':')
#     password = line[1][1:]
#     letter = line[0][-1]
#     ranges = line[0][:-2].split('-')
#     start_range = int(ranges[0])
#     end_range = int(ranges[1])
#     letter_occurance = Counter(password)[letter]
#     valid += int(start_range <= letter_occurance <= end_range)
# print(valid)

# part 2
#     if start_range < len(password) or end_range < len(password):
#         valid += int((password[start_range-1] == letter) ^ (password[end_range-1] == letter))
# print(valid)

# day 3 

# file = open('advent_input.txt')
# lines = file.readlines()
# grid = []
# for line in lines: 
#     line = list(line.strip())
#     grid.append(line)

# def walk(rstep, cstep, grid):
#     tree_count, row, col = 0, 0, 0
#     while row < len(grid):
#         wrapped_col = col % len(grid[0])
#         if grid[row][wrapped_col] == '#':
#             tree_count += 1
#         row += rstep
#         col += cstep
#     return tree_count

# total = 1
# for cstep, rstep in [(1,1), (3,1), (5, 1), (7,1), (1,2)]:
#     total *= walk(rstep, cstep, grid)

# print(total)

# day 4 

# file = open('advent_input.txt')
# lines = file.readlines()
# current_passport = {}
# valid = 0
# for i, line in enumerate(lines): 
#     if line == '\n': 
#         byr = current_passport.get('byr', '')
#         byr = byr.isdigit() and int(byr) >= 1920 and int(byr) <= 2002

#         iyr = current_passport.get('iyr', '')
#         iyr = iyr.isdigit() and int(iyr) >= 2010 and int(iyr) <= 2020

#         eyr = current_passport.get('eyr', '')
#         eyr = eyr.isdigit() and int(eyr) >= 2020 and int(eyr) <= 2030

#         hgt = current_passport.get('hgt', '')
#         hgt = ((
#             len(hgt) == 5 and 
#             hgt[-2:] == 'cm' and 
#             hgt[:-2].isdigit() and 
#             int(hgt[:-2]) >= 150 and 
#             int(hgt[:-2]) <= 193
#         )
#             or 
#         (
#             len(hgt) == 4 and 
#             hgt[-2:] == 'in' and 
#             hgt[:-2].isdigit() and 
#             int(hgt[:-2]) >= 59 and 
#             int(hgt[:-2]) <= 76
#         ))

#         hcl = current_passport.get('hcl', '')
#         hcl = len(hcl) == 7 and hcl[0] == '#'
#         c = ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#         hcl = hcl and all([l in c for l in current_passport.get('hcl')[1:]])

#         ecl = current_passport.get('ecl', '')
#         ecl = ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

#         pid = current_passport.get('pid', '')
#         pid = pid.isdigit() and len(pid) == 9

#         valid += int(byr and iyr and eyr and hgt and hcl and ecl and pid)
#         current_passport = {}
#     else:
#         line = line.strip().split()
#         for entry in line:
#             entry = entry.split(":")
#             current_passport[entry[0]] = entry[1]

# print(valid)

#day 5 
# file = open('advent_input.txt')
# lines = file.readlines()
# m = 0
# mini = 1000000000000000
# total = 0
# count = 0
# seen = {}
# for line in lines: 
#     line = line.strip()
#     row = ''.join([str(int(n == 'B')) for n in line[:-3]])
#     col = ''.join([str(int(n == 'R')) for n in line[-3:]])
#     m = max(m, int(row, 2) * 8 + int(col, 2))
#     mini = min(mini, int(row, 2) * 8 + int(col, 2))
#     total += int(row, 2) * 8 + int(col, 2)

# print(((((m - mini) + 1) * (mini + m)) / 2) - total)

# day 6 


# file = open('advent_input.txt')
# lines = file.readlines()
# group = {}
# total, people = 0, 0
# for i, line in enumerate(lines): 
#     line = line.strip()
#     if line != '':
#         people += 1
#         for answer in line:
#             group[answer] = group.get(answer, 0) + 1
#     if line == '' or i == len(lines)-1:
#         total += len([a for a in group.values() if a == people])
#         people = 0
#         group = {}
# print(total)
