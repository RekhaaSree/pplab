import random
a=random.randrange(1,10)
print(a)
b=int(input("enter number:"))
while a!=b:
    b=int(input("enter number:"))
else:
    print("well guessed")
