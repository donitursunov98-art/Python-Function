def is_even(number):
    return number % 2 == 0

def print_even_message(number):
    if is_even(number):
        print(f'{number} juft son.')
    else:
        print(f'{number} toq son.')


son = int(input('Sonni kiriting: '))
print_even_message(son)
