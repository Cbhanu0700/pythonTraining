#Approach 1
# import sys
# sys.path.append("C:/PythonProject/pythontraining/day7_module/pack1")
#
# import module1
# import module2
#
# module1.display()
# module2.show()


#Approach 2
# from module1 import display
# from module2 import show
#
# display1()
# show()

#Approach 3
# import pack1.module2
# import pack1.module1
#
# pack1.module2.show()
# pack1.module1.display()

#Approach 4
from pack1 import module1,module2
module1.display()
module2.show()
