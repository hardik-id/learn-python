print("This is main script")
from parent_package.child_package import child_module

def funct_in_main():
    print("Function in main script.")

print(child_module.list1)    
child_module.list1.append(10)
print(child_module.list1)    
    
if __name__ == "__main__":
    print("Script is running as python parent_module.py")