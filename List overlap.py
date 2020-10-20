list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
new_list = []
for i in list_1 :
     if i in list_2 and i not in new_list :
         new_list.append(i)
print(new_list)
