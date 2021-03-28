# Finding the Max of Three numbers without using max() function.
# User input will allow to give only Three numbers.

Numbers = list(map(int, input("\nGive me 3 numbers : ").split( )))

if len(Numbers) == 3 :
    for k in range(2):
        for i in range(2):
            if Numbers[i] < Numbers[i+1] :
                Numbers[i], Numbers[i+1] = Numbers[i+1], Numbers[i]
    print("\nMax Number of those Three is :",Numbers[0])               

else :
    print("\n   Please give only 3 numbers \n ")
        

