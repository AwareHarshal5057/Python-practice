# nheritance kya hota hai?
# Inheritance ka matlab hai ek class ke properties aur methods ko doosri class mein use karna.


# class Father:
#     def house(self):
#         print("Father has a house")


# class Son(Father):
#     pass


# s1 = Son()

# s1.house()


# Parent aur Child ke apne methods

# class Father:
#     def house(self):
#         print("Father has a house")


# class Son(Father):
#     def bike(self):
#         print("Son has a bike")


# s1 = Son()

# s1.house()
# s1.bike()


# Inheritance with __init__()

# class Father:
#     def __init__(self, name):
#         self.name = name


# class Son(Father):
#     pass


# s1 = Son("Harshal")

# print(s1.name)

# class father:
#     def __init__(self,name):
#         self.name = name


# class son(father):
#     def __init__(self, name,age):
#          super().__init__(name)
#          self.age = age 


# s1 = son("harshal",22)

# print(s1.name)
# print(s1.age)

        
# 1. Single Inheritance
# Ek Child class, ek Parent class se inherit karti hai.

# class Father:
#     def house(self):
#         print("Father has a house")


# class Son(Father):
#     def bike(self):
#         print("Son has a bike")


# s1 = Son()

# s1.house()
# s1.bike()

# Multiple Inheritance
# Ek Child class, multiple Parent classes se inherit karti hai.

# class Father:
#     def house(self):
#         print("Father has a house")


# class Mother:
#     def car(self):
#         print("Mother has a car")


# class Son(Father, Mother):
#     def bike(self):
#         print("Son has a bike")


# s1 = Son()

# s1.house()
# s1.car()
# s1.bike()


# Multilevel Inheritance
# Ek class doosri class se inherit karti hai, aur teesri class doosri class se inherit karti hai.

# class Grandfather:
#     def house(self):
#         print("Grandfather has a house")


# class Father(Grandfather):
#     def car(self):
#         print("Father has a car")


# class Son(Father):
#     def bike(self):
#         print("Son has a bike")


# s1 = Son()

# s1.house()
# s1.car()
# s1.bike()


# 4. Hierarchical Inheritance
# Ek Parent class se multiple Child classes inherit karti hain.

# class Father:
#     def house(self):
#         print("Father has a house")


# class Son(Father):
#     def bike(self):
#         print("Son has a bike")


# class Daughter(Father):
#     def car(self):
#         print("Daughter has a car")


# s1 = Son()
# d1 = Daughter()

# s1.house()
# s1.bike()

# d1.house()
# d1.car()

# Hybrid Inheritance
# Hybrid Inheritance ka matlab hai do ya zyada inheritance types ko combine karna.


# class Father:
#     def house(self):
#         print("Father has a house")


# class Mother:
#     def car(self):
#         print("Mother has a car")


# class Son(Father, Mother):
#     def bike(self):
#         print("Son has a bike")


# class Daughter(Father):
#     def dance(self):
#         print("Daughter can dance")


# s1 = Son()
# d1 = Daughter()

# s1.house()
# s1.car()
# s1.bike()

# d1.house()
# d1.dance()