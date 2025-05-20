import datetime
now = datetime.datetime.now()
bday=datetime.datetime(2005,4,15,9,41,00)
bday_date=bday.date()
print(now)
print(bday)
print(bday_date)

bday_weekday=bday.isoweekday()
print(bday_weekday)

weekday_list=["월","화","수","목","금","토","일"]
print(weekday_list[bday_weekday])