num = int(input("Enter a number for divide :"))
divisor = []
for i in range(1, num+1):
    if num % i == 0 :
        divisor.append(i)
print(divisor)
