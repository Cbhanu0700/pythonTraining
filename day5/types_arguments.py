 #Ex 1:
# def func(x,y):
#      print(x,y)
#
# func(10,29)#Positional arguments
# func(y=22,x=33)#keyword arguments


#Ex 2:
# def func(x, y=33):
#      print(x, y)
#
# func(10,22)
# func(10)  # Positional arguments

# #ex 3:
# def greetings(name,greetmsg):
#     print(name+" "+greetmsg)
# greetings(greetmsg="Hello",name="Bhanu")

# ex 4:
# def func(a,b,c):
#     print(a,b,c)
# func(12,33,c=44)
# func(a=33,b=44,45)
#func(33,44,b=45)

#Ex 5:
def largest(a,b):
    if a>b:
        return a,b
    else:
        return b,a
print(largest(10,2))
res=largest(10,22)
print(type(res))