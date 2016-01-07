from bs4 import BeautifulSoup
from datetime import datetime

#file=open('Short_test.xls')
file=open('NRI_lafs_lookup.xls')
accounts = []

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
  
  location = elements[0]
  account = elements[1]
  fund = elements[2]
  sub = elements[3]
  begin = elements[4]
  end = elements[5]

  if account not in accounts:
    print('making new account')
    accounts.append(account)
    funds = []

  if fund not in funds:
    print('making new fund')
    funds.append(fund)

  end_date = (datetime(int(end[:4]), int(end[4:6]), int(end[-2:])))
  if(end_date > datetime.now()):
    print(elements[:6])

# Loc,Account,Fund,Sub,Lafs Begin Date,Lafs End Date,Lafs Open Trans Flag,Fin Department Code,Cp4 Code,Cp3 Code,Cp2 Code,Cp1 Code,Account Title,Fund Title,Laf Title,Prin Invest Last Name,Sponsor Desc,Fiscal Year,Overhead base code,Overhead base desc,Overhead rate
