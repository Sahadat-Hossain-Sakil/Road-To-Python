# This code will make a random list and then make another list 
# with first and last element of random list.

import random
def list_generate():
    a = random.sample(range(50), random.randint(0, 25)) # It will return a random list called ' a '
    print("random list is ", format(a))
    return a

def new_list(a):
    new = [a[0], a[-1]]  # It will create a new list with first and last element of list ' a '
    return new

x = new_list(list_generate())
print(x)
