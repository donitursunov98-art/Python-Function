def is_palindrome(text: str):
    cleaned = text.replace(' ', '').lower()
    return cleaned == cleaned[::-1]

text = input('So\'z kiriting: ')
if is_palindrome(text):
    print('Palindrome')
else:
    print('Palindrome emas')
