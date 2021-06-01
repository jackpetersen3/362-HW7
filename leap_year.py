def leap_year(year):
    if  year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                #print(year, "is a leap year\n")
                return "yes"
            else:
                #print(year, "is not a leap year\n")
                return "no"
        else:
            #print(year, "is a leap year\n")
            return "yes"