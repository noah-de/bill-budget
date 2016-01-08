from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator

class Account(models.Model):
  label = models.CharField(
    default='',
    blank=True,
    max_length = 6,)

  def __str__(self):
    return self.label

class Fund(models.Model):
  account = models.ForeignKey(Account, related_name='funds')
  label = models.CharField(
    default='',
    blank=True,
    max_length = 5,)

  def __str__(self):
    return self.label

class Sub(models.Model):
  fund= models.ForeignKey(Fund)
  label = models.CharField(
    default='',
    blank=True,
    max_length = 2,)

  def __str__(self):
    return self.label

class Project(models.Model):
  name = models.CharField(
    default = '',
    max_length = 6,)
  location = models.CharField(
    default='',
    max_length = 1,
    blank=True)
  fund = models.ForeignKey(Fund)

  def __str__(self):
    return self.name

