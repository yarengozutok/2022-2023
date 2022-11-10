from bs4 import BeautifulSoup
import urllib.request

dataGet = "https://creativecommons.org.tr/"

webSite = urllib.request.urlopen(dataGet)
getBytes = webSite.read()
webPage = getBytes.decode("utf8")
webSite.close()
soup = BeautifulSoup(webPage, 'html.parser')

print(soup.get_text() [ :100])
#proje için get url kısmında data write bölümünde soup title content yerine text 200 desek her bir sayfaya gidip karakteri indirecek.
#print(soup.find_all("a"))


