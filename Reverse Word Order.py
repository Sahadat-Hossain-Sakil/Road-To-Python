text = str(input('Enter a long string with some word : '))
txt_list = text.split(" ")
for i in range(1, len(txt_list)+1):
	print(txt_list[-i], end = ' ')