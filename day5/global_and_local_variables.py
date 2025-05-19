# #Ex 1:
#
# global_var=10
# def func():
#     local_var=30
#     print(local_var)
#     print(global_var)
#
# func()
# print(global_var)
# print(local_var)


#ex 2:
# global_var=10
# def func():
#     global_var=30
#     print(global_var)
# func()

#ex 3:
# global_var=10
# def func():
#     global global_var
#     global_var=30
#     print(global_var)
# func()
# print(global_var)

#Ex 4:
# global_var=10
# def func():
#     global global_var
#     global_var=30
#     print(global_var)
# # func() 
# print(global_var)

#ex 5:

def func():
    global global_var
    global_var=30
    print(global_var)
func()
print(global_var)