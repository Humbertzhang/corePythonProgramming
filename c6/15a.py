date1 = raw_input("Month1(MM)/Day1(DD)/Year1(YYYY):")
date2 = raw_input("Month2(MM)/Day2(DD)/Year2(YYYY):")
month1,day1,year1= date1.split('/')
month2,day2,year2= date2.split('/')
month1,day1,year1,month2,day2,year2 = int (month1),int (day1),int (year1),int(month2),int (day2),int(year2)

difyear,difmonth,difday = 0,0,0
if (year1 != year2):
    difyear = abs(year1 - year2)
if (month1 != month2):
    difmonth = abs(month1 - month2)
if (day1 != day2):
    difday = abs(day1 - day2)

difdayTotal = 365 * difyear + 30 * difmonth + difday

print "The days between those two date is",
print difdayTotal


