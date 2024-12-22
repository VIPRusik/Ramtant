import hashlib

def check_requirements(password):
    #проверка полученного пароля на соответствие требованиям

    banned_chars = "абвгдеёжзийклмнопрстнфхцчшщъыьэюя"

    must_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    must_number = "1234567890"
    must_char = "_-+=*&?!%"

    must_check = []

    if 8 <= len(password) < 72:
        for letter in password:
            if letter == ' ':
                return False
            elif letter.lower() in banned_chars:
                return False
            else:
                if letter in must_letter:
                    must_check.append('letter')
                elif letter in must_number:
                    must_check.append('number')
                elif letter in must_char:
                    must_check.append('char')
    else:
        return False

    if ('letter' in must_check) and ('number' in must_check) and ('char' in must_check):
        return True
    else:
        return False

def hash(password):
    #функция создания хэша пароля с помощью sha256, чтобы потом хранить в базе данных

    return hashlib.sha256(password.encode()).hexdigest()