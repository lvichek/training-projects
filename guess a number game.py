import random

c = random.randrange(1,100)
a = int(input("guess the number from 1 to 100: "))

while a != c :
    if a < c:
        print("nope, it's bigger than your number")
    else :
        print ("nope, but it's less than your number")    
    a = int(input("try again: "))

print("yeah that's it!")    