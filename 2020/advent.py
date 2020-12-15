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
# grid = [list(line.strip()) for line in lines]

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
# groups = [group.split('\n') for group in file.read().split('\n\n')]
# total = 0
# for group in groups: 
#     count = {}
#     for person in group: 
#         for answer in person:
#             count[answer] = count.get(answer, 0) + 1
#     total += len([a for a in count.values() if a == len(group)])
# print(total)

# day 7 

# file = open('advent_input.txt')
# graph = {}
# for line in file.readlines():
#     bag, contents = line.split('contain')
#     bag = bag[:-6]
#     for content in contents.split(','): 
#         inner_bag = ' '.join(content.strip()[2:].split()[:2])
#         v = graph.get(inner_bag, set())
#         v.add(bag)
#         graph[inner_bag] = v

# total = 0
# seen = set()
# q = graph['shiny gold']
# while q: 
#     cur = q.pop()
#     if cur not in seen:
#         seen.add(cur)
#         total += 1
#         if cur in graph:
#             q = q.union(graph[cur])
# print(total)

#part 2
# file = open('advent_input.txt')
# graph = {}
# for line in file.readlines():
#     bag, contents = line.split('contain')
#     bag = bag[:-6]
#     bags = set()
#     for content in contents.split(','): 
#         count = content.strip()[0]
#         inner_bag = ' '.join(content.strip()[2:].split()[:2])
#         if count != 'n':
#             bags.add((inner_bag, int(count)))
#     graph[bag] = bags

# def walk(node):
#     return sum([(child[1] * walk(child)) + child[1] for child in graph[node[0]]])

# print(walk(('shiny gold', 1))) 


# day 8 

# file = open('advent_input.txt')
# lines = [l.strip() for l in file.readlines()]

# def run(cur, acum, seen, can_change):
#     while cur not in seen and cur < len(lines): 
#         seen.add(cur)
#         cmd, arg = lines[cur][:3], int(lines[cur][4:])
#         if cmd == 'acc':
#             acum += arg
#         if cmd == 'jmp':
#             if can_change:
#                 run(cur + 1, acum, seen.copy(), False)
#             cur += arg
#         else:
#             if cmd == 'nop' and can_change:
#                 run(cur + arg, acum, seen.copy(), False)
#             cur += 1
#     if cur == len(lines):
#         print(acum)

# seen = set()
# run(0, 0, seen, True)

# day 9 



# file = open('advent_input.txt')
# nums = [int(l.strip()) for l in file.readlines()]

# def two_sum(target, available):
#     return any([target - n in available for n in available])

# preamble = 25
# cur = preamble
# available = set(nums[:preamble])

# while cur < len(nums):
#     if not two_sum(nums[cur], available):
#         target = nums[cur] 
#     available.remove(nums[cur - preamble])
#     available.add(nums[cur])
#     cur += 1

# print(target)

# # part 2
# start, end, total = 0, 0, 0

# while total != target: 
#     if total < target:
#         total += nums[end]
#         end += 1
#     else: 
#         total -= nums[start]
#         start += 1

# print(min(nums[start:end]) + max(nums[start:end]))

# day 10 

# file = open('advent_input.txt')
# nums = [int(l.strip()) for l in file.readlines()]
# target = max(nums)
# adapters = set(nums)
# adapters.add(0)
# memo = {}

# def walk(node):
#     if node in memo:
#         return memo[node]
#     total = 0
#     if node == target: 
#         return 1
#     if node+3 in adapters:
#         total += walk(node+3)
#     if node+2 in adapters:
#         total += walk(node+2)
#     if node+1 in adapters:
#         total += walk(node+1)
#     memo[node] = total
#     return total 

# print(walk(0))


# day 11 

# part 1 helper
# def num_adj_ppl(i, j):
#     occupied = 0
#     for x, y in [(1, 1), (0, 1), (1, 0), (-1, -1), (0, -1), (-1, 0), (-1, 1), (1, -1)]:
#         if i-x < 0 or j-y < 0:
#             continue
#         if i-x >= len(seats) or j-y >= len(seats[0]):
#             continue
#         occupied += int(seats[i-x][j-y] == '#')
#     return occupied

# part 2 helper
# def num_adj_ppl2(i, j):
#     total = 0
#     for x, y in [(1, 1), (0, 1), (1, 0), (-1, -1), (0, -1), (-1, 0), (-1, 1), (1, -1)]:
#         total += run_line(i+x, j+y, x, y)
#     return total

# def run_line(i, j, stepi, stepj):
#     if i < 0 or j < 0:
#         return 0 
#     if i >= len(seats) or j >= len(seats[0]):
#         return 0 
#     if seats[i][j] == 'L':
#         return 0
#     if seats[i][j] == '#':
#         return 1
#     return run_line(i+stepi, j+stepj, stepi, stepj)

# file = open('advent_input.txt')
# seats = [list(l.strip()) for l in file.readlines()]
# changes = True
# while changes:
#     changes = False
#     new_seats = []
#     for i, row in enumerate(seats):
#         new_row =[]
#         for j, seat in enumerate(row):
#             new_seat = seat
#             if seat == '.':
#                 new_seat = '.'
#             elif num_adj_ppl2(i,j) == 0:
#                 new_seat = '#'
#             elif num_adj_ppl2(i,j) > 4:
#                 new_seat = 'L'
#             if new_seat != seat:
#                     changes = True
#             new_row.append(new_seat)
#         new_seats.append(new_row)
#     seats = new_seats
# print(sum([row.count('#') for row in seats]))

# day 12 
# file = open('advent_input.txt')
# moves = [l.strip() for l in file.readlines()
# east, north = 10, 1
# ship_e, ship_n = 0,0
# for move in moves: 
#     action = move[0]
#     amt = int(move[1:])
#     if action == 'N':
#         north += amt
#     if action == 'S':
#         north -= amt
#     if action == 'E':
#         east += amt
#     if action == 'W':
#         east -= amt
#     if action == 'F':
#         ship_e +=  amt * east
#         ship_n +=  amt * north
#     if action == 'L':
#         if amt == 90:
#             east, north = north *-1, east
#         if amt == 270: 
#             east, north = north, east *-1
#     if action == 'R':
#         if amt == 90:
#             east, north = north, east * -1
#         if amt == 270: 
#             east, north = north* -1, east
#     if move == 'L180' or move == 'R180':
#         east, north = east *-1 , north *-1
# print(abs(ship_e) + abs(ship_n))

# day 13 
import math
file = open('advent_input.txt')
moves = [l.strip() for l in file.readlines()]
buses = [(int(n), i) for i, n in enumerate(moves[1].split(',')) if n != 'x']
mults = [x + y for x, y in buses]
# print(math.lcm(mults))
# print(buses)
def check(t):
    for n in buses:
        if ((t+n[1]) % int(n[0])) != 0:
            return False
    return True 

# t = (971-48) * 1000000000000000
# while not check(t):
#     t += 971

# print(t)


# day 15

from collections import deque, defaultdict
occurances = defaultdict(lambda : deque(maxlen=2))
nums = [2,0,1,7,4,14,18]
for i, n in enumerate(nums[:-1]):
    occurances[n].append(i+1)
prev = nums[-1]
for curr_index in range(len(nums), 2020):
    occurances[prev].append(curr_index)
    cur = 0
    if prev in occurances and len(occurances[prev]) > 1: 
        cur = occurances[prev][-1] - occurances[prev][-2]
    prev = cur
print(prev)






