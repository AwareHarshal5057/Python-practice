# What is Scope?
# Definition: Scope in Python defines where a variable can be accessed or used in a program.

# Simple hindi: Scope ka matlab hai ki variable ko program mein kahan use kar sakte hain.


# x = 10

# def  show():
#     print(x)

# show()
# print(x)    

# x = 10 function ke bahar hai, isliye ye global variable hai.
# show() ke andar bhi x use ho sakta hai.
# Function ke bahar bhi x use ho sakta hai.

# Types of Scope in Python

# 1. Local Scope
# Function ke andar banaya gaya variable.
# def show():
#     x = 10
#     print(x)

# show()    

# 2. Enclosing Scope
# Ek outer function ka variable, jo inner function mein use hota hai.
# def outer():
#     x = 20

#     def inner():
#         print(x)

#     inner()

# outer()

# 3. Global Scope
# Function ke bahar banaya gaya variable.

# x = 30

# def show():
#     print(x)

# show()

# 4. Built-in Scope
# Python ke predefined names, jaise print(), len(), sum().

# num = [10,20,30]

# print(len(num))

# Local Scope in detail

# def name():
#     name= "harshal"
#     print(name)

# name()    

# def name():
#     name="harshal" 

# name()
# print(name)    

# Output mein NameError aayega, kyunki name function ke bahar accessible nahi hai.


# Global Scope in detail

# x = 100

# def show():
#     print(x)

# show()
# print(x)
# Global variable ko function ke andar read kar sakte ho.

# Global variable ko change kaise karein?
# x = 10

# def change():
#     global x
#     x = 50

# change()
# print(x)