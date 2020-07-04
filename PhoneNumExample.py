def isPhoneNumber(text):
    if len(text)!=12:
        return False    #not phone number-sized
    for i in range(0,3):
        if not text[i].isdecimal():
            return False #no area code
    if text[3]!='-':
        return False    #missing dash
    for i in range(4,7):
        if not text[i].isdecimal():
            return False #no first 3 digits
    if text[7]!='-':
        return False    #missing second dash
    for i in range(8,12):
        if not text[i].isdecimal():
            return False #missing last 4 digits
    return True

message='call me 416-357-3255 tomorrow, or at 416-333-3467 at office line'
foundNumber=False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print("phone number found: " +chunk)
        foundNumber = True
if not foundNumber:
              print("Could not find any phone numbers.")
              
              

print(isPhoneNumber('416-333-4444'))
