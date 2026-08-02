grades = {
    "Математика": 4,
    "Русский язык": 5,
    "История": 3
}

grades["Физика"] = 4
grades["Математика"] = 5
del grades["История"]

for subject, grade in grades.items():
    print(f"{subject}: {grade}")
