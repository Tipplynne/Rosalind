#this is a function to solve the DNA transcript problem on Rosalind, the "Bioinformatics Stronghold" set

def transcribe():
	#get string
	t = input("Please input DNA to be transcribed: ")

	t_trans = t.replace("T","U")
	
	return t_trans
	
	
print(transcribe())
