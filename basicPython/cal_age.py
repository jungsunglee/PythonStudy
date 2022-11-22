#calculate the age using birth year.
import datetime as dt
birth_year = int(input("Please input your birth year : "))
age = int(dt.date.today().strftime("%Y")) - birth_year
print("현재 나이는 {}세 입니다.".format(age+1))