# This script identifies introns and exons in a given sequence, "splices" out the exons and tranlates the resulting transcript into a protein string as part of the Rosalind Bioinformatics Stronghold problem "SPLC"

#first import the data
def fa_load():
	#get string from file
	f = input("Please input fasta file with sequence/s of interest: ")

	#open file, read contents
	start = open(f, "r")
	newfile = start.read()
	
	#split file into seq entries
	stringlist = []
	seqno = newfile.count(">")
	stringlist = newfile.split(">")
	stringlist.remove('')
			
	#get the DNA string
	seq = stringlist[0].split("\n")
	s = seq[1]
	
	#get motifs
	i = 1
	motlist = []
	while i < len(stringlist):
		motif = stringlist[i].split("\n")
		motlist.append(motif[1])
		i += 1

	#funtion output (tuple)
	return s, motlist

dna, intronlist = fa_load()

#steal a function form another problem "Find Motif" in the same problem set (in this folder) and modify it as an intron locator
def find_introns(s, intronlist):
	
	#Quickest and most obvious solution is to use regex
	import regex as re
	
	#getting the start and stop positions of the introns
	pos_list = []
	for intron in intronlist:

		#Create regex
		mox = re.compile(intron, re.I)
	
		#create an iterator
		matches = mox.finditer(s, overlapped=True) #overlapped funtionality only available for findall() and finditer() in most recent regex package
	
		#iterate
		for match in matches:
			pos_list.append([match.start()+1, match.end()+1])
	
	#output of fxn
	return pos_list
		

	
print(find_introns(dna, intronlist))









