import csv
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Account
from .forms import TransferForm, UploadFileForm

import csv
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Account
from .forms import UploadFileForm

def import_accounts(request):
    if request.method == "POST" and request.FILES.get('file'):
        csv_file = request.FILES['file']

        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        
        for row in reader:
            account_number = row['ID']
            account_name = row['Name']
            balance = row['Balance']
            Account.objects.create(account_number=account_number, account_name=account_name, balance=balance
            )

        return HttpResponseRedirect(reverse('accounts:list_accounts'))
    
    return render(request, 'accounts/import_accounts.html', {'form': UploadFileForm()})


def list_accounts(request):
    accounts = Account.objects.all()
    return render(request, 'accounts/list_accounts.html', {'accounts': accounts})

def get_account(request, account_number):
    account = get_object_or_404(Account, account_number=account_number)
    return render(request, 'accounts/account_details.html', {'account': account})

def transfer_funds(request):
    if request.method == "POST":
        form = TransferForm(request.POST)
        if form.is_valid():
            from_account = form.cleaned_data['from_account']
            to_account = form.cleaned_data['to_account']
            amount = form.cleaned_data['amount']
            if from_account.balance >= amount:
                from_account.balance -= amount
                to_account.balance += amount
                from_account.save()
                to_account.save()
                return HttpResponseRedirect(reverse('accounts:list_accounts'))
            else:
                return HttpResponse("Insufficient funds")
    else:
        form = TransferForm()
    return render(request, 'accounts/transfer_funds.html', {'form': form})
