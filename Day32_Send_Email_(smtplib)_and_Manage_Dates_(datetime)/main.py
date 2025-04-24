# import smtplib

# my_email = "adygcsfg66tyyvv@tempmail.us.com"
# password = "ajeuwkdmtgbunspl4wqufii4tllby0"

# with smtplib.SMTP("mail.tempmail.us.com") as connection:
#     connection.starttls()

#     connection.login(user=my_email,password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="6j1wyhzzwsnsfee@tempmail.us.com",
#                         msg="Subject:hello\n\nThis is message body")

import datetime as dt

now = dt.datetime.now()
print (now)
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth =dt.datetime(year=1995, month=12,day=15,hour=4)
print(date_of_birth)
