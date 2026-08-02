names = []

count = int(input("Сколько имён вы хотели ввести? "))

for i in range(count):
    name = input("Введите имя: ")
    names.append(name)
    print("Вы ввели:", ",".join(names))

for name in names:
    print("Привет,", name + "!")