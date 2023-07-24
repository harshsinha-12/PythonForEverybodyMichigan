'''n = 3
for i in range(n):
    for j in range(i + 1):
        print("*", end="")
    print()'''


for i in range(3):
    for j in range(3):
        if i == 1:
            print("* *", end = "")
            break
        else:
            print("*", end="")   
    print()

