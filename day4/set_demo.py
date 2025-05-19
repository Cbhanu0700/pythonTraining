# Ex 1: Creating a set:

# my_set={"apple","Banana","Orange"}
# print(my_set)


#Ex 2: accessing items from set
# my_set={"apple","Banana","Orange"}
# for i in my_set:
#     print(i)

#Ex 3: value exists in set or not
# my_set={"apple","Banana","Orange"}
# print("apple" in my_set)
# print("apple1" in my_set)

#Ex 4: adding items to set
# my_set={"apple","Banana","Orange"}
# my_set.add("Guava")
# print(my_set)
# my_set.update(["Kiwi","Cherry"])
# print(my_set)

#Ex 5: length of the set
#
# set={"Apple",'Banana','cherry','Kiwi','Mango','lemon'}
# print(len(set))

#Ex 6: remove item from set
# set={"Apple",'Banana','cherry','Kiwi','Mango','lemon'}
# set.remove("Apple")
# print(set)
# set.discard("Kiwi")
# print(set)


#ex7: clear all items in set and clear set
# set={"Apple",'Banana','cherry','Kiwi','Mango','lemon'}
# set.clear()
# print(set)
# del set
# print(set)


#ex 8: joining two sets
set={"Apple",'Banana','cherry','Kiwi','Mango','lemon'}
set_1={1,2,3}
set3=set_1.union(set)
print(set3)


set={"Apple",'Banana','cherry','Kiwi','Mango','lemon'}
set_1={1,2,3}
set_1.update(set)
print(set3)