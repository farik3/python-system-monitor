# Вторая задача


def is_even(num):

    if num == 0:
        return "Выход"

    elif num % 2 == 0:
        print(f"Четное число: {num}")
    else:
        print(f"Нечетное число: {num}")

while True:
    num = int(input("Введите число 0 для выхода: "))
    result = is_even(num)
    if result == "Выход":
        break



        

