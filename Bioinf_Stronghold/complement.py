#this is a function to solve the DNA reverse complement problem on Rosalind, in the "Bioinformatics Stronghold" set

def rev_complement():
	#get string 
	s = input("Please input DNA to get reverse complement: ")
	#first reverse
	rev_s = s.strip()[::-1]
	
	#the following did not work, because the whole string could be replaced twice -blush
	#s_complement = s.replace("T","A").replace("A", "T").replace("C","G").replace("G","C")

	#instead, split string into elements and loop through, replacing elements conditionally
	letters = list(rev_s)
	complist = []
	for i in letters:
		if i == "T":
			complist.append(i.replace(i, "A"))
		elif i == "A":
			complist.append(i.replace(i, "T"))
		elif i == "C":
			complist.append(i.replace(i, "G"))
		elif i == "G":
			complist.append(i.replace(i, "C"))

	#join elements of complist to get reversed complement
	rev_s_complement = ''.join(complist)
	return rev_s_complement
	
	
print(rev_complement())
