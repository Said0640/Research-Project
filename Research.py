import random

categories = ["A", "B", "C"]
weights = [0.33, 0.33, 0.34]

count_A = 0
count_B = 0
count_C = 0

for i in range(50):
    recommendations = random.choices(categories, weights)[0]

    if recommendations == "A":
        count_A += 1
    elif recommendations == "B":
        count_B += 1
    else:
        count_C += 1

    click = random.random()

    if click < 0.5:
        clicked = "A"
    elif click < 0.75:
        clicked = "B"
    else:
        clicked = "C"

    if clicked == "A":
        weights[0] += 0.05
    elif clicked == "B":
        weights[1] += 0.05
    else:
        weights[2] += 0.05

    # keep result total = 1
    total = sum(weights)
    weights[0] /= total
    weights[1] /= total
    weights[2] /= total

print("A shown:", count_A)
print("B shown:", count_B)
print("C shown:", count_C)