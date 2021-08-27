total = 0
for i in range(0,3):
    num = int(input("Enter 3 numbers: "))
    ans = input("continue y/n? :")
    if ans == "y":
        total = total + num
print(total)