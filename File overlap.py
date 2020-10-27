# In this code we will find some overlaped or common number from two different .txt files. 
# One is called Prime.txt with all prime numbers below 1000 and other is called Happy.txt
# with all happy numbers below 1000. 

with open('.......\\Prime.txt', 'r') as p:
    k = p.read().splitlines()
    with open('.......\\Happy.txt', 'r') as h:
        l = h.read().splitlines()
        for items in k:
            if items in l: 
                print(items) 