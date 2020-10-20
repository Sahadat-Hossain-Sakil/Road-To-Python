def fib(x, a, b):
    print(a, end=" ")
    while(x>1):
        c = a + b
        a = b
        b = c
        x-=1
        print(c, end=" ")
x = int(input("How many numbers to generate : "))
a = 0
b = 1
fib(x, a, b)
