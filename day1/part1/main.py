text_file = open("data.txt", "r")
lines = text_file.read().split('\n')
increased = 0

for i in range(len(lines)):
	if (i > 0):
		if (int(lines[i]) > int(lines[i - 1])):
			increased += 1

print("increased: {}".format(increased))
