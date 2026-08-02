import tkinter as tk
from tkinter import messagebox, filedialog
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from openpyxl import Workbook
import time
import datetime

# Глобальные данные
results = []
js_errors = []

# Основная логика проверки сайта
def test_site():
    global results, js_errors
    results.clear()
    js_errors.clear()

    url = entry_url.get()
    if not url.startswith("http"):
        url = "https://" + url

    try:
        # Запуск браузера
        service = Service("F:/Pyapp/chromedriver-win64/chromedriver.exe")  # Укажи путь, если chromedriver не в папке скрипта
        driver = webdriver.Chrome(service=service)

        driver.get(url)
        time.sleep(3)

        # Заголовок
        results.append(("Заголовок страницы", driver.title))

        # Элементы
        try:
            buttons = driver.find_elements(By.TAG_NAME, "button")
            results.append(("Кнопки", len(buttons)))
        except:
            results.append(("Кнопки", "Ошибка"))

        try:
            inputs = driver.find_elements(By.TAG_NAME, "input")
            results.append(("Поля ввода", len(inputs)))
        except:
            results.append(("Поля ввода", "Ошибка"))

        try:
            forms = driver.find_elements(By.TAG_NAME, "form")
            results.append(("Формы", len(forms)))
        except:
            results.append(("Формы", "Ошибка"))

        try:
            links = driver.find_elements(By.TAG_NAME, "a")
            results.append(("Ссылки", len(links)))
        except:
            results.append(("Ссылки", "Ошибка"))

        # JavaScript ошибки из консоли
        logs = driver.get_log("browser")
        for entry in logs:
            if entry["level"] == "SEVERE":
                js_errors.append(entry["message"])

        driver.quit()
        update_results()

    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось открыть сайт:\n{e}")

# Отображение результатов
def update_results():
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "🔍 Чек-лист:\n")
    for r in results:
        output_text.insert(tk.END, f"- {r[0]}: {r[1]}\n")

    if js_errors:
        output_text.insert(tk.END, "\n⚠️ JavaScript ошибки:\n")
        for e in js_errors:
            output_text.insert(tk.END, f"- {e}\n")
    else:
        output_text.insert(tk.END, "\n✅ JavaScript ошибок не найдено\n")

# Экспорт в Excel
def export_to_excel():
    if not results:
        messagebox.showinfo("Нет данных", "Сначала проверь сайт.")
        return

    filepath = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                            filetypes=[("Excel Files", "*.xlsx")])
    if not filepath:
        return

    wb = Workbook()
    ws = wb.active
    ws.title = "Чек-лист"

    ws.append(["Элемент", "Статус"])
    for row in results:
        ws.append(list(row))

    if js_errors:
        ws2 = wb.create_sheet("JS Ошибки")
        ws2.append(["Ошибка"])
        for e in js_errors:
            ws2.append([e])

    wb.save(filepath)
    messagebox.showinfo("Готово", "Данные сохранены в Excel.")

# GUI
root = tk.Tk()
root.title("АвтоТест сайта")

tk.Label(root, text="Введите ссылку на сайт:").pack(pady=5)
entry_url = tk.Entry(root, width=60)
entry_url.pack(padx=10)

tk.Button(root, text="▶ Проверить сайт", command=test_site).pack(pady=10)

output_text = tk.Text(root, height=25, width=90)
output_text.pack(padx=10, pady=10)

tk.Button(root, text="💾 Экспорт в Excel", command=export_to_excel).pack(pady=5)

root.mainloop()
