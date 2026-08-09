books = [
    "Гарри Поттер",
    "1984",
    "Мастер и Маргарита"
]


while True:    

    print("====== БИБЛИОТЕКА ======")
    print("1. Показать книги")
    print("2. Добавить книгу")
    print("3. Удалить книгу")
    print("4. Найти книгу")
    print("5. Выйти")
    print("========================")

    try:
        choice = int(input("Выберети пункт: "))
        
    except ValueError:
        print("Введите число от 1 до 5.")
        continue
    
    if choice == 1: # Выводим список книг
        print("Каталог книг:")
        if not books:
                print("Библиотека пуста.")
        else:
            for book in books:    
                print(book)
    
    elif choice == 2: # Добавляем книгу
        print("Какую книгу хотите добавить?")
        book = input("Введите название книги: ").strip().lower()
        if book in books:
            print("Такая книга есть в списке.")
            
        else:
            books.append(book)
            print(f"Книга {book} добавлена в список.")
                
    elif choice == 3: # Удаляем книгу
        print("Какую книгу хотите удалить?")
        del_book = input("Введите название книги которую вы хотите удалить: ").strip().lower()
        if del_book in books:
            books.remove(del_book)
            print(f"Книга {del_book} удалена из списка")
        else:
            print("Такой книги нет.")
        
    elif choice == 4: # Поиск книги
        search_book = input("Поиск книги: ").strip().lower()
        found_book = None
        for book in books:
            if search_book in book.lower():
                found_book = book
                print(f"Найдена книга: {found_book}")
                break
        else:
            print("Такой книги нет.")
        
    elif choice == 5: # Выходим из программы
        print("Пока.")
        break
    else:
        print("Неверный пункт.")