text_file = open("data.txt", "r")
lines = text_file.read().split('\n')

action		= 0
value		= 1
horizontal	= 0
vertical	= 0
aim 		= 0

for i in range(len(lines)):
	print("{}".format(lines[i]))
	line = lines[i].split()
	print("action: {}, value: {}".format(line[0], line[1]))
	if (line[action] == "down"):
		aim += int(line[value])
	elif (line[action] == "up"):
		aim -= int(line[value])
	elif (line[action] == "forward"):
		horizontal += int(line[value])
		vertical += aim * int(line[value])
	print("H: {}, V:{}".format(horizontal, vertical))

print("Result: {}".format(horizontal * vertical))
