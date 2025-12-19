def check_guess(secret, guess):
    return secret == guess

def print_result(is_correct):
    if is_correct:
        print('To\'g\'ri! Siz sirli sonni topdingiz')
    else:
        print('Xato! Qayta urinib ko\'ring')    
sirli_son = 7
taxmin = int(input('Sirli sonni taxmin qiling: '))        

natija = check_guess(sirli_son, taxmin)
print_result(natija)