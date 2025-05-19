# Ex 1
# class myClass:
#     def myfun(self):
#         pass
#     def display(self,name):
#         print(name)
#
# mc1=myClass()
# mc1.display("Bhanu")
# mc1.myfun()


# #Ex 2
# class myClass:
#     def m1(self):
#         print("This is instance method")
#     @staticmethod
#     def m2(self,name):
#         print(self,name)
#
# mc1=myClass()
# mc1.m1()
# mc1.m2("Bhanu","Prakash")

#Ex 3:
# class MyClass:
#   a,b=10,20
#   def add(self):
#       print(self.a+self.b)
#   def mul(self):
#       print(self.a*self.b)
# mc=MyClass()
# mc.add()
# mc.mul()

#ex 4
# i,j=11,22
# class MyClass:
#     a,b=10,20
#     def add(self,x,y):
#         print(x+y)
#         print(i+j)
#         print(self.a+self.b)
# mc=MyClass()
# mc.add(33,44)


#ex 5:
# a,b=11,22
# class MyClass:
#     a,b=10,20
#     def add(self,a,b):
#         print(a+b)
#         print(globals()['a']+globals()['b'])
#         print(self.a+self.b)
# mc=MyClass()
# mc.add(33,44)

#ex 6:
# class MyClass:
#     def dis(self,name):
#         print(name)
#         print("This is display")
# m1=MyClass()
# m1.dis("Bhanu")
# m2=MyClass()
# m2.dis("Prakash")


#Ex 7:
# class MyClass:
#     def __init__(self):
#         print("This is constructor")
#     def dis(self):
#         print("Self")
#     def add(self,x,y):
#         return(x+y)
# mc=MyClass()
#
# print(mc.add(10,20))
# mc.dis()

#Ex 8:
#
# class MyClass:
#     name="Bhanu"
#     def __init__(self,name):
#         print(name)
#         print(self.name)
#
# mc=MyClass("Prakash")

#Ex 9:

class Emp:
    def __init__(self,eid,esal,ename):
        self.empid=eid
        self.ename=ename
        self.esal=esal

    def display(self):
       print(self.empid,self.ename,self.esal)

mc=Emp(1,"Bhanu",10000)
mc.display()