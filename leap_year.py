import calendar as cl
def is_leap_year(year = None):
    if cl.isleap(year):
        return("Is a Leap Year")
    
    else:

        return("Is not a Leap Year")
    

for x in range(2021):
    year = is_leap_year(x)

print("%s %s" % (x, year))
