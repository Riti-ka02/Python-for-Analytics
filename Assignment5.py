#ASSIGNMENT ON SALARY SLIP 
name=input("enter the EMPLOYEE NAME:")
salary=float(input("enter the BAISC SALARY:"))
bonus=int(input("enter the  BONUS :"))
tax_percentage=float(input("enter the TAX PERCENTAGE:"))

gross_salary = salary*bonus
tax_amount = gross_salary*tax_percentage/100
net=gross_salary-tax_amount
print("SALARY SALIP AMOUT IS ",net)

          
