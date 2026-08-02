names = ["Ильяс", "Айдана", "Азамат", "алина", "Ирина", "иван", "ислам", "Ася", "Арман", "Али"]
short_names = []

for name in names:
    if name.lower().startswith("а") and len(name) <= 5:
        short_names.append(name.lower())

print(short_names)
