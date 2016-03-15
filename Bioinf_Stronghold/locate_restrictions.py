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
		j = 1		#reset j (i.e. start new palindrome search), tracks bps right
		next = 0	#next tracks position of leftside pal bp from midpoint
		restr = ''	#creates pal sequence
		
		#for each of (start w/ max 6) bases up- and down-stream
		while j < 7:
			
			#if we run out of string to the right or left
			if j+i >= len(s) or i+next < 0:

				length = 0
				break

			#if we have a innermost match
			elif s[i+next] == c[i+j]:

				length = length+2
				restr = s[i+next:j+i+1]
				#print(restr)
				next += -1 	#track bp to the right
				j += 1		#track bp to the left
			
				#if we get to outermost match and 4 <= pal length <= 12
				if len(restr) > 3:

					#imutable tupleness
					l.append((restr, i+2-int((length)/2), length))

			#if not a match
			elif s[i+next] != c[i+j]:	

				length = 0
				break

	#output
	return l	

seq = fa_load()
comp = complement(seq)
result = seeker(seq, comp)

#get the result in desired Rosalind format
for i in result:
	print(str(i[1])+' '+str(i[2]))


















