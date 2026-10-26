# age = 19

# if age >= 18:
#     print("you can vote")
# else:
#     print("you can not vote")    


# age = 16

# if age >= 18:
#     print("you can vote")
# else:
#     print("you can not note")    


# age = int(input("enter the age="))

# if age >= 18:
#     print("you can vote")
# else:
#     print("you can not vote")    


# 1)Check if a number is positive or negative.

# num = int(input("enter the number:"))

# if num >= 0:
#     print("positive number")
# else:
#     print("negative number")      


# 2)Check if a person is eligible to vote (age ≥ 18).

# age = int(input("enter the your age:"))

# if age >= 18:
#     print("you can vote")
# else:
#     print("you can not vote")    

# 3)Check if a number is even or odd.

# num = int(input("enter the number:"))

# if num % 2 == 0:
#     print("even number")
# else:
#     print("odd number")    

# 4)Check if a student passed or failed (marks ≥ 35).

# passed = int(input("enter the marks:"))

# if passed > 35:
#     print("you can a pass")
# else:
#     print("you can not a pass")    

# 5)Check if a number is greater than 100 or not.

# greater = int(input("enter the number"))

# if greater > 100:
#     print("number is 100 than greater")
# else:
#     print("number is not a greater than")    


# 6) Check if a password is correct. (Example: "python123")

# password = input("enter the password:")

# if password == "python123":
#     print("login sucessfully")
# else:
#     print("login not sucessfully")    



# nested if statements

# age = int(input("enter the age"))
# permission = input("do have permission(yes/no)")

# if age >= 18:
#     if permission == "yes":
#         print("do have permision")
#     else:
#         print("You do not have permission.")    
# else:
#     print("do have no permission")        


# 1)User se age aur permission lo. Agar age 18+ aur permission "yes" ho to "Allowed" print karo.

# age = int(input("enter the age"))
# permission = input("do have permission(yes/no)")

# if age >= 18:
#     if permission == "yes":
#         print("do have permission")
#     else:
#         print("do have no permission") 
# else:
#     print("you under 18")

# 2)User se username aur password lo. Agar username "admin" ho aur password "1234" ho to "Login Successful" print karo.

# username = input("enter tha username:")
# password = int(input("enter the password:"))

# if username == "admin":
#     print("username are same")
    
#     if password == 1234:
#         print("login")
#     else:
#         print("not login")
# else:
#     print("username and password not a same")   
# 

# If, Elif, Else	Conditions lagana

# num = 10;

# if num > 0:
#     print("positive number")
# elif num < 0:
#     print("negative number")
# else:
#     print("zero")    

# age = 17

# if age > 18:
#     print("you can vote")
# else:
#     print("you can not vote")     


# Marks 90 ya usse zyada → Grade A
# Marks 80 ya usse zyada → Grade B
# Marks 70 ya usse zyada → Grade C
# Marks 60 ya usse zyada → Grade D
# Marks 60 se kam → Fail

# marks =int(input("enter tha number="))


# if marks >= 90:
#     print("grade a")
# elif marks >= 80:
#     print("grade b")
# elif marks >= 70:
#     print("grade c")
# elif marks >= 60:
#     print("grade d")
# else:
#     print("fail")           


# units = int(input("enter tha unites"))

# if units <= 100:
#     bill = units * 5
# elif units <= 200:
#     bill = units * 7
# else:
#     bill = units * 10

# print("total units bill", bill) 


# Next Question 6: Shopping Discount 🛒
# Ek shopping bill input lo.
# - Bill ₹5000 ya usse zyada → 20% discount
# - Bill ₹3000 ya usse zyada → 10% discount
# - Bill ₹1000 ya usse zyada → 5% discount
# - Bill ₹1000 se kam → No discount

# bill = int(input("enter tha amount="))

# if bill >= 5000:
#     discount = bill * 20 / 100
# elif bill >= 3000:
#     discount = bill * 10 / 100
# elif bill >= 1000:
#     discount = bill * 5 / 100
# else:
#     discount = 0

# finalbill = bill - discount

# print("shopping amount", bill)
# print("discount",discount)
# print("final bill",finalbill)           


# Question 7: Login System in Python
# Task: User se username aur password input lo.
# username = input("enter a username:")
# password = input("enter a password:")

# if username == "admin" and password == "1234":
#     print("login successful")
# elif password != "1234":
#     print("worng password")
# elif username != "admin":
#     print("worng username")
# else:
#     print("try again")       


# Next Question 8: Number Comparison 
# User se do numbers input lo.
# - Dono numbers equal hain → Both numbers are equal
# - Pehla number bada hai → First number is greater
# - Doosra number bada hai → Second number is greater


# num1 = int(input("enter tha first number="))
# num2 = int(input("enter tha second number="))

# if num1 == num2:
#     print("Both numbers are equal")
# elif num1 > num2:
#     print("first number is greater")
# else:
#     print("second number is greater")


# Next Question 9: Find the Largest of Three Numbers 
# Bro, ab difficulty thodi badhate hain!

# Task: User se 3 numbers input lo.

# Conditions:
# - Agar num1 sabse bada hai → First number is largest
# - Agar num2 sabse bada hai → Second number is largest
# - Agar num3 sabse bada hai → Third number is largest
# - Agar teeno equal hain → All numbers are equal

# num1 = int(input("enter tha first number:"))
# num2 = int(input("enter tha second number:"))
# num3 = int(input("enter tha third number:"))

# if num1 > num2 and num1 > num3:
#     print("first number is largest")
# elif num2 > num1 and num2 > num3:
#     print("second number is largest")
# elif num3 > num1 and num3 > num2:
#     print("third number is largest")
# else:
#     print("all number are equal")


# Next Question 10: Leap Year Checker 
# Ek year user se input lo.

# leap = int(input("enter tha number:"))

# if leap % 4 == 0:
#     print("leap year")
# else:
#     print("not a leap year")    


# Next Question 11: Number Classifier 
# Bro, ab ek question mein multiple conditions use karni hain.

# User se ek number input lo.
# - Number positive aur even hai → Positive Even
# - Number positive aur odd hai → Positive Odd
# - Number negative hai → Negative Number
# - Number zero hai → Zero


# num = int(input("enter tha number:"))

# if num % 2 == 0 and num > 0:
#     print("positive even")
# elif num % 2 == 1 and num > 0:
#     print("positive odd")
# elif num < 0:
#     print("negative number")
# elif num == 0:
#     print("number is zero")
# else:
#     print("enter valid number")         


# Next Question 12: Simple Calculator 
# User se do numbers aur ek operator (+, -, *, /) input lo.

# num1 = int(input("enter a  frist number:"))
# op = input("enter a opertors:+, - , *, /:")
# num2 = int(input("enter a second number:"))

# if op == "+":
#     print("result:", num1 + num2)

# elif op == "-":
#     print("result:", num1 - num2)

# elif op == "*":
#     print("result:", num1 * num2)    

# elif op == "/":
#     print("result:",num1 / num2) 

# else:
#     print("invalid op")
