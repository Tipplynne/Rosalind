# this is my approach to solving Rosalind's Textbook track problem BA1C

#first import the data
def pattern_load():
 #get string from file
 f = input("Please input file with sequence of interest: ")

 #open file, read contents
 start = open(f, "r")
 newfile = start.read()
	
 #split file into seq entries
 stringlist = []
 seqno = newfile.count("\n")
 stringlist = newfile.split("\n")
 stringlist.remove('')
			
 return stringlist[0]

#reverse complement function using python's string maketrans function, which maps elements of two strings to each other (a table), then uses translate to return mappings on a new string
def rev_complement(text):
 #iterating through each letter of the dna, going backwards (hence -1)
 revc = text[::-1].translate(str.maketrans('ACGT','TGCA'))
 return revc 

#run functions	
dna = pattern_load()
print(rev_complement(dna))

