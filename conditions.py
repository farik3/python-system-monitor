
days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

while True:
    day_of_the_week = int(input("Введите число: "))

    if day_of_the_week == 0:
        print("Программа завершена.")
        break
    elif 1 <= day_of_the_week <= 7:
        print(days[day_of_the_week - 1])

    else:
        print("Нет такого дня недели")