import random
from collections import Counter

while True:
	ran_num =  str(random.randint(1000, 9999)) # create a 4 digits random number 
	c = Counter(str(ran_num))# Counter will count dublicate digits in random number 
	if all(value == 1 for value in c.values()):   
		break
# input_num() functioin will take 4 digits number from user to guess the random number  
def input_num():
	n = input("Please enter a number with 4 individual digits : ")
	while True:
		c = Counter(str(n))
		if len(n) != 4 :
			n = input("Please enter a number with 4 digits : ")
		elif any(value > 1 for value in c.values()):
			n = input("Your input number has repeating digits, try another one : ")
		else :
			break
	return n

# print(ran_num)
# print(num)

num = input_num()
while True:
	cows = 0 # cows for every match of digits in same place both user number and random number 
	bulls = 0 # bulls for every miss match of digits in worng place both user number and random number 
	for i in range(4):
		for j in range(4):
			while ran_num[i] == num[j]:
				if i == j:
					cows+=1
					break
				else :
					bulls+=1
					break
	print(" %d cows"%cows, "%d bulls"%bulls)
	if cows == 4:
		print(" Congratulations!!! you find the number ")
		break
	else:
		print("\nTry with different number!!")
		num = input_num()


