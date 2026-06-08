gender=int(input("enter your gender(M/F)"))
age=int(input("enter your age:"))
hight=int(input("enter your hight"))

if gender="M" and age>=25 and age<=35 and hight>5:
       print("Eligible:")
elif gender="F" and age>=18 and age<=25 and hight>4:
       print("Eligible:")
else:
    print("not eligible")
