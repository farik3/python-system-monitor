age = int(input("Ведите возраст: "))
heals = input("Есть ли проблемы со здоровьем?  (да/нет): ")

if age >= 18 and age <= 27 and heals == "нет":
    print("Годен к службе")
else:
    print("Не годен или есть ограничения")