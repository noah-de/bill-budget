from django.db import models

class Project(models.Model):
  name = models.TextField(default = '')

  def __str__(self):
    return self.name
