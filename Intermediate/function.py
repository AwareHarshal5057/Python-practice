# Function kya hota hai?
# Function code ka ek reusable block hota hai. Ek baar function bana do, phir use multiple times call kar sakte ho.

# def name():
#     print("harshal")

# name()    

# def — function banane ke liye keyword.
# greet — function ka naam.
# () — function ke parameters yahan aate hain.
# : — function body start hoti hai.
# Indentation — function ke andar ka code.
# greet() — function ko call karna.

# Function with parameters

# def greet(name):
#     print("hello",name)

# greet("harshal")    

# def add(a,b):
#     print(a + b)

# add(20,10)    
# add(15,23.5)

# return statement
# return function se result wapas deta hai, jise hum variable mein store kar sakte hain.

# def add(a,b):
#     return a + b

# result = add(10,20)

# print(result)

# Default parameter
# Agar argument pass nahi kiya, toh default value use hogi.

# def xyz(name="hey"):
#     print("hello",name)

# xyz()
# xyz("harshal")    

# Keyword arguments
# Arguments ko parameter ke naam se pass kar sakte ho.

# def student(name,age):
#     print(name,age)


# student("harshal",21)
# student(age=21,name="harshal")

# Question 1: Add Two Numbers
# def add(a,b):
#     print(a + b)

# add(20,10)     

# Return Statement
# def squ(number):
#     return number * number

# result = squ(5)
# print(result)

# Function ke andar if-else

# def check_number(number):
#     if number % 2 == 0:
#         print("even number")
#     else:
#         print("odd number")

# check_number(10)
# check_number(7)


# Function ke andar for loop

# def check_number():
#     for i in range(1,6):
#         print(i)


# check_number()

# Explain how to write a function that checks whether numbers from 1 to 10 are even or odd using a loop and if-else.

# def check():
#     for number in range(1,11):
#         if number % 2 == 0:
#             print("even")
#         else:
#             print("odd")


# check()

# Positive or Negative
# Explain how to write a function that checks whether each number in a list [-2, 5, -7, 3, 0] is positive, negative, or zero.


# def check_number():
#    numbers = [-2, 5, -7, 3, 0]

#    for i in numbers:
#       if i > 0:
#          print("positive")
#       elif i < 0:
#          print("negative")
#       else:
#          print("zero")       

# check_number()

# Print Even Numbers
# Explain how to write a function that prints only even numbers from 1 to 20 using a loop and if.

# def even():
#     for i in range(1,21):
#         if i % 2 == 0:
#             print(i)


# even()

# Find Numbers Greater Than 10
# Explain how to write a function that loops through [5, 12, 8, 20, 3, 15] and prints only numbers greater than 10.

# def greate():
#     numbers = [5,12,8,20,3,15]

#     for i in numbers:
#         if i > 10:
#             print(i, "greater ")
#         else:
#             print(i, "numbers not greater")


# greate()

# Pass or Fail
# Explain how to write a function that checks marks [35, 80, 25, 60, 90]. Print "Pass" for marks 35 or above and "Fail" otherwise.

# def marks():
#     numbers = [35,80,25,60,90]

#     for i in numbers:
#         if i > 35:
#             print(i,"pass")
#         else:
#             print(i,"fail")


# marks()

#  Question 6: Multiplication Table
# Explain how to write a function that prints the multiplication table of 5 from 1 to 10, but prints "Skip" instead of the result when the multiplier is 5.    


# def table():
#     for i in range(1,11):
#         if i == 5:
#             print("skip")
#         else:
#             print(5*i) 


# table()               