def deposit(balance, amount):
    balance += amount
    print(f'{amount} qo\'shildi. Yangi balans: {balance}')
    return balance

def withdraw(balance, amount):
    if amount > balance:
        print('Yetarli mablag\' yo\'q!')
    else:
        balance -= amount
        print(f'{amount} yechildi. Yangi balans: {balance}')
    return balance

def check_balance(balance):
    print(f'Sizning balansingiz: {balance}')

balance = 0.0

while True:
    amal = input('Amalni tanlang (deposit, withdraw, check, exit): ').lower()
    if amal == 'deposit':
        amount = float(input('Miqdor kiriting: '))
        balance = deposit(balance, amount)
    elif amal == 'withdraw':
        amount = float(input('Miqdor kiriting: '))
        balance = withdraw(balance, amount)
    elif amal == 'check':
        check_balance(balance)
    elif amal == 'exit':
        print('Dastur yakunlandi.')
        break
    else:
        print('Noto\'g\'ri amal!')
