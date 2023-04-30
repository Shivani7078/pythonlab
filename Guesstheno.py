import random
random.randint(1,100)
jackpot=random.randint(1,100)
guess=int(input("Enter the number:"))
counter=1
while guess!=jackpot:
    if guess<jackpot:
        print("Guess higher")
    else:
        print("Guess lower")
    guess=int(input("Guess the number"))
    counter=1

print("Right answer")
print("You took",counter,"attempts")
    
