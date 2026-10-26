# OOP kya hai?
# OOP ka full form hai Object-Oriented Programming.

# Python mein OOP ka use karke hum code ko Class aur Object ki help se organize karte hain.

# Class kya hoti hai?
# Class ek blueprint (design) hoti hai, jiske through hum objects banate hain.

# class car:
#     color = "red"
#     name   = "bmw"

# print(car.color)
# print(car.name)

# class — class banane ka keyword.
# Car — class ka naam.
# color aur brand — class attributes.
# Car.color — attribute ki value access karna.

# Object kya hota hai?
# Object class se banne wali actual instance hoti hai.

# class car:
#     color = "red"
#     name = "bmw"

# car1 = car()
# car2  = car()

# print(car1.color)
# print(car2.name)

# Car — class hai.
# car1 — pehla object hai.
# car2 — doosra object hai.
# Car() — class ka object banata hai.

# Class ko blueprint aur object ko us blueprint se bani actual car samjho.


# class student:
#     name = "harshal"
#     age = "22"

# stu = student()

# print(stu.name)
# print(stu.age)

# __init__() Constructor
# Bro, ab maan lo tumhe 3 students banane hain, aur har student ka name alag hai. Kya har baar class mein name change karoge? Nahi!

# class student:
#     def __init__(self,name,age):

#         self.name = name
#         self.age = age

# stu1 = student("harshal",22) 
# stu2 = student("jay",19) 

# print(stu1.name)
# print(stu1.age)


# self kya hota hai?
# self current object ko refer karta hai. 

# class student:
#     def __init__(self,name):
#         self.name = name

#     def show(self):
#         print(self.name)    

# stu1 = student("harshal")

# stu1.show()

# class stu:
#     def __init__(self,name):
#         self.name = name

#     def show(self):
#         print(self.name)

# m1 = stu("harshal")
# m2 = stu("jay")

# m2.show()


# class stu:
#     school = "abc school"
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def show(self):
#         print(self.name,self.age)

# s1 = stu("harshal",22)
# s2 = stu("jay",23)

# s1.show()
# s2.show()       


# print(s1.name)   
# print(s2.age) 
# print(s2.school)
# print(s1.school)



# tributes ke types

# - Class Attribute: Class mein directly define hota hai, jaise school = "ABC School".
# - Instance Attribute: Har object ka apna data hota hai, jaise self.name = name.


# class Student:
#     school = "ABC School"  # Class Attribute

#     def __init__(self, name):
#         self.name = name    # Instance Attribute

# s1 = Student("Harshal")
# s2 = Student("Rahul")

# print(s1.school)
# print(s2.school)

# print(s1.name)
# print(s2.name)