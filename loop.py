# 1. Loop kya hota hai?
# Loop ka use kisi code ko baar-baar execute karne ke liye hota hai.

# 1. for loop kya hota hai?
# for loop ka use kisi code ko baar-baar run karne ke liye hota hai, jaise numbers print karna ya list ke items ko ek-ek karke access karna.

# range() ka matlab hai kahan se start karna hai aur kahan tak chalna hai.


# for i in range(1,6):
#     print(i)

# for i in range(5,11):
#     print(i)

# Question 1: Print Even Numbers

# for i in range(2,21,2):
#     print(i)

# Question 2: Multiplication Table

# for i in range(5,51,5):
#     print(i)

# Question 3: Reverse Counting

# for i in range(10,0,-1):
#     print(i)

# Question 4: Sum of Numbers

# sum = 0;

# for i in range(1,11):
#     sum = i + sum

# print("sum:",sum)    



# Question 5: Odd Numbers

# for i in range(1,21):
#     if i % 2 == 1:
#         print(i)

# Question 6: Factorial Calculator
# range(1, num) → num se pehle tak.
# range(1, num + 1) → num tak.

# num = int(input("enter a number"))
# fact = 1

# for i in range(1,num+1):
#     fact = i * fact

# print(fact)     

# Multiplication Table
# User se ek number input lena hai aur uska 1 se 10 tak table print karna hai.

# num = int(input("enter a number"))

# for i in range(1,11):
#     print(i*num)

# Next question — Question 7 
# Bro, for loop use karke 1 se 10 tak ke numbers ka total sum calculate kar.

# sum = 0

# for i in range(1,11):
#     sum = sum + i

# print(sum)  

# Next question — Question 8 
# Bro, for loop use karke 1 se 20 tak sirf even numbers ka total sum calculate kar.

# total = 0

# for i in range(1,21):
#     if i % 2 == 0:
#        total = total + i

# print(total)        

# Next question — Question 9 
# Bro, ab 1 se 10 tak sirf odd numbers ka sum calculate kar.

# sum = 0

# for i in range(1,11):
#     if i % 2 == 1:
#         sum = sum + i

# print(sum)        


# : Factorial

# num = int(input("enter a number"))

# fact = 1

# for i in range(1,num+1):
#     fact = i * fact


# print(fact)    


# Count Digits

# int() → String ko integer mein convert karta hai.
# str() → Number ko string mein convert karta hai.
# float() → Number ko decimal value mein convert karta hai.
# range() -> number ko enter karta hai
# str() -> string ko enter karta hai 

# num = input("enter a number")
# count = 0

# for i in str(num):
#     count = 1 + count


# print(count)

# Reverse = 4321

# num = input("enter a number")
# reverse = ""

# for i in num:
#     reverse = i + reverse


# print(reverse)    

# prime number= 7

# num = int(input("enter a number:"))

# if num < 2:
#     print("not a prime number")
# else:
#     for i in range(2,num):
#         if num % i == 0:
#             print("not a prime number")
#             break
#         else:
#             print("prime number") 


# num = int(input("Enter a number: "))

# if num < 2:
#     print("Not a prime number")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number")



# while loop kya hota hai?
# Definition: Python mein while loop tab tak code repeat karta hai jab tak condition True hoti hai.

# i = 1
# while i <= 5:
#     print(i)
#     i = i + 1

# Reverse Counting

# i = 10
# while i >= 1:
#     print(i)
#     i = i - 1

# while loop se 1 se 10 tak numbers ka sum calculate karo.

# num = int(input("enter a number:"))
# sum = 0
# i = 1

# while i <= 10:
   
#     sum = sum + i
#     i = i + 1


# print(sum)
   
   
# Reverse a Number 

# num = input("enter a number")

# reverse = ""

# for i in num:
#     reverse = i + reverse

# print(reverse)    

# count the digits in a number

# num = int(input("enter a number: "))
# count = 0

# while num > 0:
#     count = 1 + count
#     num = num // 10

# print(count)    


# Palindrome Number check karne ka code.

# num = input("enter a number: ")
# reverse = ""

# for i in num:
#     reverse = i + reverse

# # print(reverse)

# if num == reverse:
#     print("palinrome number") 
# else:
#     print("not a palindrome number")       



# 1. break — loop ko stop karna
# break loop ko turant terminate kar deta hai.

# 2. continue — current iteration skip karna
# continue current iteration ko skip karke next iteration par chala jata hai.

# 10 tak numbers print karo, lekin 6 aate hi loop stop kar do.

# for i in range(1,11):
#     if i == 6:
#         break
#     print(i)

# Even numbers skip karo

# for i in range(1,11):
#     if i % 2 == 0:
     
#         continue
#     print(i)

# 1 se 10 tak numbers print karo, lekin 7 aate hi loop stop kar do.

# for i in range(1,11):
#     if i == 7:
#         break
#     print(i)
 

# 1 se 15 tak numbers print karo, lekin 3 aur 8 ko skip karna hai.

# for i in range(1,16):
#     if i == 3 or i == 8:
#         continue
#     print(i)
# 

# 1 se 20 tak numbers mein:
# - Even numbers skip karo.
# - Number 15 aate hi loop stop karo.


# for i in range(1,21):
#     if i % 2 == 0:
#         continue
#     if i == 15:
#         break

#     print(i)


# 1 se 20 tak numbers print karo, lekin:
# - Number 5 aate hi skip karo.
# - Number 12 aate hi loop stop karo.
# - continue aur break dono use karo.

# for i in range(1,21):
#     if i == 5:
#         continue
#     if i == 12:
#         break
#     print(i)