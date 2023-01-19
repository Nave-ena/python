import os
path=input("folder path?")
isFile = os.path.isfile(path)
if(isFile==True):
    root_dir = path    
else:
     print("path not found")
for directory, subdirectories, files in os.walk(root_dir):
        for file in files:
            print(os.path.join(directory, file))