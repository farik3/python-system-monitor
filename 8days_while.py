
grades = []

while True:
    grade = int(input("Введите оценку (1-5, 0 - выход): "))

    if grade == 0:
        break
    elif 1 <= grade <= 5:
        grades.append(grade)
    else:
        print("Оценка должна быть от 1 до 5")

print(f"\n Всего оценок: {len(grades)}")

if grades:
    everage = sum(grades) / len(grades)
    print(f"Средняя оценка: {everage:.2f}")

    for i in range(1, 6):
        print(f"Оценка {i} встретилась {grades.count(i)} раз")

else:
    print("Оценок не было.")
