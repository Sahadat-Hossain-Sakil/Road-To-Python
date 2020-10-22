# prime_or_not(num) function will check the input number if is prime or not 

def prime_or_not (num):            
    a = [i for i in range(2, num) if num % i ==0]
    if num > 1 :
        if len(a) == 0 :
            return print(num, "is a prime number ")
        else :
            return print(num, " is not a prime number ")
    else :
        return print(num, "is not a prime number ")

while(True):
    num = int(input("Enter a number for test : "))
    prime_or_not(num)
