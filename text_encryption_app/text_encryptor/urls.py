# text_encryptor/urls.py

from django.urls import path
from .views import encrypt_view, decrypt_view, clear_history_view

urlpatterns = [
    path('', encrypt_view, name='encrypt'),
    path('decrypt/', decrypt_view, name='decrypt'),
    path('clear_history/', clear_history_view, name='clear_history'),
]
