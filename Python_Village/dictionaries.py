#this is a function to solve the dictionaries problem on Rosalind-Python set

def wordcnt():
	#get string chop into words
	s = input("Please input string of interest: ")
	lst = s.split(" ")
	setlst = set(lst)
	print(lst, "\n", setlst, "\n")
	
	#open dictionary
	diction = {}
	c = 0
	for i in setlst:
		for j in lst:
			if i == j:
				c += 1
				diction[i] = c
		c = 0	
	print(diction, "\n")
	for i in diction:
		print(i+" "+str(diction[i]))
wordcnt()
	
