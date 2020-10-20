import random
x = random.sample(range(0, 30), 8)
y = random.sample(range(0, 30), 10)
result_pri = [i for i in x if i in y]
final_result = []
for i in result_pri:
    if i in result_pri and i not in final_result :
        final_result.append(i)
print(final_result)