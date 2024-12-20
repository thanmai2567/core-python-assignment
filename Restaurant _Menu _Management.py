def add_menu_item(menu,item):
    if item not in menu:
        menu.append(item)
    return menu

def remove_menu_item(menu,item):
    if item in menu:
        menu.remove(item)
    else:
        print(f"Item {item} does not exist in the menu")
    return menu

def check_menu_item(menu,item):
    if item in menu:
        return f"{item}  is available"
    else:
        return f"{item} is not available"
initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item="Tacos"
updated_menu=add_menu_item(initial_menu,add_item)

remove_item="Salad"
updated_menu=remove_menu_item(updated_menu,remove_item)

check_item="Pizza"
availability=check_menu_item(updated_menu,check_item)

print("Updated menu:", updated_menu)
print("Availability:", availability)