import os

root_dir = 'python.py'

for directory, subdirectories, files in os.walk(root_dir):
    for file in files:
        print(os.path.join(directory, file))