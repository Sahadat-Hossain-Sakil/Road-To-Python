import random
def list_generate():
    a = random.sample(range(50), random.randint(0, 25))
    print("random list is ", format(a))
    return a

def new_list(a):
    new = [a[0], a[-1]]
    return new

x = new_list(list_generate())
print(x)
