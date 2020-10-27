counter = {}

with open('........\\text.txt', 'r') as f:
    line = f.readline()
    while line :
        line = line.strip()
        if line in counter:
            counter[line] += 1
        else:
            counter[line] = 1
        
        line = f.readline()

for pair in counter.items():
    print(pair)