#  1: File Handling kya hai?
# File Handling ka use Python se file ko create, read, write aur update karne ke liye hota hai.

# Mode	Meaning
# "r"	File read karna
# "w"	File write karna; purana content delete ho sakta hai
# "a"	File ke end mein content add karna
# "x"	Nayi file create karna; file pehle se ho toh error
# "r+"	Read aur write dono
# "b"	Binary mode, jaise images
# "t"	Text mode (default)

# file = open("data.txt", "w")

# file.write("Hello")

# file.close()

# Samjho:
# - open() — file open karta hai.
# - "w" — file mein likhta hai.
# - write() — text save karta hai.
# - close() — file close karta hai.
# Agar data.txt nahi hai, toh "w" mode use karne par Python use create kar dega.



# File read karna
# Ab data.txt mein Hello Harshal likha hai.

# file = open("data.txt", "r")

# content = file.read()

# print(content)

# file.close()

# file =  open("max.text" , "w")
# file.write("python")
# file.close()

# file = open("max.text","r")
# con = file.read()
# print(con)

# File mein append karna

# file = open("data.txt","a")
# file.write(" i am learning python")
# file.close()


# File mein check karna ki file exist karti hai ya nahi
# import os

# if os.path.exists("data.txt"):
#     print("File exists")
# else:
#     print("File does not exist")

# File delete karne ke liye:
# import os

# if os.path.exists("data.txt"):
#     os.remove("data.txt")
#     print("File deleted")

# Exception Handling ke saath File Handling
# try:
#     with open("data.txt", "r") as file:
#         print(file.read())

# except FileNotFoundError:
#     print("File not found")