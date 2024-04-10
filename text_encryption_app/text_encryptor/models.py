from django.db import models

class EncryptedText(models.Model):
    text = models.TextField()
    encrypted_text = models.TextField()
    decrypted_text = models.TextField()
