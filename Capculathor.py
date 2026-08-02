
while True:
    calc_1 = int(input("Введите первое число: "))

    if calc_1 == 0:
        print("Програма завершена.")
        break


    x = input("Введите операцию (+, -, *, /): ")
    calc_2 = int(input("Введите второе число: "))



    if x == '+':
        print(f"Результат: {calc_1 + calc_2}")
    elif x == '-':
        print(f"Результат: {calc_1 - calc_2}")
    elif x == '*':
        print(f"Результат: {calc_1 * calc_2}")
    elif x == '/':
        if calc_2 == 0:
            print("На ноль делить нельзя!")
        else:
            print(f"Результат: {calc_1 / calc_2}")

    else:
        print("Неизвестная операция")

