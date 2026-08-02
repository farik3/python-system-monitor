names = []

count = int(input("Сколько имён вы хотите ввести? "))

for i in range(count):
    name = input(f"Введите имя: {i + 1}: ")
    names.append(name)

print(f"\nВы ввели имя { ', ' .join(names)}\n")

for name in names:
    print(f"Привет,  {name}!")