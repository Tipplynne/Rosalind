""" This is a basic script to try and infer mRNA from a protein string, based on the Rosalind problem, in the Bioinformatics Stronghold set"""

#first define a function for input
def fa_load():
 	#get protein string from fasta file
  	f = input("Please enter file name of interest: ")

  	#open file, read contents
	start = open(f, "r")
	newfile = start.read()

	#split file into seq entries
	stringlist = []
	seqno = newfile.count(">")
	stringlist = newfile.split(">")
	stringlist.remove('')

	#open up a dictionary and save sequences and ID keys
	seqs = {}
	for entry in stringlist:

		#to get key
		seq = entry.split("\n")
		seq.remove('')
		key = seq[0]
			
		#get the DNA string
		seq.remove(seq[0])
		s = ''.join(seq)

		#add key:string pair to dictionary
		seqs[key] = s
		
	return seqs

#Steal some code from an earlier problem (translation), which created a codon to aa look-up. Modify the code to provide and aa to codon look up
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
def codon_find(aa):
	return tRNA_df['codon'][tRNA_df['aa'] == aa].values









































