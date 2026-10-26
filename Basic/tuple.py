# Python Tuple kya hai?
# Tuple Python ka ek data type hai jisme hum multiple values ek hi variable mein store kar sakte hain.

# numbers = (10, 20, 30, 40, 50)
# print(numbers)

# # Integer tuple
# numbers = (10, 20, 30)

# # String tuple
# names = ("Harshal", "Rahul", "Amit")

# # Mixed tuple
# data = ("Harshal", 22, 75.5, True)

# print(numbers)
# print(names)
# print(data)



# numbers = (10, 20, 30)

# numbers[0] = 100

# print(numbers)

# TypeError: 'tuple' object does not support item assignment
# Kyun? Tuple immutable hota hai, matlab tuple banane ke baad uski existing values ko directly change nahi kar sakte.

# Python Tuple ke sirf 2 built-in methods hote hain:

# 1. count()

# numbers = (10, 20, 10, 30, 10)
# print(numbers.count(10))

# 2. index()
# numbers = (10, 20, 30, 40)
# print(numbers.index(30))

# | Function | Use |
# |---|---|
# | `len()` | Total elements count karna |
# | `max()` | Sabse badi value |
# | `min()` | Sabse chhoti value |
# | `sum()` | Numbers ka total |
# | `sorted()` | Values ko sort karke list dena |
# | `tuple()` | List/string ko tuple mein convert karna |
# | `any()` | Koi ek element truthy hai ya nahi |
# | `all()` | Saare elements truthy hain ya nahi |
# | `type()` | Data type check karna |

# numbers = (10, 20, 30, 40, 50)

# print(len(numbers))
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
# print(sorted(numbers))
# print(type(numbers))