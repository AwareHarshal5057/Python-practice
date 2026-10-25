# List kya hoti hai?
# Definition: Python list ek collection hai jisme hum multiple values ko ek hi variable mein store kar sakte hain.

# fruits = ["Apple", "Banana", "Mango"]

# print(fruits)

# List kaise banate hain?
# List banane ke liye square brackets [] use karte hain.

# numbers = [10, 20, 30, 40, 50]
# names = ["Harshal", "Rahul", "Amit"]
# mixed = [10, "Python", 20.5, True]

# print(numbers)
# print(names)
# print(mixed)


# Python List Methods

# 1. append() — last mein item add karna

# name = ["harshal","jay"]
# name.append("viraj")
# print(name)

# 2. insert() — specific position par item add karna

# name = ["harshal","jay"]
# name.insert(1,"viraj")
# print(name)

# 3. extend() — multiple items add karna

# a = [10,20]
# a.extend([30,40])
# print(a)

# 4. remove() — value remove karna

# a = [10,20,30,40]
# a.remove(20)
# print(a)

# 5. pop() — index se item remove karna

# a = [10,20,30,40]
# a.pop(2)
# print(a)

# 6. clear() — saare items remove karna

# num = [10,20,30]
# num.clear()
# print(num)

# 7. index() — item ka index find karna
# name = ["harshal","jay","kalpesh"]
# print(name.index("jay"))


# 8. count() — item kitni baar hai

# a = [10,20,10,30,10]
# print(a.count(10))

# 9. sort() — list ko sort karna

# a = [10,30,40,20,50]
# a.sort()
# print(a)

# Descending order:
# a.sort(reverse=True)
# print(a)

# 10. reverse() — list ka order reverse karna

# numbers = [10, 20, 30, 40]
# numbers.reverse()

# print(numbers)

# 11. copy() — list ki copy banana

# a = [10, 20, 30]
# b = a.copy()

# print(b)

# Question 1 — append() and remove()

# numbers = [10, 20, 30, 40]

# numbers.append(50)
# numbers.remove(20)

# print(numbers)


# q2 =  append(), insert() aur pop()

# numbers = [10, 20, 30, 40]

# numbers.append(50)
# numbers.insert(4,50)
# numbers.pop(2)

# print(numbers)

# Question 3 — sort() and reverse()
# numbers = [40, 10, 30, 20]

# numbers.sort()
# numbers.reverse()
# numbers.append(50)

# print(numbers)

# numbers = [5, 10, 15, 20, 25]

# numbers.remove(15)
# numbers.pop(2)
# numbers.append(30)

# print(numbers)


# Question 5 — insert(), sort() and pop()

# numbers = [30, 10, 40, 20]

# numbers.insert(1, 15)
# numbers.sort()
# numbers.pop()

# print(numbers)