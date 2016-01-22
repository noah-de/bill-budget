#!/Users/ncs/envs/bill-budget/bin/python

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bill.settings")
import django
django.setup()

from budget.models import Account,Fund,Project, Sub
print('projects count:', Project.objects.count())

import csv
with open('NRI_active_projects.txt', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
      print('project: ',row[0])
      """ 
      look up account
      does it have a matching fund?
      if so, create this project
      """
print ('hello')
