import re

#Groups
phoneNumRegex =re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo=phoneNumRegex.search('My number is 416-357-3255')
mo.group() #whole number
mo.group(1) #'416'
mo.group(2) #'357-3255'

#Pipe Character: OR = |
#Grouping using pipes |
batRegex=re.compile(r'Bat(man|mobile|copter|bat)')
mo=batRegex.search('Batmobile lost a wheel')
mo.group()
