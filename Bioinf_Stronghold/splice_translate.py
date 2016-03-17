# This script identifies introns and exons in a given sequence, "splices" out the exons and tranlates the resulting transcript as part of the Rosalind Bioinformatics Stronghold problem set

#first import the data
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

#steal a function form another problem "Find Motif" in the same problem set (in this folder) and modify it as an intron locator
def find_introns(s, kwargs**):
	#get the input sequence
	s = s.strip()

	#get the intron list
	introns = []
	for arg in kwargs:
		introns.append(arg)
		

	#Quickest and most obvious solution is to use regex
	import regex as re

	#Create regex
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

# steal a function from a previous problem set (complement.py, in this folder) and modify it to convert DNA template to its complementary (coding) strand
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

#steal another script to transcribe the complimentary DNA to RNA

def transcribe():
	#get string
	t = input("Please input DNA to be transcribed: ")

	t_trans = t.replace("T","U")
	
	return t_trans

	
print(transcribe())


