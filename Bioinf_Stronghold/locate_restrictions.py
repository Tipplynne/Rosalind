#this is a script to solve the find restction sites problem on Rosalind, in the "Bioinformatics Stronghold" set

# first, steal a function from a previous problem set (compliment.py, in this folder) and modify
def rev_complement():
	#get string from file
	s = input("Please input DNA to get reverse complement: ")
	#first reverse
	rev_s = s.strip()[::-1]
	
	#split string into elements and loop through, replacing elements conditionally
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
