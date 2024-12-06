# --- Day 3: Mull It Over ---
from re import findall

with open("../input.txt", "r") as file:
    content = file.read()

sum1 = 0
sum2 = 0
enable = True
for a, b, do, dont in findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", content):
    if do:
        enable = True
        continue
    if dont:
        enable = False
        continue
    multips = int(a) * int(b)
    sum1 += multips
    sum2 += multips * enable

print("Part I: ", sum1)
print("Part II: ", sum2)
