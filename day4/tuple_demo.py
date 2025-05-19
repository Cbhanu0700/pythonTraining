#ex 1:creating a tuple
# tuple=("Apple",'Banana','cherry','Kiwi','Mango','lemon')
# tuple1=()
# print(tuple)
# print(tuple1)

#Ex 2: access the tuple

# tuple=("Apple",'Banana','cherry','Kiwi','Mango','lemon')
# print(tuple[1])
# print(tuple[-1])

#Ex 3: range of indexes

# tuple=("Apple",'Banana','cherry','Kiwi','Mango','lemon')
# print(tuple[2:5])
# print(tuple[-6:-2])

#ex 4: changing values  in tuple
# my_tuple=("Apple",'Banana','cherry','Kiwi','Mango','lemon')
# my_list=list(my_tuple)
# my_list[0]="cherry"
# my_tuple=tuple(my_list)
# print(my_tuple)

#ex 5: reading tuple using for loop
# my_tuple=("Apple",'Banana','cherry','Kiwi','Mango','lemon')
# for i in my_tuple:
#     print(i)

#ex 6: check if a item exists in tuple or not

# my_tuple=("Apple",'Banana','cherry','Kiwi','mango','lemon')
#
# if "mango" in my_tuple:
#     print("Fruit exists")
# else:
#     print("Fruit not exists")


#Ex 7: Tuple length
# my_tuple=("Apple",'Banana','cherry','Kiwi','Mango','lemon')
# print(len(my_tuple))

#Ex 8 adding items into tuple:not possible

# Ex 9: copying from tuple to another:

# my_tuple=("Apple",'Banana','cherry','Kiwi','Mango','lemon')
# my_tuple1=tuple(my_tuple)
# print(my_tuple1)

#Ex 10: removing items
# my_tuple=("Apple",'Banana','cherry','Kiwi','Mango','lemon')
# #my_tuple.remove("Apple")
# del my_tuple
# print(my_tuple)

# Ex 11: join/combine tuple

# tuple1=(11,1,13)
# tuple2=('a','b','c')
# tuple3=tuple1+tuple2
# print(tuple3)


#ex 12:equal or not
tuple1=(11,1,13)
tuple2=(11,1,13)
if tuple1==tuple2:
    print("equal")
else:
    print("not equal")