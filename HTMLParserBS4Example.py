import bs4, requests

def getUrlAuthor(nameUrl):
    res=requests.get(nameUrl)
    res.raise_for_status()

    soup=bs4.BeautifulSoup(res.text, 'html.parser')
    elems= soup.select('body > table > tbody > tr > td:nth-child(2) > p:nth-child(8) > a:nth-child(4)')
    return elems[0].text.strip() #listindexoutofrange #lesson40 in videos

name= getUrlAuthor('http://dr-chuck.com/')
print('the author\'s name is '+name)
