import random

def random_list(ran, ele):
    x = [random.randrange(ran) for i in range(ele)]
    print("Random first list : ", x)
    return x

def remove_dublicates(List):
    result = list(set(List))
    return result

Range = int(input("Enter List elements range : "))
Num = int(input("How many elements : "))
final_res = remove_dublicates(random_list(Range, Num))
print("Without dublicates final list : ", final_res)