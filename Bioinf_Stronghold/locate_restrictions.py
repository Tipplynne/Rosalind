#this is a script to solve the "find restction sites" problem on Rosalind, in the "Bioinformatics Stronghold" set

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
		else:
			print("Warning! Non-standard base symbols in sequence!")

	#join elements of complist to get complement
	s_complement = ''.join(complist)
	return s_complement

	#create new fxn, for detecting the sructure of a palindrome, constraints on palindrome being 4-12bp. The seeker will function at each position between the 2nd and 2nd last positions, seeking outwards from the positions between two palindromic pairs for a max of 12 steps, provided a minimum of two is met (ie. a max palindromic size of 12). Ideally want to do this taking note of locations, and attaching them to their respective lengths. Not part of this problem, but I also want to create a list of restriction sequences on the way, and count their occurances, which might be useful in other ways

def seeker(s,c):
	length = 0
	l = []
	i = 0
	
	for i in range(len(s)):	#for each base in sequence	
		j = 11		#reset j (i.e. start new palindrome search) at max 12bp
		next = 0	#next counter tracks position of each pal bp from start
		restr = ''	#creates pal sequence

		#for each of (start w/ max 12) bases upstream
		while j >= 0:
			
			#if we run out of string
			if j+i >= len(s):
				j += -1

			#if we have a furthermost match
			elif s[i+next] == c[i+j]:	
				length = length+1
				restr = restr + s[i+next]
				next += 1	
				j += -1
				
				#if we get to innermost match and 4 <= pal length <= 12
				if j == -1 and len(restr) > 3:
					l.append((restr, i+1, length)) #imutable tupleness
					length = 0
					break

			#if we have a pal with a false start
			elif s[i+next] != c[i+j] and length > 0: 
				length = 0
				next = 0
				restr = ''
				j += -1
				
			#if not a furthermost match, move to next furthest
			else:
				j += -1
	#output
	return l	

seq = fa_load()
comp = complement(seq)
result = seeker(seq, comp)

#get the result in desired Rosalind format
for i in result:
	print(str(i[1])+' '+str(i[2]))


















