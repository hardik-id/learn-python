print("Start of the script")


try:
    print("Try block.")
    raise NameError("Something wrong here.")
except NameError:
    print("Name Error")
except:
    print("Except block.")
else:
    print("Else block.")
finally: 
    print("Finally block.")
    
    
    
# Reference https://docs.python.org/3.8/tutorial/errors.html
# custom error class