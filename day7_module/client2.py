#Approach 1
# import sys
# sys.path.append("C:/PythonProject/pythontraining/day7_module/package1")
# sys.path.append("C:/PythonProject/pythontraining/day7_module/package1/package2")
# import module1
# import module2
# module1.display()
# module2.show()


#Approach 2

import sys
sys.path.append("C:/PythonProject/pythontraining/day7_module/package1")
sys.path.append("C:/PythonProject/pythontraining/day7_module/package1/package2")
from  module2 import *
from module1 import *

display()
show()