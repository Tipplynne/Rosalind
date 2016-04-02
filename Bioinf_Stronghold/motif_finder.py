# This script calculates the number of occurances of a simple motif in a given sequence as part of the Rosalind Bioinformatics stronghold set

def find_motif():
	#get the input sequences
	s = input("\nPlease enter the DNA sequence to be analysed: ").strip()
	m = input("\nPlease enter the motif to be searched for: ").strip()

	#Quickest and most obvious solution is to use regex
	import regex as re

	#Create regex -shit what does the re.I package do again?
	mox = re.compile(m, re.I)
	
	#create an iterator
	matches = mox.finditer(s, overlapped=True) #overlapped funtionality only available for findall() and finditer() in most recent regex package
	
	#iterate
	pos_list = []
	for match in matches:
		pos_list.append(match.start()+1)
	
	#output in desired format
	for i in pos_list:
		print(i, end=' ')

	#additional functionality not requested in the original problem, view results in sequence
	print("\n\n" + mox.sub(m, s.lower()))#not perfect as does not allow overlapping

	#try with string formatting:

	
find_motif()
