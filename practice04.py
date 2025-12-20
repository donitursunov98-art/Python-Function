def get_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 70 <= score <= 89:
        return 'B'
    elif 60 <= score <= 69:
        return 'C'
    elif 0 <= score <= 59:
        return 'F'
    else:
        return 'Bunaqa ball mavjud emas'


ball = int(input('Ballni kiriting: '))
print(get_grade(ball))
