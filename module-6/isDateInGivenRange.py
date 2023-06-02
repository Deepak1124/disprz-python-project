# Create a python function to check if date is in given range


import datetime

def is_date_in_range(date, start_date, end_date):
    if start_date <= date <= end_date:
        return True
    else:
        return False


date=datetime.date(2023, 5, 31)
start_date=datetime.date(2023, 5, 1)
end_date=datetime.date(2023, 6, 30)

print(is_date_in_range(date, start_date, end_date))