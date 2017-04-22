num = input("Please input a int number < 1000 and >0:")
list1 = ['zero','one','two','three','four','five','six','seven','eight','nine']


if (num>=1000) or (num<=0):
	print "Illeagl input"

else:
	if num >=100 and num <=999:
		bit1 = num/100
		num -= bit1*100
		print list1[bit1],"-",
	if num >=10 and num <=99:
		bit2 = num/10
		num -= bit2*10
		print list1[bit2],"-",
	print list1[num]

