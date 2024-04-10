def encrypt(text, shift=3):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(encrypted_text, shift=3):
    return encrypt(encrypted_text, shift=-shift)
