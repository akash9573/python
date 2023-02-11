month = input("Enter month : ")
day = int(input("Enter no.of days: "))

if month in ('January','February','March'):
	season = 'winter'
elif month in ('April','May','June'):
	season = 'summer'
elif month in ('July','August','September'):
	season = 'spring'
else:
	season = 'autumn'

if (month == 'March') and (day > 19):
	season = 'summer'
elif (month == 'June') and (day > 20):
	season = 'spring'
elif (month == 'December') and (day > 20):
	season = 'winter'
print("Season is",season)
