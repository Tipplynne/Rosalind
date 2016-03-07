
ask = input("please enter file name :\n")


f=open(ask, "r")

p=open("evenlines.txt", "w")

num_lines = sum(1 for line in f)
f.seek(0)
print(num_lines)

liner = 1

while liner <= num_lines:
	print(liner%2)
	if liner%2 == 0:
		p.write(f.readline())
	else:
		f.readline()
	liner += 1
	

f.close()
p.close()


