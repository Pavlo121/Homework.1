#discount = 0.1

#def create_order(price):
#    final_price = price * (1 - discount)

#    print(f"Фінальна ціна: {final_price}")

#create_order(1000)





discount = 0.1

def create_order(price):
    final_price = price * (1 - discount)

    def apply_additional_discount():
        nonlocal final_price
        final_price *= 0.95

    apply_additional_discount()
    print(f"Фінальна ціна: {final_price}")



create_order(1000)

