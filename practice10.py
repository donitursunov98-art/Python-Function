def is_strong_password(password: str):
    if len(password) > 8:
        return 'Parol kuchli'
    else:
        return 'Parol kuchsiz'    

password = input('password: ')        
print(is_strong_password(password ))