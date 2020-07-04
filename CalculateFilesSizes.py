import os
#This program calculates the total size of all files in a given path directory (i.e.in a given folder)

totalSize=0
for filename in os.listdir('C:\\Users\\stars\\MyPythonScripts'):
    if not os.path.isfile(os.path.join('C:\\Users\\stars\\MyPythonScripts',filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Users\\stars\\MyPythonScripts',filename))

totalSize
