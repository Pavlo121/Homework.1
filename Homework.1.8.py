def create_user_settings():
    settings = {
        'theme': 'light',
        'language': 'en',
        'notifications': True
    }

    def user_settings(action, key=None, value=None):
        if action == 'get':
            return settings.get(key, 'Налаштування не знайдено')
        elif action == 'set':
            settings[key] = value
            print(f"Налаштування '{key}' змінено на '{value}'")
        elif action == 'view':
            return settings
        else:
            return "Невідома дія!"

    return user_settings


settings_manager = create_user_settings()


def settings_interface():
    while True:
        print("\nМеню:")
        print("1. Переглянути всі налаштування")
        print("2. Отримати певне налаштування")
        print("3. Змінити налаштування")
        print("4. Вийти")

        choice = input("Виберіть опцію (1/2/3/4): ")

        if choice == '1':
            current_settings = settings_manager('view')
            print(f"Поточні налаштування: {current_settings}")
        elif choice == '2':
            key = input("Введіть назву налаштування (theme, language, notifications): ")
            value = settings_manager('get', key)
            print(f"Значення '{key}': {value}")
        elif choice == '3':
            key = input("Введіть назву налаштування (theme, language, notifications): ")
            if key in ['theme', 'language', 'notifications']:
                if key == 'notifications':
                    value = input("Введіть нове значення (True/False): ") == 'True'
                else:
                    value = input(f"Введіть нове значення для '{key}': ")
                settings_manager('set', key, value)
            else:
                print("Невідоме налаштування!")
        elif choice == '4':
            print("Програма завершена.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


settings_interface()
