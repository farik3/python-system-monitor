account = {
    "name": "Ильяс",
    "balance": 500000
}

def deposit(account, amount):
    if amount <= 0:
        print("Введите корректную сумму.")
        return False
        
    else:
        account["balance"] = account["balance"] + amount
        return True
        
def get_amount():
    try:
        amount = int(input("Введите сумму: "))
        return amount
    except ValueError:
        print("Введите сумму числом.")
        return None   
        
def get_name(account):
    return account["name"]
        
def get_balance(account):
    return account["balance"]

def withdraw(account, amount):
    if amount <= 0:
        print("Введите сумму больше нуля.")
        return False
        
    elif amount <= account["balance"]:
        account["balance"] = account["balance"] - amount
        return True
    
    else:
        print("На вашем счету не достаточно средств.")
        return False

history = []
        
while True: 
       
    print("====== БАНК ======")
    print("1 Показать баланс: ")
    print("2 Пополнить баланс: ")
    print("3 Снаять деньги: ")
    print("4 История операций: ")
    print("5 Выйти: ")
    print("==================")


    try:
        choice = int(input("Выберети пункт: "))
        
    except ValueError:
        print("Введите число от 1 до 5.")
        continue

    if choice == 1:
        name = get_name(account)
        balance = get_balance(account)
        print("Владелец: ", name)
        print("Баланс:", balance)

    elif choice == 2:
        amount = get_amount()

        if amount is not None:
            success = deposit(account, amount)
            if success:
                history.append(f"Пополнение: + {amount}")
                print("Баланс успешно пополнен.")
                print("Новый баланс:", account["balance"])

    elif choice == 3:
        amount = get_amount()
            
        if amount is not None:
            success = withdraw(account,amount)
            if success:
                history.append(f"Снятие: -{amount}")
                print("Деньги успешно сняты.")
                print("Остаток:", account["balance"])
                
    elif choice == 4:
        if not history:
            print("Совершите хотя-бы одну операццию")
            
        else:    
            for operation in history:
                print(operation)
                        
    elif choice == 5:
        print("До свидания.")
        break

    else:
        print("Неверный пункт.")
    
