def calculate_bmi(weight: float, height: float):
    return weight / (height ** 2)

def bmi_status(bmi: float):
    if bmi < 18.5:
        return 'Underweight'
    elif bmi < 25:
        return 'Normal'
    elif bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'

weight = float(input('Og\'irlik (kg): '))
height = float(input('Bo\'y (m): '))
bmi = calculate_bmi(weight, height)
print(f'BMI: {bmi:.2f}')
print(f'Holati: {bmi_status(bmi)}')
