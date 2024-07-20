from django import forms
from .models import Account

class TransferForm(forms.Form):
    from_account = forms.ModelChoiceField(queryset=Account.objects.all())
    to_account = forms.ModelChoiceField(queryset=Account.objects.all())
    amount = forms.DecimalField(max_digits=15, decimal_places=2)

class UploadFileForm(forms.Form):
    file = forms.FileField()
