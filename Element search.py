# import time
import random

print("\n  1  :  Genarate a list randomly \n  2  :  Create a list by own  \n")
n = int(input(" Please choose an option to proceed (1/2) > ")) 

# we can randomly generate a list with random.smaple()
# or create a list by own.
if n == 1:
    own_list = random.sample(range(50), random.randint(0, 50))
    print(own_list)
elif n == 2:
    own_list = list(int(num) for num in input(" Enter your all list elements separated by space :> ").strip().split())
    print(own_list)

# this loop will sort the list by ascending order 
for i in range(len(own_list)):
    for j in range(len(own_list)-1):
        if own_list[j] > own_list[j+1] :
            own_list[j], own_list[j+1] = own_list[j+1], own_list[j] 
        else :
            continue
# binary search() function will search the user input integer in list. 
# if it finds the integer then it will return True / otherwise it will return False  
def binary_search(List):
    first_index = 0
    num_search = int(input("\nPut an integer to search in the list :>  "))
    end_index = len(List)
    while True :
        middle_index = (first_index + end_index) // 2
        middle_element = List[middle_index]
        if middle_element == num_search :
            return True 
        elif middle_element < num_search :
            first_index = first_index + 1
        else :
            end_index = middle_index
        if (first_index == end_index or List[first_index] == List[-1]) :
            return False    

print(binary_search(own_list))

            