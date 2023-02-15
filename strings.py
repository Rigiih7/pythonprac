str1 = "22-01-2023"
strz = str1.split("-")
print(strz)
print(strz[2])

str2 = "i am rich now fuckers!!"
stra = str2.capitalize()
strb = str2.title()
strc = str2.upper()
strd = strb.swapcase()
print(stra)
print(strb)
print(strc)
print(strd)

if "rich" in str2:
    print("True")
