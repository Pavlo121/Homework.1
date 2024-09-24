total_expense = 0

def add_expense(amount):
    global total_expense
    total_expense += amount
    print(f"Витрати додані: {amount} грн")


def get_expense():
    return total_expense


def expense_tracker():
    while True:
        print("\nМеню:")
        print("1. Додати витрати")
        print("2. Переглянути загальну суму витрат")
        print("3. Вийти")

        choice = input("Виберіть опцію (1,2,3): ")

        if choice == '1':
            try:
                amount = float(input("Введіть суму витрат: "))
                add_expense(amount)
            except ValueError:
                print("Помилка! Введіть коректну числову суму.")
        elif choice == '2':
            print(f"Загальна сума витрат: {get_expense()} грн")
        elif choice == '3':
            print("Програма завершена.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


expense_tracker()
