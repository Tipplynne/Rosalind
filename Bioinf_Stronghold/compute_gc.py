'''Rosalind problem Bioinfomatics Stronghold set; solution for compute GC content'''

#first import the data
def fa_load():
	#get strings from file
	f = input("Please input fasta file with sequence/s of interest: ")

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

data = fa_load()

#now write a function to calculate gc content and store that to new dictionary
def calc_gc(data):

	gc_dict = {}	
	for key in data:

		#count residues and calc GC content
		tot = len(data[key])
		GnC = data[key].count("G") + data[key].count("C")
		gc = GnC/tot*100
		ID = key
		gc_dict[ID] = gc

	return gc_dict

gc_dict = calc_gc(data)

#new function to calculate the sequence with the highest GC content

def utmost_gc(gc_dict):

	#from this soln on stack: http://stackoverflow.com/a/12343826/5722099
	v=list(gc_dict.values())
	k=list(gc_dict.keys())
	winner = k[v.index(max(v))]
	print(winner)
	print(round(gc_dict[winner],6))

utmost_gc(gc_dict)















