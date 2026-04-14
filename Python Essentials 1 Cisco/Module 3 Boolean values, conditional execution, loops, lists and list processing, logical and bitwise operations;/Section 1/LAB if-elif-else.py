'''
if the year number isn't divisible by four, it's a common year;
otherwise, if the year number isn't divisible by 100, it's a leap year;
otherwise, if the year number isn't divisible by 400, it's a common year;
otherwise, it's a leap year.
The code should output one of two possible messages, which are Leap year or Common year, depending on the value entered.
'''
year = int(input("Enter a year: "))

if year < 1582:
	print("Not within the Gregorian calendar period")
else:
    #  Write the if-elif-elif-else block here.
	if year % 4 != 0:
		print("Common Year")
	elif  year % 100 != 0:
		print("Leap year")
	elif year % 400 != 0:
		print("Common year")
	else:
		print("Leap year")
	