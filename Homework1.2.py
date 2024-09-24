subscribers = []

def subscribe(name):
    def confirm_subscription():
        return f"Підписка підтверджена для {name}"

    global subscribers
    subscribers.append(name)
    return confirm_subscription

def unsubscribe(name):
    global subscribers
    if name in subscribers:
        subscribers.remove(name)
        return f"{name} успішно відписаний"
    else:
        return f"Підписника з ім'ям {name} не знайдено"

subscribe('Олена')
subscribe('Ігор')
print(subscribers)
print(unsubscribe('Ігор'))
print(subscribers)