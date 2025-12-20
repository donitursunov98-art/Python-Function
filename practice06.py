def is_valid_phone_number(phone: str):
    if len(phone) == 9 and phone.isdigit():
        return True
    else:
        return False

phone = input('Phone: ')
print(is_valid_phone_number(phone))
