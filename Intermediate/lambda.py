# 1. Lambda Function kya hota hai?
# English definition: A lambda function is a small anonymous function that can contain only one expression.

# Hindi mein: Lambda ek chhota function hota hai jise hum lambda keyword se banate hain. Isme def aur return likhne ki zaroorat nahi hoti.


# Normal function vs Lambda function
# def add(a, b):
#     return a + b

# print(add(10, 20))


# add = lambda a, b: a + b
# print(add(10, 20))


# Lambda function ka syntax
# lambda arguments: expression

# squ = lambda x: x*x
# print(squ(5))

# Ek number ko double karna

# double = lambda x: x*2
# print(double(5))

# Do numbers ka subtraction

# sub = lambda a,b: a -b
# print(sub(10,5))

# Number even hai ya odd

# check = lambda x: "even" if x % 2 == 0  else "odd"
# print(check(5))

# Do numbers mein se bada number

# check = lambda a,b: a if a > b else b
# print(check(10,5))

# Lambda with map(), filter() and sorted()

# 1. map() function
# Definition: map() har element par ek function apply karta hai aur transformed results deta hai.

# Example: Har number ko double karna.

# num = [1,2,3,4,5]

# def add(x):
#     return x*2

# result = list(map(add,num))
# print(result)

# Lambda ke saath same example:

# num = [1,2,3,4,5]

# result = list(map(lambda x: x* 2,num))

# print(result)

# 2. filter() function
# Definition: filter() condition ke according sirf un elements ko select karta hai jo condition satisfy karte hain.

# num = [1,2,3,4,5,6,7,8]

# result = list(filter(lambda x: x % 2 == 0,num))
# print(result)

# 3. reduce() function
# Definition: reduce() elements ko combine karke ek final result deta hai. Iske liye functools se import karna hota hai.

# from functools import reduce

# numbers = [1, 2, 3, 4, 5]

# result = reduce(lambda x, y: x + y, numbers)

# print(result)


# Function	        Kaam	                            Example
# map()	    Har element ko transform karna	       Har number double
# filter()	Condition ke basis par select karna	   Even numbers
# lambda	    Short function banana	               lambda x: x * 2
# reduce()	Elements ko combine karna	           Total sum

