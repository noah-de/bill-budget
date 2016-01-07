#!/Users/ncs/envs/bill-budget/bin/python

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bill.settings")
import django
django.setup()

from budget.models import Account,Fund,Project, Sub
print('projects count:', Project.objects.count())

print ('hello')
