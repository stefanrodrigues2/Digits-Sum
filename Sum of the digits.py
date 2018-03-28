def exp(n):
	number = 2 ** n
	print ("Number is: %d" % number)
	sum = 0
	while(number>0):
		mode = number%10
		sum = sum + mode
		number = number/10
	print "Sum of the digits is: %d" % sum

	
n= int(input("Enter number:"))
exp(n)
