def to_num(vec) -> list:
    return [int(x) for x in vec]

def is_safe(vec) -> bool:
    num = to_num(vec)
    increasing = all(num[i] < num[i + 1] for i in range(len(num) - 1))
    decreasing = all(num[i] > num[i + 1] for i in range(len(num) - 1))
    
    if not (increasing or decreasing):
        return False
    
    for i in range(len(num) - 1):
        difference = abs(num[i] - num[i + 1])
        if difference < 1 or difference > 3:
            return False
            
    return True

def can_be_safe_with_removal(vec) -> bool:
    for i in range(len(vec)):
        modified_vec = vec[:i] + vec[i+1:] 
        if is_safe(modified_vec):
            return True
    return False

with open("../input.txt", "r") as file:
    content = file.readlines()

# Part I
counter = 0
for line in content:
    vector = line.split()
    if is_safe(vector):
        counter += 1
print("Part I: ", counter)

# Part II
counter2 = 0
for line in content:
    vector = line.split()
    if is_safe(vector) or can_be_safe_with_removal(vector):
        counter2 += 1

print("Part II: ", counter2)
