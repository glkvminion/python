activity_log = []

class Item:
    def __init__(self, title, quantity, cost):
        self.title = title
        self.quantity = quantity
        self.cost = cost

    def increase_quantity(self, amount):
        self.quantity += amount
        activity_log.append(f"Добавлено {amount} единиц товара {self.title}. Текущее количество: {self.quantity}")

    def decrease_quantity(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            activity_log.append(f"Списано {amount} единиц товара {self.title}. Остаток: {self.quantity}")
            return True
        else:
            activity_log.append(f"Ошибка: невозможно списать {amount} единиц товара {self.title}. Доступно: {self.quantity}")
            return False

    def calculate_total_value(self):
        return self.quantity * self.cost

    def __eq__(self, other):
        return isinstance(other, Item) and self.title == other.title and self.quantity == other.quantity and self.cost == other.cost


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, title, quantity, cost):
        new_item = Item(title, quantity, cost)
        self.items.append(new_item)
        activity_log.append(f"Добавлен товар: {title}, Количество: {quantity}, Цена: {cost}")
        return new_item

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            activity_log.append(f"Удалён товар: {item.title}, Количество: {item.quantity}, Цена: {item.cost}")
        else:
            activity_log.append(f"Ошибка: товар {item.title} не найден в списке")

    def calculate_inventory_value(self):
        total_value = sum(item.calculate_total_value() for item in self.items)
        activity_log.append(f"Общая стоимость товаров на складе: {total_value}")
        return total_value

    def list_items(self):
        activity_log.append("Список товаров на складе:")
        for item in self.items:
            activity_log.append(f"Название: {item.title}, Количество: {item.quantity}, Цена: {item.cost}")


class Vendor:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
        self.sales = []

    def sell_item(self, title, quantity):
        for item in self.inventory.items:
            if item.title == title:
                if item.decrease_quantity(quantity):
                    revenue = quantity * item.cost
                    self.sales.append({"Название": item.title, "Количество": quantity, "Цена за единицу": item.cost})
                    activity_log.append(f"Продан товар: {item.title}, Количество: {quantity}, Выручка: {revenue}")
                    return revenue
                else:
                    return "Недостаточно товара на складе"
        activity_log.append(f"Ошибка: товар {title} не найден на складе")
        return "Товар не найден"

    def sales_report(self):
        activity_log.append("Формирование отчёта о продажах...")
        return self.sales


warehouse = Inventory()
vendor = Vendor("Иван", warehouse)

warehouse.add_item("Хлеб", 10, 25)
warehouse.add_item("Молоко", 20, 50)
warehouse.add_item("Сок", 15, 30)

warehouse.list_items()

warehouse.remove_item(Item("Хлеб", 10, 25))

total_value = warehouse.calculate_inventory_value()

revenue_1 = vendor.sell_item("Молоко", 5)
revenue_2 = vendor.sell_item("Сок", 10)

total_value_after_sales = warehouse.calculate_inventory_value()

sales_report = vendor.sales_report()

print("Отчёт о продажах:", sales_report)

print("История операций:")
for record in activity_log:
    print(record)
