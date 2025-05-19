#Approach 1
# import sys
# sys.path.append("C:/PythonProject/pythontraining/day7_module/packagea")
# sys.path.append("C:/PythonProject/pythontraining/day7_module/packageb")
# import emp
# import stu
# obj=emp.Employee(1,"Bhanu",10000)
# obj.displayemp()
# stuobj=stu.student(2,"Prakash",20000)
# stuobj.displaystu()

#Approach 2

from emp import Employee
from stu import Student

obj = Employee(1, "Bhanu", 10000)
obj.displayemp()

stuobj = Student(2, "Prakash", 20000)
stuobj.displaystu()
