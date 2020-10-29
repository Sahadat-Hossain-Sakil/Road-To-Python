def dot_line():
    print(" ..."*(size-1))

def var_line():
    print("|   "*size)
size = int(input("\nEnter your game board size : "))
size += 1
for i in range(size):
    dot_line()
    if i < size-1 :
        var_line()
print("\n")

