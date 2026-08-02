numbers = []

while True:

    number = int(input("Введите числа от 1-9 или 0 для выхода: "))

    if number == 0:
        break
    elif 1 <= number <= 9:
        numbers.append(number)
    else:
        print(f"Число не должно превышать 9")


if numbers:
    print(f"\n Вы ввели: {numbers}")
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    print(f" Сумма: {total}")
    print(f" Среднее: {average:.2f}")
    print(f" Максимум: {maximum}")
    print(f" Минимум: {minimum}")

else:
    print("Вы не ввели ни одного числа.")


