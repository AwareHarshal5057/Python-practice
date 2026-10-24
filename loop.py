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