from email.policy import default
import json

class MenuItem:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

    def __str__(self):
        return f"{self.name}, {self.category}, {self.price: .2f}"

    def to_dict(self):
        return {
            'name': self.name, 'category': self.category, 'price': self.price
         }


class MenuManager:
    def __init__(self):
        self.menu_items = {}

    def add_item(self, item):
        if item.category not in self.menu_items:
            self.menu_items[item.category] = {}
        self.menu_items[item.category][item.name] = item
        print(f'Added {item.name} to the {item.category} menu.')

    def remove_item(self, name, category):
        if category in self.menu_items and name in self.menu_items[category]:
            del self.menu_items[category][name]
            print(f'Removed {name} from the {category} menu.')
            if not self.menu_items[category]:
                del self.menu_items[category]
        else:
            print(f"Item {name} not found in the {category} category")

    def update_item_price(self, name, category, new_price):
        if category in self.menu_items and name in self.menu_items[category]:
            self.menu_items[category][name].price = new_price
            print(f'Updated {name} price to {new_price: .2f}.')
        else:
            print(f"Item {name} not found in the {category} category")

    def list_items_by_category(self, category):
        if category in self.menu_items:
            print(f"Category: {category}")
            for name, item in self.menu_items[category].items():
                print(f"\t {item}")
            else:
                print(f"No items in the {category} category.")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.menu_items, file, default=to_dict_func, indent=4)
            print("Menu Saved to file")

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            for category, items in data.items():
                if category not in self.menu_items:
                    self.menu_items[category] = {}
                for item_name, item_data in items.items():
                    self.menu_items[category][item_name] = MenuItem(item_name, category, item_data['price'])
        print('Menu loaded from file')


def to_dict_func(obj):
    return obj.to_dict()


menu_manager = MenuManager()

latte = MenuItem("Latte", "Beverage", 3.50)
print(latte)

coffee = MenuItem("Coffee", "Beverage", 2.50)
print(coffee)



menu_manager.add_item(latte)
menu_manager.add_item(coffee)


print(menu_manager.menu_items)

print()

menu_manager.update_item_price("Latte", "Beverage", 2.50)
print(coffee)
print(latte)

print()

pudding = MenuItem("Pudding", "Dessert", 3.50)
menu_manager.add_item(pudding)
print(pudding)

#print(menu_manager.menu_items)

print()

menu_manager.list_items_by_category('Beverage')
menu_manager.list_items_by_category('Dessert')

print()

menu_manager.add_item(MenuItem('Pasta', 'Entree', 12.00))
menu_manager.add_item(MenuItem('Burger', 'Entree', 10.00))

menu_manager.save_to_file('Menu Files/menu.json')

print()

menu_manager.load_from_file('Menu Files/menu.json')

print()

menu_manager.remove_item("Coffee", "Beverage")
menu_manager.remove_item("Latte", "Beverage")
#print(menu_manager.menu_items)

menu_manager.list_items_by_category('Dessert')