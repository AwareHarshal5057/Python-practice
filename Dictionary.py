# Dictionary kya hoti hai?
# Dictionary Python mein data ko key : value pair mein store karti hai.

# student = {
#     "name": "Harshal",
#     "age": 22,
#     "city": "Surat"
# }

# print(student)

# Python Dictionary Commands

# stu = {"name":"harshal", "age":22}

# Dictionary create karna
# stu = {"name":"harshal", "age":22}
# print(stu)

# get() — Value lena
# stu = {"name":"harshal", "age":22}
# print(stu.get("name"))
# print(stu.get("age"))

# keys() — Saari keys lena
# print(stu.keys())

# values() — Saari values lena
# print(stu.values())


# # items() — Key-value pairs lena
# print(stu.items())

# update() — Data update ya add karna
# # stu.update({"age":23})
# print(stu)

# pop() — Specific item remove karna
# stu.pop("age")
# print(stu)

# popitem() — Last item remove karna
# name = {"name": "harshal", "age":21}
# name.popitem()
# print(name)

# clear() — Dictionary empty karna
# name = {"name": "harshal", "age":21}
# name.clear()
# print(name)

# copy() — Dictionary copy karna
# name = {"name": "harshal", "age":21}
# new = name.copy()
# print(new)

# setdefault() — Missing key add karna

# stu = {"name": "harshal"}
# stu.setdefault("city","surat")
# print(stu)

# fromkeys() — Keys se dictionary banana
# keys = ["name", "age", "city"]
# student = dict.fromkeys(keys, 0)
# print(student)


# len() — Total items count karna
# student = {"name": "Harshal", "age": 22}
# print(len(student))


# del — Item delete karna
# student = {"name": "Harshal", "age": 22}
# del student["age"]
# print(student)

# for — Dictionary par loop
# student = {"name": "Harshal", "age": 22}

# for key, value in student.items():
#     print(key, value)