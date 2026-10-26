# What is a Set in Python?
# Definition: A set is a collection of unique elements. It does not allow duplicate values.

# numbers = {10, 20, 30, 20, 10}
# print(numbers)


# How to Create a Set

# # Integer set
# numbers = {10, 20, 30, 40}
# print(numbers)

# # String set
# names = {"Harshal", "Rahul", "Amit"}
# print(names)

# # Mixed data types
# data = {10, "Python", 20.5}
# print(data)


# numbers = {10, 20, 30, 40}
# print(numbers[0])
# TypeError: 'set' object is not subscriptable
# Kyunki set indexing support nahi karta.

# Set ke elements ko access karne ke liye for loop use kar sakte hain.
# numbers = {10, 20, 30, 40}

# for num in numbers:
#     print(num)


# 1. add() method
# numbers = {10, 20, 30}
# numbers.add(40)
# print(numbers)

# 2. update() method

# number = {10,20}
# number.update([30,40])
# print(number)

# 3. remove() method

# num = {10,20,30,40}
# num.remove(20)
# print(num)


# 4. discard() method
# num = {10,20,30,40}
# num.discard(20)
# print(num)

# 5. pop() method

# num = {10,20,30,40}
# num.pop()
# print(num)

# 6. clear() method
# num = {10,20,30,40}
# num.clear()
# print(num)

# 7. copy() method
# a = {10, 20, 30}
# b = a.copy()
# print(b)

# fruits = {"apple", "mango"}

# fruits.add("banana")

# print(len(fruits))

# union() Method
# a = {10, 20, 30}
# b = {30, 40, 50}
# result = a.union(b)
# print(result)


# 9. intersection() — common elements
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.intersection(b))

# 10. difference() — pehle set ke non-common elements
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.difference(b))

# 11. symmetric_difference() — dono sets ke non-common elements
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.symmetric_difference(b))

# 12. issubset() — check karna ki ek set doosre set ka subset hai
# a = {1, 2}
# b = {1, 2, 3}

# print(a.issubset(b))

