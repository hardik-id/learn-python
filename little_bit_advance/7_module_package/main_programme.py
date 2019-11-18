from my_module import module_func

print("Print from main programme")

module_func()



## Another way:
import my_module 
print("Print from main programme")
my_module.module_func()




### Parent and Child module
from parent_package.child_package import child_module

print(child_module.list1)