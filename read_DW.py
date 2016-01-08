import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bill.settings")
import django
django.setup()

from budget.models import Account,Fund,Project, Sub
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

  end_date = (datetime(int(end[:4]), int(end[4:6]), int(end[-2:])))

  if(end_date > datetime.now()):
# print(elements[:6])

    if account not in accounts:
        print('Creating new account: ', account)
        accounts.append(account)
        a = Account.objects.create(**{'label':account})
        funds = []

    if fund not in funds:
        print('  Creating new fund', fund)
        f = Fund.objects.create(**{'label':fund, 'account':a})
        funds.append(fund)

    print('   Creating Sub ', sub)
    Sub.objects.create(**{'label':sub, 'fund':f})
