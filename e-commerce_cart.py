def calculate_total_price(cart_items):
    if cart_items==0:
        return 0
    total_price=sum(cart_items.values())
    if len(cart_items)> 5:
        total_price*=0.9
    return total_price
cart_items={'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
r=calculate_total_price(cart_items)
print(r)




