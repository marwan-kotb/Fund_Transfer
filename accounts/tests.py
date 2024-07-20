from django.test import TestCase, Client
from django.urls import reverse
from .models import Account
from .forms import TransferForm, UploadFileForm
from django.core.files.uploadedfile import SimpleUploadedFile
import io

class AccountViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.account1 = Account.objects.create(account_number='123', account_name='Account1', balance=1000)
        self.account2 = Account.objects.create(account_number='456', account_name='Account2', balance=500)
    
    def test_import_accounts_view(self):
        csv_data = """ID,Name,Balance
                      789,Account3,3000
                      012,Account4,4000"""
        csv_file = SimpleUploadedFile('accounts.csv', csv_data.encode('utf-8'), content_type='text/csv')

        response = self.client.post(reverse('accounts:import_accounts'), {'file': csv_file})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Account.objects.count(), 4)

    def test_list_accounts_view(self):
        response = self.client.get(reverse('accounts:list_accounts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/list_accounts.html')
        self.assertContains(response, 'Account1')
        self.assertContains(response, 'Account2')

    def test_get_account_view(self):
        response = self.client.get(reverse('accounts:get_account', args=['123']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/account_details.html')
        self.assertContains(response, 'Account1')

    def test_transfer_funds_view(self):
        response = self.client.post(reverse('accounts:transfer_funds'), {
            'from_account': self.account1.id,
            'to_account': self.account2.id,
            'amount': 200
        })
        self.assertEqual(response.status_code, 302)
        self.account1.refresh_from_db()
        self.account2.refresh_from_db()
        self.assertEqual(self.account1.balance, 800)
        self.assertEqual(self.account2.balance, 700)

        # Test insufficient funds
        response = self.client.post(reverse('accounts:transfer_funds'), {
            'from_account': self.account2.id,
            'to_account': self.account1.id,
            'amount': 800
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Insufficient funds')

    def test_transfer_funds_view_get(self):
        response = self.client.get(reverse('accounts:transfer_funds'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/transfer_funds.html')

if __name__ == '__main__':
    
    import coverage
    import xmlrunner
    import unittest

    cov = coverage.Coverage()
    cov.start()

    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))

    cov.stop()
    cov.save()

    print("Coverage Report:")
    cov.report()
    cov.html_report(directory='coverage')
