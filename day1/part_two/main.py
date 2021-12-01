text_file = open("data.txt", "r")
lines = text_file.read().split('\n')
privious_a = 0
privious_b = 0
privious_c = 0
increased = 0

for i in range(len(lines)):
	current = int(lines[i])
	# print("{}, {}, {}, {}".format(current, privious_c, privious_b, privious_a))
	if current + privious_c + privious_b > privious_c + privious_b + privious_a and i > 2:
		increased += 1
		# print("{} > {}".format(current + privious_c + privious_b, privious_c + privious_b + privious_a))
	privious_a = privious_b
	privious_b = privious_c
	privious_c = current
print("increased: {}".format(increased))

# new

increased = 0
for i in range(len(lines)):
	if (i > 2):
		if (int(lines[i]) > int(lines[i - 3])):
			increased += 1

print("increased: {}".format(increased))
