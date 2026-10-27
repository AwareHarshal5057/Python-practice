# What is Polymorphism?
# English: Polymorphism means “Many Forms.” The same method name can behave differently depending on the object.

# Hindi: Polymorphism ka matlab hai ek hi method ka alag-alag objects ke liye alag tarike se kaam karna.


# class cat:
#     def sound(self):
#         print("abc")

# class dog:
#     def sound(self):
#         print("bca")

# c1 = cat()
# d1 = dog()

# c1.sound()
# d1.sound()

# Polymorphism using Inheritance
# Ab Father aur Son ko inheritance se connect karte hain.

# class father:
#     def work(self):
#         print("harshal")


# class son(father):
#     def work(self):
#         print("coding")


# s1 = son()

# # s1.work()


# polymorphism using a common method
# Ab ek aur important concept samjho. Hum do alag classes banayenge, lekin dono mein method ka naam same rakhenge.

# class Dog:
#     def sound(self):
#         print("Bark")


# class Cat:
#     def sound(self):
#         print("Meow")


# def make_sound(animal):
#     animal.sound()


# d1 = Dog()
# c1 = Cat()

# make_sound(d1)
# make_sound(c1)


# Python Polymorphism ke Types

# 1. Method Overriding
# Child class, parent class ke method ko apne hisaab se redefine karti hai.

# class Father:
#     def work(self):
#         print("Business")


# class Son(Father):
#     def work(self):
#         print("Coding")


# s1 = Son()
# s1.work()

# Duck Typing
# Alag-alag classes ke objects mein same method ho, toh Python un objects ke saath kaam kar sakta hai.

# class Dog:
#     def sound(self):
#         print("Bark")


# class Cat:
#     def sound(self):
#         print("Meow")


# def make_sound(animal):
#     animal.sound()


# make_sound(Dog())
# make_sound(Cat())

# Operator Overloading
# Same operator ka behavior objects ke according alag ho sakta hai.

# print(10 + 20)
# print("Hello " + "Harshal")

# Method Overloading
# Ek hi method name ko different parameters ke saath use karna.

# class Calculator:
#     def add(self, a, b=0):
#         print(a + b)


# c1 = Calculator()

# c1.add(10)
# c1.add(10, 20)