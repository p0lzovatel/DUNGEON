# Класс Inventory: словарь предметов в __init__; методы add(name, qty) и total() (сумма
# количеств); вывести total после трёх добавлений

class Inventory:
    def __init__(self):
        self.items = {}

    def add(self, name: str, qty: int):
        if name in self.items:
            self.items[name] += qty
        else:
            self.items[name] = qty

    def total(self) -> int:
        return sum(self.items.values())

def demo_class6():
    inv = Inventory()
    inv.add("sword", 1)
    inv.add("potion", 3)
    inv.add("arrow", 10)
    print("Total items:", inv.total())

demo_class6()
