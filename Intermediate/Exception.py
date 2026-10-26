# Exception Handling kya hota hai?
# Exception handling ka use program mein aane wale errors ko handle karne ke liye hota hai, taaki program achanak crash na ho.

# a = 10
# b = 0

# print(a/b)
# ZeroDivisionError: division by zero

# try and except

# try:
#     a = 10
#     b = 0
#     print(a/b)

# except:
#     print("something went wrong")  

# try — jis code mein error aa sakta hai.
# except — agar error aaya, to kya karna hai.

# Specific Exception Handle Karna

# try:
#     a = 10
#     b = 0
#     print(a / b)

# except ZeroDivisionError:
#     print("Number cannot be divided by zero")


# ValueError
# Jab value ka type ya format sahi nahi hota, tab ValueError aa sakta hai.  

# try:
#      a = int("25")
#      print(a)

# except ValueError:
#      print("plz enter a valid number")     


# try: 
#     a = int("harshal")
#     print(a)

# except:
#     print("enter valid number")


# else block
# else tab execute hota hai jab try block mein koi error nahi aata.  

# try:
#     number = int("25")

# except ValueError:
#     print("Invalid number")

# else:
#     print("Your number is", number)

# try — code run karo.
# except — error handle karo.
# else — error nahi aaya, to ye code run karo.

# finally block
# finally block normally har situation mein execute hota hai, chahe error aaye ya na aaye.

# try:
#     print(10 / 2)

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# finally:
#     print("Program finished")

# raise keyword
# raise ka use khud se exception generate karne ke liye hota hai.

# age = -5

# if age < 0:
#     raise ValueError("Age cannot be negative")



# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))

#     print(a / b)

# except ValueError:
#     print("Please enter numbers only")

# except ZeroDivisionError:
#     print("Cannot divide by zero")



# Exception Handling ka complete structure
# try:
#     # Code that may cause an error
#     pass

# except ValueError:
#     # Handle the error
#     pass

# else:
#     # Runs if no exception occurs
#     pass

# finally:
#     # Runs whether an exception occurs or not
#     pass