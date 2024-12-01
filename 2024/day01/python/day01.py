# 2024 Advent of Code: --- Day 1: Historian Hysteria ---

def open_input(location) -> list:
    input = open(location)
    content = input.readlines()
    input.close()
    return content

# part 1

a_list = []
b_list = []
content = open_input('../input.txt')

for line in content:
    a, b = line.split("   ")
    a = int(a.strip())
    b = int(b.strip())
    a_list.append(a)
    b_list.append(b)

a_list.sort()
b_list.sort()

i = 0
sum_dist = 0
while i < len(a_list):
    distance = abs(a_list[i] - b_list[i])
    sum_dist += distance
    i += 1

print("part I:", sum_dist)

# part 2

sim_score = 0

for num in b_list:
    if num in a_list:
        sim_score += num

print("Part II:", sim_score)