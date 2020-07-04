import re #regular expression module


#re.compile(r ---- r=rawstring, \d = digit
phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#search method will find the first match of phone number format 416-357-3255
matchObject = phoneNumRegex.search('call me 416-357-3255 tomorrow, or at 416-333-3467 at office line')
print(matchObject.group())
                         
#to find every occurance of the phone number use findall()
phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall('call me 416-357-3255 tomorrow, or at 416-333-3467 at office line'))
