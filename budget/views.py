from django.views.generic import ListView
from django.shortcuts import render
from budget.models import Account, Fund, Sub, Project

def index(request):
  projects = Project.objects.all()
  accounts = Account.objects.all()
  context = { 'accounts': accounts, 'projects': projects }
  return render(request, 'home.html', context)

