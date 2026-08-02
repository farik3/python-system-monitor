def check_age(age):
    if age <= 14:
        return "Ты школьник!"
    elif age <= 18:
        return "Ты подросток!"
    elif age <= 30:
        return "Молодой человек!"
    else:
        return "Ты взрослый!"

age = int(input("Сколько тебе лет? "))
result = check_age(age)
print(result)



