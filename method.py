names = ["Ильяс", "Айдана", "Азамат", "алина", "Ирина", "иван", "ислам", "Батыр", "Камилла"]

a_name = []
i_name = []

for name in names:

    if name.lower().startswith("и"):
        i_name.append(name.lower())

    elif name.lower().startswith("а"):
        a_name.append(name.lower())


print(a_name)
print(i_name)

