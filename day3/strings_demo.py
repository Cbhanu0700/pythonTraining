#name="Bhanu Prakash"
# user_id=""


#id
# name="Bhanu"
# print(id(name))
# name=name+"Prakash"
# print(name)
# print(id(name))

# + and * with strings

# name="Bhanu"
# print(name+"Prakash")  #o/p: BhanuPrakash
# print(name*2) #o/p: BhanuBhanu

#Slicing in strings
# str="Bhanuprakash"
# print(str[1:3])
# print(str[:9])
# print(str[3:])
# print(str[3:-2])

# ord() and chr()

# print(ord('@'))
# print(chr(69))

#min() max() len()
# a="bhanuprakash"
# print(max(a))
# print(min(a))
# print(len(a))

# in and not in

# a="Chandubhanuprakash"
# print("chandu" in a)
# print("anp" not in a)

#String comparison
# str1 = "apple"
# str2 = "banana"
#
# print(str1 == str2)   # False
# print(str1 != str2)   # True
# print(str1 < str2)    # True (because 'a' < 'b')
# print(str1 > str2)    # False

#Testing Strings
# s = "welcome to python"
# print(s.isdigit())   # false
# print(s.isalpha())   # false
# print(s.islower())  #true
# print(s.isalnum())   # false
# print(s.isspace())   # false
# print(s.istitle())   # false
# print(s.isidentifier()) # false

#searching for substrings
# text = "hello world"
# print(text.find("world"))
# print(text.startswith("hel"))
# print(text.endswith("d"))
# print(text.find("wod"))
# print(text.count("o"))

# Converting strings

# s="BHanu prakash"
# print(s.capitalize())
# print(s.lower())
# print(s.title())
# print(s.upper())
# print(s.swapcase())
# print(s.replace("BH","bh"))

#reverse a String

s="Bhanu"
p=""
for i in s:
    p=i+p
print(p)

#approach 2
a="Bhanu"
b=""
print(a[::-1])

abc=""
print(id(abc))