from bs4 import BeautifulSoup

file=open('NRI_lafs_lookup.xls')

soup=BeautifulSoup(file, 'html.parser')
table = soup.find('table')
rows = table.findAll('tr')
for tr in rows:
  cols = tr.findAll('td')
  text = ''
  for td in cols:
       text+=td.get_text()+':::'
 
  string = text.replace(u'\xa0', u'')
  elements = string.split(':::')
  print(elements[1])
