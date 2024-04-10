# text_encryptor/views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import EncryptedText

def encrypt_view(request):
    if request.method == 'POST':
        text_to_encrypt = request.POST.get('text', '')
        encrypted_text = caesar_cipher_encrypt(text_to_encrypt)
        EncryptedText.objects.create(text=text_to_encrypt, encrypted_text=encrypted_text)
        return redirect('encrypt')

    texts = EncryptedText.objects.all()
    return render(request, 'text_encryptor/home.html', {'texts': texts})

def decrypt_view(request):
    if request.method == 'POST':
        text_to_decrypt = request.POST.get('text', '')
        decrypted_text = caesar_cipher_decrypt(text_to_decrypt)
        EncryptedText.objects.create(text=decrypted_text, decrypted_text=text_to_decrypt)
        return redirect('decrypt')

    texts = EncryptedText.objects.all()
    return render(request, 'text_encryptor/home.html', {'texts': texts})

def clear_history_view(request):
    if request.method == 'POST' and request.POST.get('clear_history', '') == 'true':
        type_to_clear = request.POST.get('type', '')
        if type_to_clear == 'encryption':
            EncryptedText.objects.filter(encrypted_text__isnull=False).delete()
        elif type_to_clear == 'decryption':
            EncryptedText.objects.filter(decrypted_text__isnull=False).delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})

def caesar_cipher_encrypt(text, shift=3):
    result = ''
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                result += chr((shifted - 97) % 26 + 97)
            else:
                result += chr((shifted - 65) % 26 + 65)
        else:
            result += char
    return result

def caesar_cipher_decrypt(text, shift=3):
    result = ''
    for char in text:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                result += chr((shifted - 97) % 26 + 97)
            else:
                result += chr((shifted - 65) % 26 + 65)
        else:
            result += char
    return result
