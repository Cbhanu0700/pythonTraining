# Ex 1:
# mylist1=[12,13,14,15]
# mylist2=["apple","Banana","cherry"]
# mtlist3=["Bhanu",24,74000]
# mylist=list()
# print(mylist1)
# print(mylist2)
# print(mtlist3)
# print(mylist)


#Ex 2: Accessing items from list

# mylist=["apple","Banana","cherry"]
# print(mylist[2])
# print(mylist[-1])
# print(mylist[-2])

#Ex 3: range of indexes

# mylist=["Apple",'Banana','cherry','Kiwi','Mango','lemon']
# print(mylist[2:5])
# print(mylist[-5:-1])


#Ex 4:change item value
# mylist=["Apple",'Banana','cherry']
# print(mylist)
# mylist[0]='Orange'
# print(mylist)

#Ex 5:print each item from the list individually
# mylist=["Apple",'Banana','cherry']
# for i in mylist:
#     print(i)

#Ex 6: Check if item exists in list or not

# mylist=["Apple",'Banana','cherry','Kiwi','Mango','lemon']
# for i in mylist:
#     if(i=="did"):
#         print("Mango exists")
# print("fruit not exists")


# mylist=["Apple",'Banana','cherry','Kiwi','Mango','lemon']
# if "gum" in mylist:
#    print("apple exists")
# else:
#     print("Not exists")


#Ex 7: length of the list

# mylist=["Apple",'Banana','cherry','Kiwi','Mango','lemon']
# print(len(mylist))

# #ex 8: add items in list append() and insert()
# mylist=["Apple",'Banana','cherry']
# mylist.append("kiwi")
# print(mylist)
# mylist.insert(1,"guava")
# print(mylist)

#Ex 9:remove item from list pop()

# mylist=["Apple",'Banana','cherry','Kiwi','Mango','lemon']
# print(mylist)
# mylist.pop(0)
# print(mylist)
# del mylist[3]
# print(mylist)
# mylist.clear()
# print(mylist)

#Ex 10:copy
# mylist=["Apple",'Banana','cherry','Kiwi','Mango','lemon']
# mylist1=list(mylist)
# print(mylist)
# print(mylist1)
# mylist3=["Apple",'Banana','Mango','lemon']
# mylist4=mylist3.copy()
# print(mylist3)
# print(mylist4)

#ex 11:combine/join lists

list=["Apple",'Banana','Mango','lemon']
list1=["Kiwi",'Guava']
list3=list+list1
print(list3)

for i in list1:
    list3.append(i)
print(list3)


list1.extend(list)
print(list1)
