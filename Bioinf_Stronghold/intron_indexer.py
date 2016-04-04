#steal a function form another problem "Find Motif" in the same problem set (in this folder) and modify it as an intron locator

#this was unecessary code written for the RNA splicing problem, and removed from that script
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
		
intron_index = find_introns(dna, intronlist)




