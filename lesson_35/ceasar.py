# Функция шифрования
def cipher_encrypt(plain_text, key):
    encrypted = ""
    for c in plain_text:
        if c.isupper(): #проверить, является ли символ прописным
            c_index = ord(c) - ord('A')
            # сдвиг текущего символа на позицию key
            c_shifted = (c_index + key) % 26 + ord('A')
            c_new = chr(c_shifted)
            encrypted += c_new
        elif c.islower(): #проверка наличия символа в нижнем регистре
            # вычесть юникод 'a', чтобы получить индекс в диапазоне [0-25)
            c_index = ord(c) - ord('a')
            c_shifted = (c_index + key) % 26 + ord('a')
            c_new = chr(c_shifted)
            encrypted += c_new
        elif c.isdigit():
            # если это число, сдвинуть его фактическое значение
            c_new = (int(c) + key) % 10
            encrypted += str(c_new)
        else:
            # если нет ни алфавита, ни числа, оставьте все как есть
            encrypted += c
    return encrypted
# Функция дешифрования
def cipher_decrypt(ciphertext, key):
    decrypted = ""
    for c in ciphertext:
        if c.isupper():
            c_index = ord(c) - ord('A')
            # sсдвинуть текущий символ влево на позицию клавиши, чтобы получить его исходное положение
            c_og_pos = (c_index - key) % 26 + ord('A')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.islower():
            c_index = ord(c) - ord('a')
            c_og_pos = (c_index - key) % 26 + ord('a')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.isdigit():
            # если это число, сдвиньте его фактическое значение
            c_og = (int(c) - key) % 10
            decrypted += str(c_og)
        else:
            # если нет ни алфавита, ни числа, оставьте все как есть
            decrypted += c
    return decrypted