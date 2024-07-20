from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('import/', views.import_accounts, name='import_accounts'),
    path('', views.list_accounts, name='list_accounts'),
    path('transfer/', views.transfer_funds, name='transfer_funds'),
    path('<str:account_number>/', views.get_account, name='get_account'),
]