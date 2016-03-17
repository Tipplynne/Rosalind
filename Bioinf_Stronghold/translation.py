# This script tranlates an RNA transcript to protein as part of the Rosalind Bioinformatics Stronghold problem set

#first we need to convert a codon table (tRNA.csv) into a structure. I like pandas dfs so:

import pandas as pd

#read in codon table
def csv_loader(filename):
	df = pd.read_csv(filename)           
	return df

raw_codons = csv_loader("tRNA.csv")

#create columns
raw_codons["U"] = [x.split()[0] for x in raw_codons["Codons"]]
raw_codons["Uaa"] = [x.split()[1] for x in raw_codons["Codons"]]
raw_codons["C"] = [x.split()[2] for x in raw_codons["Codons"]]
raw_codons["Caa"] = [x.split()[3] for x in raw_codons["Codons"]]
raw_codons["A"] = [x.split()[4] for x in raw_codons["Codons"]]
raw_codons["Aaa"] = [x.split()[5] for x in raw_codons["Codons"]]
raw_codons["G"] = [x.split()[6] for x in raw_codons["Codons"]]
raw_codons["Gaa"] = [x.split()[7] for x in raw_codons["Codons"]]

#drop raw data columns
codons = raw_codons.drop('Codons', axis =1)

#wide to long
codons.columns = ['codon', 'aa', 'codon', 'aa', 'codon', 'aa', 'codon', 'aa']
tRNA_df = codons[[0,1]].append(codons[[2,3]]).append(codons[[4,5]]).append(codons[[6,7]])

#new function is a codon-to-aa look-up
def aa_find(codon):
	return tRNA_df['aa'][tRNA_df['codon'] == codon].values

#get the input sequence, 
#Aside: today I learned about "segmentation faults (core dumped)" this is happens when you input way to much data at the terminal, like a 10kb RNA sequence! Rather read in a file!

def rna_load():
	#get string from file
	f = input("Please input fasta file with sequence/s of interest: ")

	#open file, read contents
	start = open(f, "r")
	newfile = start.read()
	seq = newfile.strip("\n")	
	return seq

s = rna_load()

#scan the rna for the start codon
i=0
while i < len(s):
	poss_codon = s[0+i:3+i]
	if aa_find(poss_codon) == "M":
		start = i
		break
	else:
		i += 1

#translate the open reading frame	
prot = ''
i=0
while i < len(s):
	orf_codon = s[0+i+start:3+i+start]
	aa = aa_find(orf_codon)
	if aa == "Stop":
		# the following helped me to figure out that I had a segmentation fault
		#print("I stopped at i = "+str(i)+" orf codon = "+orf_codon) 
		break
	else:
		prot = prot+aa
		i += 3
		
print(prot[0])

	






