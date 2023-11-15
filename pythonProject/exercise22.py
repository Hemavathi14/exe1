
def year_month(Year,Month):
    leap_year=0
    if Year % 4 == 0:
        if Year % 100 == 0:
            if Year % 400 == 0:
                leap_year= Year
            else:
                Year = Year
        else:
            leap_year = Year
    else:
        Year = Year


    if month==1:
        return "31"
    elif month==2:
        if year==leap_year:
            return "29"
        else:
            return "28"
    elif month==3:
        return "31"
    elif month==4:
        return "30"
    elif month==5:
        return "31"
    elif month==6:
        return "30"
    elif month==7:
        return "31"
    elif month==8:
        return "28"
    elif month==9:
        return "30"
    elif month==10:
        return "31"
    elif month==11:
        return "30"
    elif month==12:
        return "31"

year=int(input("Enter the year:"))
month=int(input("Enter the month:"))

days=year_month(Year=year,Month=month)
print(f"no of days in {month} is {days}")