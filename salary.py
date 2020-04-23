income=int(input("Enter Basic Salary : "))
sal=income
if income>=1000 and income<100:
         sal+=0.3*income
elif income>20000:
             sal+=.2*basic
elif income>10000:
             sal+=.1*basic

print("Total Salary = ",sal)
