
num1 = int(input("Enter number 1 :"))
total = num1
again = "y"
while again == "y":
    num2 = int(input("Enter number 2 :"))
    total = total + num2
    again = input("add another num y/n? ")

print(total)


