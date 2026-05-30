import random
def validate_password(password):
    specsymbols = "!@#$%^&*()_+-=[]{}|;:,.<>?`"
    bigletterlist = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    smallletterlist = bigletterlist.lower()
    lengthtest = haslettertest = hasdigittest = hasspecialtest = hasuppertest = haslowertest = True
    if len(password) < 8:
        lengthtest=False
    atleastoneletter=False
    for i in password:
        if i.isalpha():
            atleastoneletter=True
            break
    if atleastoneletter==False:
        haslettertest=False
    atleastonedigit = False
    for i in password:
        if i.isdigit():
            atleastonedigit = True
            break
    if atleastonedigit==False:
        hasdigittest=False
    atleastonespec=False
    for i in password:
        if i in specsymbols:
            atleastonespec=True
            break
    if atleastonespec==False:
        hasspecialtest=False
    atleastonebig=False
    atleastonesmall=False
    for i in password:
        if i in bigletterlist:
            atleastonebig=True
        elif i in smallletterlist:
            atleastonesmall=True
        if (atleastonesmall and atleastonebig)==True:
            break
    if atleastonebig==False:
        hasuppertest=False
    if atleastonesmall==False:
        haslowertest=False
    if lengthtest and haslettertest and hasdigittest and hasspecialtest and hasuppertest and haslowertest:
        valide = True
    else:
        valide=False
    return (valide, {'length': lengthtest,
                    'has_letter': haslettertest,
                    'has_digit': hasdigittest,
                    'has_special': hasspecialtest,
                    'has_uppercase': hasuppertest,
                    'has_lowercase': haslowertest}
            )
"""
while True:
    passw = input("Введите пароль: ")
    results = validate_password(passw)
    print(f"Проверка пройдена: {results[0]}")
    for key, value in results[1].items():
        print(f"{key}: {value}")
    if results[0]==True:
        break
"""
def generate_password(length=12):
    specsymbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    uppercase = "ABCDEFGHJKLMNPQRSTUVWXYZ"
    smalletterlist = "abcdefghijkmnopqrstuvwxyz"
    digits="23456789"
    if length<8:
        return "Ошибка: длина должна составлять минимум 8 символов"
    while True:
        password = ''
        for symbol in range(length):
            capac = random.choice([specsymbols,uppercase,smalletterlist,digits])
            capacsymbol=random.choice(capac)
            password+=capacsymbol
        if validate_password(password)[0]:
            return password

#консольное приложение:
while True:
    print("Выберите действие:\n1 - Проверить пароль на валидность\n2 - Сгенерировать валидный пароль\n3 - Выйти")
    act=int(input())
    if act==1:
        passw = input("Введите пароль: ")
        results = validate_password(passw)
        print(f"Проверка пройдена: {results[0]}")
        for key, value in results[1].items():
            print(f"{key}: {value}")
    if act==2:
        length = int(input("Введите длину пароля (минимум 8): "))
        generated=generate_password(length)
        print(f"Сгенерированный пароль - {generated}")
    if act==3:
        break