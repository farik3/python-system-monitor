account = {
    "name": "Ильяс",
    "balance": 500000
}

def deposit(account, amount):
    if amount <= 0:
        print("Введите корректную сумму.")
        
    else:
        account["balance"] = account["balance"] + amount
        
def get_name(account):
    return account["name"]
        
def get_balance(account):
    return account["balance"]

def withdraw(account, amount):
    if amount <= 0:
        print("Введите сумму больше нуля.")
        
    elif amount <= account["balance"]:
            account["balance"] = account["balance"] - amount
    
    else:
        print("На вашем счету не достаточно средств.")
        
while True: 
       
    print("====== БАНК ======")
    print("1 Показать баланс: ")
    print("2 Пополнить баланс: ")
    print("3 Снаять деньги: ")
    print("4 Выйти: ")
    print("==================")

    choice = int(input("Выберети пункт: "))

    if choice == 1:
        name = get_name(account)
        balance = get_balance(account)
        print("Владелец: ", name)
        print("Баланс:", balance)

    elif choice == 2:
        amount = int(input("Введите сумму пополнения: "))
        deposit(account, amount)
        print("Ваш депозит составляет:", account["balance"])

    elif choice == 3:
        amount = int(input("Введите сумму для снятия: "))
        withdraw(account, amount)
        print("Остаток на вашес счету:", account["balance"])
        
    elif choice == 4:
        print("До свидания.")
        break

    else:
        print("Неверный пункт.")
    
