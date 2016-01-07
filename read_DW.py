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
# print(elements[1])
  location = elements[1]
  account = elements[2]
  fund = elements[3]
  sub = elements[4]
  begin_date = elements[5]
  end_date = elements[6]
  print(elements[1:6])

# Loc,Account,Fund,Sub,Lafs Begin Date,Lafs End Date,Lafs Open Trans Flag,Fin Department Code,Cp4 Code,Cp3 Code,Cp2 Code,Cp1 Code,Account Title,Fund Title,Laf Title,Prin Invest Last Name,Sponsor Desc,Fiscal Year,Overhead base code,Overhead base desc,Overhead rate
