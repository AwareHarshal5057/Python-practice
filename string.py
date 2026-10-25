# Python String kya hoti hai?
# String ka matlab text hota hai. Python mein string ko single quotes ' ' ya double quotes " " mein likhte hain.

# name = "harshal"
# city = "surat"

# print(name)
# print(city)

# Important Python String Methods

# 1. upper() — Capital letters
# String ke saare letters capital kar deta hai.

# name = "harshal"
# print(name.upper())

# 2. lower() — Small letters
# String ke saare letters small kar deta hai.

# name = "HARSHAL"
# print(name.lower())

# 3. capitalize() — First letter capital
# Sirf string ka first character capital karta hai aur baaki characters lowercase karta hai.

# name = "harshal"
# print(name.capitalize())


# 4. title() — Har word ka first letter capital

# name = "harshal aware"
# print(name.title())


# 5. strip() — Extra spaces remove
# Starting aur ending ke spaces remove karta hai.

# name = "  harshal  "
# print(name.strip())


# 6. replace() — Text replace karna
# Ek text ko doosre text se replace karta hai.

# name = "i like java"
# print(name.replace("java","python"))

# 7. find() — Text ki position find karna
# Text kis index par start ho raha hai, woh batata hai. Python mein indexing 0 se start hoti hai.

# name = "python"
# print(name.find("h"))

# Agar text nahi milta, toh -1 return hota hai.

# 8. count() — Kitni baar aaya?

# name = "banana"
# print(name.count("a"))

# 9. startswith() — Starting check karna

# name = "harshal and python"
# print(name.startswith("harshal"))

# 10. endswith() — Ending check karna

# name = "harshal and python"
# print(name.endswith("harshal"))
# print(name.endswith("python"))

# 11. split() — String ko list mein convert karna

# name = "harshal, jay, hardik"
# print(name.split())

# answers list milta hai 

# 12. join() — List ko string mein jodna

# name = ["harshal",  "and", "jay"]
# print(" ".join(name))

# 13. isalpha() — Sirf letters hain?

# text = "Harshal"
# print(text.isalpha())

# 14. isdigit() — Sirf digits hain?

# text = "12345"
# print(text.isdigit())

# 15. isalnum() — Letters aur numbers?

# text = "Harshal123"
# print(text.isalnum())

# Step 1: String Indexing kya hai?
# Indexing ka matlab hai string ke andar kisi particular character ki position access karna.

# text = "PYTHON"

# print(text[0])
# print(text[1])
# print(text[2])

# Negative Indexing
# Negative indexing mein right side se counting hoti hai.

# text = "python"

# print(text[-1])

# text[0] → first character
# text[1] → second character
# text[-1] → last character
# text[-2] → second-last character


# Step 2: String Slicing kya hai?
# Slicing ka matlab hai string ka ek part nikalna.

# string[start:end:step]
# start = kis index se start karna hai.
# end = kis index se pehle rukna hai. End index include nahi hota.
# step = step matlab ki kitna chalna

# name = "python"
# print(name[0:3])
# print(name[1:4])
# print(name[-1:-3:-1])


# 1. Starting se characters lena

# text = "PYTHON"
# print(text[:3])

# 2. Ending tak characters lena
# text = "PYTHON"
# print(text[2:])

# 3. Puri string copy karna

# text = "PYTHON"
# print(text[:])
