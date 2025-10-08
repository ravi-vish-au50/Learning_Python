# Library : 
            # A set of data code that can 

# Datetime library is used for date time series analysis date time contains 4 major modules
    
    # * Date
    # * Time
    # * Datetime
    # * Timedate

# Funtions 

# import datetime 

# x = datetime.date(2010, 8, 24)

# print(x)

# x.year
# x.month
# x.day
# print(x.year)
# print(x.month) 
# print(x.day)
# x.replace(2020, 10, 25)
# print(x)
# x.weekday()
# print(x.weekday()) # 0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday, 4 = Friday, 5 = Saturday, 6 = Sunday
# x.isoweekday()
# print(x.isoweekday()) # 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, 7 = Sunday

# today = datetime.date.today()
# print(today)
# be used by importing it into your program



# Attribute : date modules have year, month & day as Attribute

# formatting date
# x = datetime.date(2010, 8, 24)
# print(x)
# %a = Abbreviated weekday name
# %A = Full weekday name
# %b = Abbreviated month name
# %B = Full month name
# %c = Local version of date & time
# %d = Day of the month (01 to 31)
# %j = Day of the year (001 to 366)
# %m = Month of the year (01 to 12)
# %U = Week number of the year (Sunday as the first day of the week) (00 to 53)
# %W = Week number of the year (Monday as the first day of the week) (00 to 53)
# %x = Local version of date
# %y = Year without century (00 to 99)

# x.strftime("%a") # Abbreviated weekday name
# print(x.strftime("%a"))
# (x.strftime("%A")) # Full weekday name
# print(x.strftime("%A"))
# (x.strftime("%b")) # Abbreviated month name
# print(x.strftime("%b")) 
# (x.strftime("%B")) # Full month name
# print(x.strftime("%B"))
# (x.strftime("%c")) # Local version of date & time
# print(x.strftime("%c"))
# (x.strftime("%d")) # Day of the month (01 to 31)

# Time module :
             # is used to work with time independent of any particular day and

# from datetime import time
# x = time(10, 30, 45)
# print(x)

# y = time(5, 15, 30 , 500)
# print(y)
# print(y.hour)
# print(y.minute)
# print(y.second)
# print(y.microsecond)
# x.strftime("%H") # Hour (00 to 23)
# print(x.strftime("%H"))
# print(x.strftime("%I")) # Hour (01 to 12)
# print(x.strftime("%I"))
# print(x.strftime("%M")) # Minute (00 to 59)
# print(x.strftime("%M"))
# print(x.strftime("%S")) # Second (00 to 59)

# Datetime module :
             # is used to work with both date & time

# from datetime import datetime
# x = datetime(2020, 5, 17, 10, 30, 45)
# print(x)

# print(x.year)
# print(x.month)
# print(x.day)
# print(x.hour)
# print(x.minute)
# print(x.second)
# print(x.microsecond)
# print(x.strftime("%c")) # Local version of date & time
# print(x.strftime("%x")) # Local version of date
# print(x.strftime("%X")) # Local version of time
# print(x.strftime("%Y")) # Year with century
# print(x.strftime("%y")) # Year without century (00 to 99)
# print(x.strftime("%a")) # Abbreviated weekday name
# print(x.strftime("%A")) # Full weekday name
# print(x.strftime("%b")) # Abbreviated month name

# # timedalta module :
#                 # is used to work with the difference between two dates or times

# from datetime import datetime, timedelta  # importing datetime and timedelta classes from datetime module
# x = datetime(2020, 5, 17, 10, 30, 45)    # creating a datetime object
# print(x)
# y = x + timedelta(days=5, hours=2, minutes=30) # adding 5 days, 2 hours and 30 minutes to the datetime object
# print(y) 
# z = x - timedelta(days=10, hours=5, minutes=15)  # subtracting 10 days, 5 hours and 15 minutes from the datetime object
# print(z)    
# a = timedelta(days=5, hours=2, minutes=30) # creating a timedelta object
# print(a)
# b = timedelta(days=10, hours=5, minutes=15) # creating another timedelta object
# print(b) 
# c = a + b # adding two timedelta objects
# print(c)
# d = b - a
# print(d)
# e = a.total_seconds()
# print(e)
# f = b.total_seconds()
# print(f)
# g = c.total_seconds()   

# Datedelta Module :
             # is used to work with the difference between two dates or times

# from datetime import date, timedelta
# x = date(2020, 5, 17)
# print(x)
# y = x + timedelta(days=5) # adding 5 days to the date object
# print(y)
# z = x - timedelta(days=10) # subtracting 10 days from the date object
# print(z)

# Timelibrary :
         # is used to work with time in seconds

# import time
# x = time.time() # returns the current time in seconds since the epoch
# print(x)
# y = time.ctime() # returns the current time in a human-readable format
# print(y)
# z = time.localtime() # returns the current time in a struct_time format
# print(z)
# print(z.tm_year) # returns the year
# print(z.tm_mon) # returns the month
# print(z.tm_mday) # returns the day
# print(z.tm_hour) # returns the hour
# print(z.tm_min) # returns the minute
# print(z.tm_sec) # returns the second
# print(z.tm_wday) # returns the weekday (0 = Monday, 6 = Sunday


# File operations Sets :
                        # is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
a = {1,2,3}  # a = {1,2,3,4,5}
b = {3,4,5}  # b = {3,4,5,6,7}
c = a & b  #  c = {3} 
c = a.intersection(b) #  c = {3}
c
d = b & a # d = {3}
d = b.intersection(a) # d = {3}
d
print(c)
print(d)
# union
a = {1,2,3}  # a = {1,2,3,4,5}
b = {4,5,6}  # b = {3,4,5,6,7}
c = a | b  #  c = {1,2,3,4,5,6}       
c = a.union(b) #  c = {1,2,3,4,5,6}
c
d = b | a # d = {1,2,3,4,5,6}
d = b.union(a) # d = {1,2,3,4,
d = b.union(a) # d = {1,2,3,4,5,6}6}
d
d
print(c)
print(d)