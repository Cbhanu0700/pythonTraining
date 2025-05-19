# Ex 1: Creating a dictionary
#
# my_dict={101:"x",102:"y",103:"z"}
# print(my_dict)

#Ex 2: Accessing the item from dictionary

# my_dict={
#
#     "Brand":"Hyundai",
#     "Model":"i10",
#     "Year":2021
# }
# print(my_dict["Brand"])
# print(my_dict.get("Brand"))

#Ex 3:change values in dictionary

# my_dict={
#
#     "Brand":"Hyundai",
#     "Model":"i10",
#     "Year":2021
# }
#
# my_dict['Year']=2022
# print(my_dict)

#Ex 4: reading items from dictionary using loop

# my_dict={
#
#     "Brand":"Hyundai",
#     "Model":"i10",
#     "Year":2021
# }
#
# for i in my_dict:
#     print(i)
# for i in my_dict:
#         print(my_dict[i])
# for i in my_dict.values():
#     print(i)
# for x,y in my_dict.items():
#     print(x,y)


# Ex 5:Check key is exists in dictionary or not

# my_dict={
#
#     "Brand":"Hyundai",
#     "Model":"i10",
#     "Year":2021
# }
#
# # for i in my_dict:
# #     if(i=="Brand"):
# #         print("Brand Exists")
#
# if "Brand" in my_dict:
#     print("Exists")
# else:
#     print("not exists")

#Ex 6:total number of items in dictionary
# my_dict={
#
#     "Brand":"Hyundai",
#     "Model":"i10",
#     "Year":2021
# }
#
# print(len(my_dict))

#Ex 7:Adding items in dictionary

# my_dict={
#
#     "Brand":"Hyundai",
#     "Model":"i10",
#     "Year":2021
# }
#
# my_dict["color"]="red"
# print(my_dict)

#ex 8:Removing item in dictionary
# my_dict={
#
#     "Brand":"Hyundai",
#     "Model":"i10",
#     "Year":2021
# }
#
# my_dict.pop("Brand")
# del my_dict["Year"]
# print(my_dict)
# my_dict.clear()
# print(my_dict)

#Ex 9: copying dictonaries
my_dict={

    "Brand":"Hyundai",
    "Model":"i10",
    "Year":2021
}

mydict1=my_dict
print(mydict1)

mydict2=my_dict.copy()
print(mydict2)
