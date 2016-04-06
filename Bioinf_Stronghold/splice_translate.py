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
	seq.remove('')
	seq.remove(seq[0])
	s = ''.join(seq)

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

#create a function to splice out introns
def excise_introns(dna, intronlist):

	processed = dna
	#loop throught the intron positions list
	for site in intronlist:
		processed = processed.replace(site, '')
		
	#return processed dna
	return processed

proc_dna = excise_introns(dna, intronlist)

#now transcribe dna to rna
def transcribe(proc_dna):
	#get string
	t = proc_dna
	t_trans = t.replace("T","U")
	
	return t_trans
	
transcript = transcribe(proc_dna)

#now steal pretty much all the translation.py code from the translation problem
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

#scan the rna for the start codon
i=0
while i < len(transcript):
	poss_codon = transcript[0+i:3+i]
	if aa_find(poss_codon) == "M":
		start = i
		break
	else:
		i += 1

#translate the open reading frame	
prot = ''
i=0
while i < len(transcript):
	orf_codon = transcript[0+i+start:3+i+start]
	aa = aa_find(orf_codon)
	if aa == "Stop": 
		break
	else:
		prot = prot+aa
		i += 3
		
print(prot[0])






































