import re
batRegex=re.compile((r'Batman|Batwoman')
#Same thing as
batRegex=re.compile(r'Bat(wo)?man')
mo=batRegex.search('The Adventures of Batman')
mo.group() #'Batman'
mo=batRegex.search('The Adventures of Batwoman')
mo.group() #'Batwoman'
phoneRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=phoneRegex.search('my phone number is 416-355-5782. call me tmr.')
phoneRegex=re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
phoneRegex.search('my phone number is 416-367-3267') #...match=416-367-3267
phoneRegex.search('my phone number is 367-3267' #...match=367-3267
# Therefore, the ? means 0 or 1 times (optioal) in Regular Expressions

# also * means match (0 or more) times
batRegex=re.compile(r'Bat(wo)*man')
mo=batRegex.search('The Adventures of Batwoman')
mo.group()
mo=batRegex.search('The Adventures of Batwowowowowowoman')
mo.group()

# + means (one or more)
batRegex=re.compile(r'Bat(wo)+man')
regex=re.compile(r'\+\*\?')
regex.search('I learned about+*? regex syntax')
#several number of matches (3)
haRegex=re.compile(r'(Ha){3}')
haRegex.search('He said "HaHaHa')

#several number of matches (3 to 6)
haRegex=re.compile(r'(Ha){3,6}')
haRegex.search('He said "HaHaHaHaHa')
                

#matching phone number 3 times, optionally area code (\d\d\d)? and optionally seperated by comma (,)?)
phoneRegex=re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?) {3}')
phoneRegex.search('My numbers are 416-367-3267,444-5723,222-124-6746') #Match = '416-367-3267,444-5723,222-124-6746'
                  
#Greedy match - matching longest possible string)
digitRegex=re.compile(r'(\d){3,5}')
digitRegex.search('1234567890')

#NON Greedy match - matching shortest match using ?
digitRegex=re.compile(r'(\d){3,5}?')
digitRegex.search('1234567890')
