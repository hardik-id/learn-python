x = 1

def print_x():
    print(x)

def local_x():
    # print(x)
    x = 2
    print(x)


    
def update_global_x():
    global x
    x = 3
    
print_x()
local_x()
print_x()
update_global_x()
print_x()
print(x)





# non local
print("\n\n## Non Local")
x = "Global"
def root():
    x = "X at root"
    def change_x():
        x = "This change will not happen."
    def change_x_non_local():
        nonlocal x
        x = "x at root changed"
    def change_x_global():
        global x
        x = "Global x changed"
    change_x()
    print(x)
    change_x_non_local()
    print(x)
    root.change_x_global = change_x_global
    return root
    
root()
print(x)
y = root()
y.change_x_global()
print(x)