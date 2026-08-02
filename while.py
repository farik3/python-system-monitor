total = 0

while True:
    command = input("Введите число или stop: ")

    if command == "stop":
        break

    num = int(command)

    total += num   # ← сумма ВСЕХ чисел

    if num % 2 == 0:
        print(num)

print(total)