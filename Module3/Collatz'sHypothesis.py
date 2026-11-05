
integer = int(input("Please enter a number (non-negative and non-zero): "))
steps = 0
while integer != 1:
    if integer % 2 == 0:
        integer = integer // 2
    else:
        integer = integer * 3 + 1
    print(integer)
    steps += 1
print("Steps:", steps)