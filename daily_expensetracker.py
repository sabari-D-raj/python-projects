import csv
from datetime import datetime
def expens_hold():
    amount=float(input("enter the amount ₹:"))
    category=input("enter the category: ")
    note=input("Enter the note(optional): ")
    date=datetime.now()  # it will get today date  in form of year-month-date
    with open('expense.csv', 'a', newline='') as file:#with open will open the file in append mode close it after writing
        writer = csv.writer(file)
        writer.writerow([amount,category,note,date])#it will write the data in csv format and write the data in new line(rows)
def month_expens():
    month=input("enter the month in format YYYY-MM: ")
    file=open('expense.csv', 'r') #open the file in read mode
    total_expense = 0
    for row in file:     # read the file line by line i=rows
        row = row.strip().split(',') # split the row by comma
        date_object = datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S.%f') # convert the date string to datetime object
        if date_object.strftime('%Y-%m') == month:
            amount = float(row[0])
            total_expense += amount
    file.close()  # close the file
    print(f"Total expense for {month} is ₹{total_expense:.2f}")  # print the total expense for the month
def yearly_expens():
    year=input("enter the year in format YYYY: ")
    file=open('expense.csv','r')
    total_expense = 0
    for row in file:
        row=row.strip().split(',')
        date_object = datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S.%f')
        if date_object.strftime('%Y')==year:
            amount = float(row[0])
            total_expense += amount
    file.close()
    print(f"Total expense for {year} is ₹{total_expense:.2f}") 
while True:
    print("1:add expense")
    print("2:show monthly expense")
    print("3:yearly expense")
    print("4:exit")
    choice=input("enter your choice: ")
    if(choice=="1"):
        expens_hold()
    elif(choice=="2"):
        month_expens()
    elif(choice=="3"):
        yearly_expens()
    elif(choice=="4"):
        print("bye.....bye")
        break
    else:
        print("invalid choice, please try again")