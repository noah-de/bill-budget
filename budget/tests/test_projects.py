#from .base import FunctionalTest
from django.test import TestCase, LiveServerTestCase, Client
from django.core.exceptions import ValidationError
from budget.models import Project

class ProjectModelTest(TestCase):

  def test_project_creation(self):
    ''' Projects are the primary unit of gus
    users will need to create projects
    '''
    self.assertEqual(Project.objects.all().count(), 0)
    project = Project()
    project.name = "sdn32"
    project.save()
    project.full_clean()
    self.assertEqual(Project.objects.all().count(), 1)
