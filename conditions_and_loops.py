#this is a function to calculate the sum of all odd numbers between two integers a and b

def oddthomas():
	#get the integers a and b and process from user inputted string
	lst = input("\nI can haz 2 of integers :\n")
	new_ls = lst.split(" ")
	a = int(new_ls[0])
	b = int(new_ls[1])

	#initialise the sum of the odds and counter
	summation = 0
	i = a
	
	#time-consuming step
	while i <= 10000 and i <= b:
		#print(i)
		if i%2 == True:
			summation = summation+i
			#print(summation)
		i += 1

	return summation

print(oddthomas())
