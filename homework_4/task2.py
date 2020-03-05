print('''Конвертер валют на Python
Підтримує долари(USD), євро(EUR) та гривні(UAH)
''')
try:
    amount = float(input("Яку сумму хочеш конвертувати?\nСумма - "))
except ValueError:
    print("Введена сума має бути числом.")
    exit()
try:
    currency = int(input("Яка це валюта? 1 - USD, 2 - EUR, 3 - UAH\nВалюта - "))
    if not 1 <= currency <= 3:
        raise ValueError("Ви ввели вхідну валюту, яка поки що не підтримується. ;)")
    choose_currency = int(input("У яку валюту перевести? 1 - USD, 2 - EUR, 3 - UAH\nПеревести у - "))
    if not 1 <= choose_currency <= 3:
        raise ValueError("Ви ввели вихідну валюту, яка поки що не підтримується. ;)")
except ValueError as e:
    print("Не можу обробити дані.", e)
    exit()

#тіло програми
if currency == 1 and choose_currency == 2:
    result = round()