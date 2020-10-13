import random


def generate_gardens(num_gardens: int, upper: int):
    lst = []
    for _ in range(num_gardens):
        # lst.append((1,1))
        lst.append((random.randint(0, upper), random.randint(0, upper)))
    return lst


def find_smartest_brute_force(gardens):
    smartest = []
    for i in range(len(gardens)):
        target1, target2 = gardens[i]
        smart = True
        for j in range(len(gardens)):
            if j == i:
                continue
            other1, other2 = gardens[j]
            if target1 < other1 and target2 < other2:
                smart = False
        if smart:
            smartest.append((target1, target2))
    return len(smartest), smartest


test = [(27, 88), (96, 45), (85, 68), (73, 44), (71, 73), (87, 42), (55, 95)]

a = generate_gardens(10, 100)
print(a)
print()
print(find_smartest_brute_force(test))
