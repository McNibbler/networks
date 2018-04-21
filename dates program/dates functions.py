#Python dates functions
#Networks 9/28/17

#imports datetime and relativedelta from
#dateutil (third party library)
import datetime
from dateutil.relativedelta import relativedelta

#finds today's date and relative dates
#of the next and previous months
currentDate = datetime.datetime.now()
previousMonth = currentDate - relativedelta(months = 1)
nextMonth = currentDate + relativedelta(months = 1)

#finds days until birthday
birthdayDate = datetime.datetime(2018, 1, 8)
changeInDate = (birthdayDate - currentDate).days + 1

#prints results
print("The current date and time is: ",
    currentDate.replace(microsecond = 0) , "\n")
print("The previous month's date and time is: ", 
    previousMonth.replace(microsecond = 0) , "\n")
print("The next month's date and time is: ",
    nextMonth.replace(microsecond = 0) , "\n")
print("There are ",
    changeInDate," days until your birthday!\n")