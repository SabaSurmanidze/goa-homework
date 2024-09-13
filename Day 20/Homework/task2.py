x = [1,2,56,89,23,45,67,81,101]
print(x)
num = int(input("enter some number from the list:"))

if num == 23:
    print("bingo")
elif num not in x:
    print("this number isnt in list")
else:
    print("you entered wrong number")