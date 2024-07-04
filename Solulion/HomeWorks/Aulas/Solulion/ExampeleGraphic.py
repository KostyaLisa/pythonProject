import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: деление на ноль невозможно!"
    return x / y

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "Сложение":
            result = add(num1, num2)
        elif operation == "Вычитание":
            result = subtract(num1, num2)
        elif operation == "Умножение":
            result = multiply(num1, num2)
        elif operation == "Деление":
            result = divide(num1, num2)

        result_label.config(text=f"Результат: {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите числовое значение.")

# Создание главного окна
root = tk.Tk()
root.title("Калькулятор")

# Создание и размещение виджетов
entry1 = tk.Entry(root, width=10)
entry1.grid(row=0, column=1, padx=10, pady=10)

entry2 = tk.Entry(root, width=10)
entry2.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Первое число:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="Второе число:").grid(row=1, column=0, padx=10, pady=10)

operation_var = tk.StringVar(root)
operation_var.set("Сложение") # Установить значение по умолчанию

operations_menu = tk.OptionMenu(root, operation_var, "Сложение", "Вычитание", "Умножение", "Деление")
operations_menu.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Операция:").grid(row=2, column=0, padx=10, pady=10)

calculate_button = tk.Button(root, text="Вычислить", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Результат:")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Запуск главного цикла событий
root.mainloop()
