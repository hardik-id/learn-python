import os
import time

print(os.getcwd())
os.chdir('D:/projects')
print("Directory changed to: ", os.getcwd())
print("------------------------")

print(os.listdir())

# os.rename(
#     list(
#         filter(
#             lambda x: str(x).startswith('Rename'),
#             os.listdir())
#          ).pop(),
#     'Rename_'+str(time.time())
#     )

os.rename(
    [x for x in os.listdir() if str(x).startswith('Rename')]
    .pop(),
    'Rename_'+str(time.time())
    )

for f in os.listdir():
    print(f)
    
    
    