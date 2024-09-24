def create_product(name):
    def product_with_price(price):
        def product_with_quantity(quantity):
            def update_price(new_price):
                nonlocal price
                price = new_price
                print(f"Ціна товару '{name}' змінена на {price} грн")


            def get_info():
                return f"Назва: {name}, Ціна: {price} грн, Кількість: {quantity} шт."

            return update_price, get_info

        return product_with_quantity

    return product_with_price



create_iphone = create_product("Відео карта 4090")
set_price_iphone = create_iphone(90000)
update_price_iphone, get_info_iphone = set_price_iphone(10)

print("Інформація про товар:", get_info_iphone())

update_price_iphone(88000)

print("Оновлена інформація про товар:", get_info_iphone())
