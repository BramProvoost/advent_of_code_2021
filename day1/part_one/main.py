text_file = open("data.txt", "r")
lines = text_file.read().split('\n')
privious = 0
increased = 0

for i in range(len(lines)):
	current = int(lines[i])
	# print("{}, {}".format(current, privious))
	if current > privious and i > 0:
		increased += 1
		# print("{} > {}".format(current, privious))
	privious = current
	
print("increased: {}".format(increased))

# new

increased = 0
for i in range(len(lines)):
	if (i > 0):
		if (int(lines[i]) > int(lines[i - 1])):
			increased += 1

print("increased: {}".format(increased))
