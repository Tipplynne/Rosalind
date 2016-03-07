#this function takes user inputted string and values and returns two concatenated sliced strings according to four inputted integers

def IRFun():
	#user inputs info
	s = input("\nI can haz string :")
	lst = input("\nI can haz list of integers :\n")
	
	#do all the things with the info
	new_ls = lst.split(" ")
	print(new_ls)
	i = 0
	intlst = []
	for i in new_ls:
		intlst.append(int(i))
		
	print(intlst)
	intlst = sorted(intlst)
	outstring = s[intlst[0]:intlst[1]+1]+' '+s[intlst[2]:intlst[3]+1]
	return outstring

print(IRFun())
