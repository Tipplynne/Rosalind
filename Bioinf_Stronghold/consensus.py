"""
This is a basic script to try and infer a consensus psequence and profile for several DNA sequences, based on the Rosalind problem CONS, in the Bioinformatics Stronghold set.

Am trying make my approaches to solving the rosalind problems more sophisticated and fast by using oop and more functions. So this code may seem overly complicated but the idea is to build chunks and tools that other solutions can call.
"""

import pandas as pd

#first define a sequence class 

class Sequence:
	SEQ = None
	IDY = None

	def toString(self):
		return self.SEQ+"\n"

	def __init__(self, seq, idy): 
		self.SEQ = seq
		self.IDY = idy
             		
slist = []
#now create a function to load fasta files, the example/test file is in the fasta file consensus_input.fa
def fasta_loader(FAST):

	start = open(FAST, "r")
	newfile = start.read()
	stringlist = []
	seqno = newfile.count(">")
	
	#split file into seq entries
	if seqno > 1:
		stringlist = newfile.split(">")	

	#in case of only a single entry
	else:
		stringlist = []
		stringlist.append(newfile)
	stringlist.remove('')
		
	#split entries into basic lines (assuming seq runs over several lines) and seq ID
	for k in range(len(stringlist)):
		stringlist[k] = stringlist[k].split("\n")		
	

	#remove seq ID's after saving them to a keylist
	keys = []
	for l in range(seqno):
		keys.append(stringlist[l][0])
		stringlist[l].remove(stringlist[l][0])
				
	#change to lower case for seqIDs, this makes regex and later searching easier
	keys2 = [change.lower() for change in keys]
	
	diction = {}
	
	#join baselines into a single sequence string minus \n formatting, whilst filling a dictionary
	
	for i in range(seqno):
		diction[keys2[i]] = ''.join(stringlist[i])		
	
	for key in diction:									
		print("Sequence %s loaded; %i Residues\n" %(key.upper(), int(len(diction[key]))))

	#moving newly loaded sequences to class "Sequence"
	for key in diction:
		seq = Sequence(diction[key],key)
		slist.append(seq)					

#make sequence matix using pandas dataframe
table = []

def na_matrix(ls_obj):

	#get individual residues from each sequence
	for each in ls_obj:
		table.append(list(each.SEQ))
	df = pd.DataFrame(table)

	#now create profile based on df using value_counts fxn
	profile = df.apply(pd.value_counts).fillna(0)
	print(profile)
	#get index value of the max value in each column of profile and send to cons list
	cons = []
	for pos in df.columns:
		cons.append(profile[pos].idxmax())

	#concatenate cons list into the consensus seq and add to Sequence class
	consensus = Sequence(''.join(cons),'Consensus')

	#print desired output
	print(consensus.SEQ)
	
	
"""
Essentially solved but need to work on output format (like printing output to file, including large profiles), also, alternate consensus sequences can exist. Can we find all possible alternate consensus seqs? look at shared solutions for the problem on Rosalind...?
"""


fasta_loader('rosalind_cons.txt')

na_matrix(slist)
