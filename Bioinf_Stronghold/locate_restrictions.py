#this is a script to solve the find restction sites problem on Rosalind, in the "Bioinformatics Stronghold" set

#create a file loading function
def fa_load():
	#get string from file
	f = input("Please input fasta file with sequence/s of interest: ")

	#open file, read contents
	start = open(f, "r")
	newfile = start.read()
	
	#create contingency for multiple sequences (preempting this in future problems)
	stringlist = []
	seqno = newfile.count(">")
	if seqno > 1:
		stringlist = newfile.split("\n\n")	#split file into seq entries
	else:
		stringlist = []
		stringlist.append(newfile)

	#But, for this problem, we are assuming only 1 seq:
	seq = stringlist[0].split("\n")
	s = seq[1]
	return s

# steal a function from a previous problem set (complement.py, in this folder) and modify
def complement(s):
	
	#split string into elements and loop through, replacing elements conditionally
	letters = list(s.strip())
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

	#join elements of complist to get complement
	s_complement = ''.join(complist)
	return s_complement

	#create new fxn, for detecting the sructure of a palindrome, constraints on palindrome being 4-12bp. The seeker will function at each position between the 2nd and 2nd last positions, seeking outwards from the positions between two palindromic pairs for a max of 6 steps, provided a minimum of two is met (ie. a max palindromic size of 12). Ideally want to do this taking note of locations, and attaching them to their respective lengths. Not part of this problem, but I also want to create a list of restriction sequences on the way, and count their occurances, which might be useful in other ways

def seeker(s,c):
	length = 0
	l = []
	restr = ''
#start a counter
	i = 0
	#print(s.tolist())
	for i in range(len(s)):	#for each base in sequence
		print("i="+str(i))	
		j = 11		#reset j (i.e. start new palindrome search)
		next = 0	#next counter tracks size & position of each pal base
		restr = ''
		#for each of (start w/ max 12) bases upstream
		while j >= 0:
			
			#if we run out of string
			if j+i >= len(s):
				print("if happened")
				j += -1
				

			#if we have a furthermost match
			elif s[i+next] == c[i+j]:	
				print("elif1 happened")
				length = length+1
				print(length)
				restr = restr + s[i+next]
				print(restr)
				next += 1	
				#print("next="+str(next))
				j += -1
				#print("j="+str(j)+" pos "+c[i+j])
				
				if j == -1 and len(restr) > 3:
					print("miracle happened")
					l.append((restr, i+1, length))
					length = 0
				
					break
			

			#if we have a pal with a false start
			elif s[i+next] != c[i+j] and length > 0: #likely bug here - fixed?

				print("elif3 happened")
				length = 0
				print(length)
				next = 0
				restr = ''
				j += -1
				#print("j="+str(j)+" pos "+c[i+j])
				
			
			#if not a furthermost match, move to next furthest
			else:

				print("else happened")
				j += -1
				#print("j="+str(j)+" pos "+c[i+j])
	#check
	print(l)	
	


seq = fa_load()
comp = complement(seq)
result = seeker(seq, comp)




















