#Swapping numbers
# x=11
# y=13
# print(x,y)
# y,x=x,y
# print(x,y)
# del x
# print(x)

#Arthmatic operators
# a=5
# b=2
# print(a**b)

# #Concatenation
# str="Bhanu"
# print("My Name is "+str+" I am 24 years old!")
#
# #Formatting out put
# name="Bhanu"
# age=24
# sal=2222
# print("Name is:",name)
# print("Age is:",age)
# print("Sal is:",sal)
#
# print("Name is %s age is %d sal is %g"%(name,age,sal))
#
# print("Name is {} age is {} sal is {}".format(name,age,sal))

#Input from user
# user_name=input("Enter your name")
# print(user_name)
# id=int(input("enter your id:"))
# print(id)

#Leap year

year=int(input("Enter the year"))
if year%4==0 and year%100!=0:
    print("Leap year")
elif year%100==0 and year%400==0:
    print("leap year")
else:
    print("not leap year")