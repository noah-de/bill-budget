#!/Users/ncs/envs/bill-budget/bin/python

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bill.settings")
import django
django.setup()

from budget.models import Account,Fund,Project, Sub
print('projects count:', Project.objects.count(),"\n")

def error(string, nums):
  print(" ERROR [",string,'-', nums,']')

import csv
with open('NRI_active_projects.txt', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
      a = Account.objects.filter(label=row[1])
      if(a.count() == 1):
        """ account exists """
        acc= a.last()
        f = acc.funds.filter(label=str(row[2].zfill(5)))

        if(f.count() == 1):
          """ fund exists """
          """ MAKE the project """
          p = Project()
          p.fund=f
          p.name="sdn32"
          p.full_clean()
          p.save()
        else:
          error("["+row[0]+"] fund("+row[2]+") does not exist on the account ("+row[1]+")" ,f.count())

      else:
        """ account does not exist"""
        error("account ("+row[2]+")",a.count())

#        print(row[4], ' ', row[1],'-',row[2].zfill(5), ' ', row[0], sep='')


      """ 
      look up account
      does it have a matching fund?
      if so, create this project
      """

print('projects count:', Project.objects.count(),"\n")
