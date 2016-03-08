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

#create a palindrome recognition function
def find_palin(s, t):

	#going to use a df approach again, stealing code from yet another problem (hamming.py, this folder)
	#convert strings to lists, cleaning up on the way
	s_el = list(s.strip())
	t_el = list(t.strip())

	#Put my lists into a df:
	import pandas as pd

	pal_df = pd.DataFrame({'Original' : s_el,
 				'Complement' : t_el,
  				})
	
	#create new fxn, for detecting the sructure of a palindrome, constraints on palindrome being 4-12bp. The seeker will function at each position between the 2nd and 2nd last positions, seeking outwards from the positions between two palindromic pairs for a max of 6 steps, provided a minimum of two is met (ie. a max palindromic size of 12). Ideally want to do this taking note of locations, and attaching them to their respective lengths. Not part of this problem, but I also want to create a list of restriction sequences on the way, and count their occurances, which might be useful in other ways
	def seeker(rows):
		pass
		#this is gonna get crazy

		#start a counter
		i = 0
		for i in len(pal_df.index.tolist()):
			
		
		
#determin

	print(pal_df)

	














	

seq = fa_load()
comp_seq = complement(seq)
find_palin(seq, comp_seq)





































