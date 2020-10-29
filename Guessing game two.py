## It's a number guessing game. User must choose a number between 1 to 1000 and keep in mind.
## And this programe will find the number.
## It will guess different number untill it find the user number. Abd every time it guesses
## a number it will show the user and ask for feedback.


import random

user_input = {"1" : "Too high", "2" : "High", "3" : "Too low", "4" : "low", "5" : "Match"}
guess_low = 0
guess_high = 1001
guess_mid = random.randint(0, 1000)  ## At first it will select a random number 
print("\n>>>>--WELCOME TO GUESSING GAME--<<<<")
print("\nChoose a random number in your mind between 0 to 1000\n")
print("Well, i think the number is : ", guess_mid, "\n")

while True:   
    print("1 :> Too high \n2 :> High \n3 :> Too low \n4 :> Low \n5 :> Match")
    user = input("How was my guess!? :> ")
    if int(user) == 1:
        guess_high = guess_mid
        guess_mid = (guess_high+guess_low) // 2
        print("Well, i think the number is : ", guess_mid, "\n")
    elif int(user) == 2:
        guess_mid -= 1      
        print("Well, i think the number is : ", guess_mid, "\n")
    elif int(user) == 3:
        guess_low = guess_mid
        guess_mid = (guess_high+guess_low) // 2
        print("Well, i think the number is : ", guess_mid, "\n")
    elif int(user) == 4:
        guess_mid += 1
        print("Well, i think the number is : ", guess_mid, "\n")
    else:
        print("\nI found it !! It's :> ", guess_mid)
        break
        