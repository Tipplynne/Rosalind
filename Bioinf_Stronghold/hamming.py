# This script calculates the Hamming Distance, or number of point mutations, between two DNA sequences, s and t: dH(s,t) 

def hamming():
	#get the input sequences
	s = input("\nPlease enter first DNA sequence: ")
	t = input("\nPlease enter second DNA sequence: ")

	#convert strings to lists, cleaning up on the way
	s_el = list(s.strip())
	t_el = list(t.strip())

	#I could loop through both the lists' elements and count mismatches but I'm trying to teach myself to think of sequences in terms of positions, and alignments in terms of matrices. Also trying to learn how to use dataframes:

	#Put my lists into a df:
	import pandas as pd

	ham_df = pd.DataFrame({'SeqS' : s_el,
 				'SeqT' : t_el,
  				})

	#create a third column with mismatch data, by creating a function to calculate
	def match(row):        								
		pos_s = row[0]
		pos_t = row[1]           							
	
		if pos_s == pos_t:
			return 0
		else:
			return 1
	
	ham_df["Match"] = [match(row) for row in ham_df.itertuples(False)]

	#get the sum of mismatches
	dH = ham_df.Match.sum()
	
	#Playing around with fancy string formatting, which was just for fun and not practical
	return "\nThe Hamming Distance between the first and second sequence is {hamming}.\n".format(hamming = dH) 

print(hamming())
