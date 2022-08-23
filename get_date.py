import datetime


current = datetime.datetime.now()
current = current.date()

current_splitted = str(current).split("-")

current_day = current_splitted[-1]

current_year = current_splitted[0]

current_month = current_splitted[1]

year = input("year\n")
day = input("day\n")
month = input("month\n")
print(current_day, current_month, current_year)

def checking_dates(y=year,d=day,m=month,cy=current_year,cm=current_month,cd=current_day):
    if int(y) >= int(cy) and int(m) > int(cm):
        print("sorry you have entered Future Date")
        if int(d) > int(cd):
            print("Future Dates")
    else:
        date_str = f"{y}-{m}-{d}"
    
        return date_str






    




 



