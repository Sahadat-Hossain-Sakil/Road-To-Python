user = input(" Give a shape of game board seperate by space (3 2) or (3 3) :> ")
x, y = user.split()
x = int(x)
y = int(y)
dot_line = " ..."
var_line = "|   "
def x_output(x):
	print(dot_line * x)

def y_output(x):
	print(var_line * (x+1))

for i in range(y):
	x_output(x)
	y_output(x)

x_output(x)