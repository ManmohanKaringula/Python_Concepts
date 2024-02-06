import datetime

# to print current date
print(datetime.date.today())

# To print current date:
print(datetime.datetime.now().strftime("%H:%M:%S"))

# Note: To change the format for displaying the date and time like "mm,dd,yy" to "dd,mm,yy" we use small characters 
# (%d) in strftime() function and use (%A, %B) for dat and month in textual format in strftime() function.

#------>>>***********IMPORTANT*************<<<-----------
print(datetime.datetime.now().strftime("%A, %B, %d, %m, %Y, %T")) # This is very important for project purpose 
print(datetime.datetime.now())
