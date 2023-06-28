start_date = "01.01.0001" #Saturday
date = "02.01.0001"

days = {
    1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday",
    6:"Saturday", 0:"Sunday"
}

months = {
    1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31
}

def diff(date):
    day = int(date[:2])
    month = int(date[3:5])
    year = int(date[6:])
    d = day
    m = month
    y = year
    return d,m,y

#date = ["01.01.0001","02.01.0001","01.02.0001","01.01.0002"]

#for i in date:
    #d,m,y = diff(i)
    #print(d,m,y)

d,m,y = diff(date)

def assig(d):
    a = d%7 
    return a

#for i in range(1,32):
    #assig(i)
final = assig(d)


print("The day on",date,"is",days[final])
