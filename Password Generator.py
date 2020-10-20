import random 
import string


print(" simple--> 1 \n middle--> 2 \n strong--> 3")
password = ""

k = {1 : 'simple',
     2 : 'middle',
     3 : 'strong'}


lvl = k.get(int(input("How strong do you want ? > ")), "invalid")
length = int(input("Length of the password ? > "))


n_list = "abcdefghijklmnopqrstuvwxyz01234567890"
all_chars = string.digits + string.ascii_letters + string.punctuation


if lvl == "simple" :
    password = "".join(random.sample(n_list, length))
    print("Your password is : ", password)
elif lvl == "middle":
    n_list = n_list + string.ascii_uppercase
    for i in range(length):
        password = "".join(random.sample(n_list, length))
    print("Your password is : ", password)
else:
    for i in range(length):
        password += "".join(random.choice(all_chars))
    print("Your password is : ", password)