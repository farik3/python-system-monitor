#names = []

#count = int(input("Сколько имён вы хотели ввести? "))

#for i in range(count):
#    name = input("Введите имя: ")
#    names.append(name)
#    print("Вы ввели:", ",".join(names))

#for name in names:
#    print("Привет,", name + "!")

history = [
    "Пополнение: +50000",
    "Снятие: -20000",
    "Пополнение: +100000"
]

for operation in history:
    print(operation)