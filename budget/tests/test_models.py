from django.test import TestCase
from django.core.exceptions import ValidationError


class AccountModelTest(TestCase):

  def test_cannot_create_account_with_bad_name(self):
    # A sleepy administrator forgets that accounts are 6 digits
    # fortunately, the system will not allow it
    False

  def test_cannot_create_duplicate_active_account(self):
    # On larger teams with less than ideal communication
    # duplicate entries are created
    False

  def test_can_create_duplicate_accounts_if_only_one_is_active(self):
    # Accounting will reuse accounts, so there must be the ability
    # to create duplicate accounts
    False
