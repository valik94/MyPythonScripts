import os

os.getcwd()
os.chdir('c:\\users\\stars\\documents\\')
os.getcwd()

#opening file
helloFile = open('c:\\users\\stars\\documents\\hello.txt')
#reading contents and printing
content = helloFile.read()
print(content)

#OR same as above
helloFile = open('c:\\users\\stars\\documents\\hello.txt')
helloFile.readlines()

helloFile.close()

#Writing to File
helloFile = open('c:\\users\\stars\\documents\\hello.txt','w')
helloFile.write('Hello!!!!!!......\nbla bla bla...')
helloFile.close()

#appending to a file without overwriting to it
baconFile = open('bacon.txt','a')
baconFile.write('\n\nBacon is delicious.')
baconFile.write('\nThis document is about bacon being appended not overwritten using a for append')


#Using shelve file module for storing dictionary data, key value pairs
import shelve
shelfFile=shelve.open('mydata')
shelfFile['cats']=['Zophie','Pooka','Simon','Fat-tail','Cleo'] #cat names dictionary
shelfFile['cats']
 shelfFile.close()
#['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'cleo']
#this creates 3 files mydata.bak mydata.dat and mydata.dir

#also see
helfFile=shelve.open('mydata')
list(shelfFile.keys())
list(shelfFile.values())
