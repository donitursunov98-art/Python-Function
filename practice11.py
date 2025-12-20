def calculate_tax(salary: float):
    if salary > 5000000:
        tax = salary * 0.20
    else:
        tax = salary * 0.13
    return tax

def calculate_net_salary(salary: float):
    return salary - calculate_tax(salary)

salary = float(input('Maoshingizni kiriting: '))
print(f'Soliq: {calculate_tax(salary)}')
print(f'Net salary: {calculate_net_salary(salary)}')
