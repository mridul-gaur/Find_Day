start_date = "01.01.0001" #Saturday
date = "02.01.0001"

days = {
    1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday",
    6:"Saturday", 7:"Sunday"
}

months = {
    1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31
}

def diff(date):
    day = int(date[:2])
    month = int(date[3:5])
    year = int(date[6:])
    d = 1 + day
    m = 1 + month
    y = 1 + year
    return d,m,y


