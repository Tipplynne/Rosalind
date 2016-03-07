#this is a function to solve the DNA problem on Rosalind, the "Bioinformatics Stronghold" set

def basecnt():
	#get string chop into words
	s = input("Please input string of interest: ")
	baselst = [s.count("A"),s.count("C"),s.count("G"),s.count("T")]
	
	print(baselst[0],baselst[1],baselst[2],baselst[3])
	
	

basecnt()
