#This program gets text of a word file and displays it as it's inside the word file


import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText=[]
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

print(getText('c:\\users\\stars\\desktop\\demo.docx'))
