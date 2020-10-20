import random
print("Find the random number")
s = int(random.randint(0, 101))

guess = int(input("Please guess a number between 1 to 100 : "))
c = 1
while guess != s :   
    if (s > guess) :
        c += 1
        guess = int(input("Please make another guess higher number then before : "))       
    else :
        c += 1
        guess = int(input("Please make another guess lower then before : "))

if (guess == s) :
    print("Congratulations, You find the number with %d attempts " %c)        
        

