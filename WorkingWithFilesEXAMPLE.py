#working with files and filepaths:
#relative and absolute file paths
import os #os is used for working on OS folders

#2 days to write paths

#or
os.path.join('folder1','folder2','folder3','filename.png')
#to CHECK CURRENT working directory
os.getcwd()
#to CHANGE working directory
os.chdir('c:\\') #you use \\ because its a string or u can use rawstring and only need one \
# for example: r'c:\spam\eggs.png'

#to SEE ABSOLUTE PATH
os.path.abspath('filename.png')
#To CHECK Absolute path is True or False (Relative)
os.path.isabs('..\\..\\filename.png')
#To CHECK Relative path
os.path.relpath('c:\\folder1\\folder2\\spam.png',os.getcwd())
#outputs relative folder path to get there from current working directory (os.getcwd())

#to see directory name spam.png
os.path.dirname('c:\\folder1\\folder2\\spam.png')
#to see base name
os.path.basename('c:\\folder1\\folder2')
#to check if a file EXISTS
os.path.exists('c:\\windows\\system32\\calc.exe')
#to check IF ITS a FILE
os.path.isfile('c:\\windows\\system32\\calc.exe')
#to check IF ITS a DIRECTORY
os.path.isdir('c:\\windows\\system32')
#Get FILE SIZE
os.path.getsize('c:\\windows\\system32\\calc.exe')
#LIST files in directory
os.listdir('C:\\Users\\stars\\MyPythonScripts')

#Making directories (wallnut''waffles')
os.makedirs('C:\\Users\\stars\\MyPythonScripts\\madeadirectoryforexample\\walnut''waffles')
