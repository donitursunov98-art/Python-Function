def check_answer(user_answer, correct_answer):
    if user_answer.lower() == correct_answer.lower():
        return True
    else:
        return False

def ask_question(question: str, correct_answer: str):
    user_answer = input(question + ' ')
    
    if check_answer(user_answer, correct_answer):
        print('To\‘g\‘ri')
    else:
        print('Noto\‘g\‘ri')

ask_question('O\'zbekiston poytaxti qaysi shahar: ', 'Toshkent')
