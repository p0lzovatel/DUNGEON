# Класс Potion: name, price, heal в __init__; метод describe() возвращает строку «name: price gold,
# +heal health»; вывести результат метода

class Potion:
    def __init__(self, name: str, price: int, heal: int):
        self.name = name
        self.price = price
        self.heal = heal

    def describe(self) -> str:
        return f"{self.name}: {self.price} gold, +{self.heal} health"

def demo_class4():
    potion = Potion("Minor Healing", 10, 20)
    print(potion.describe())

demo_class4()
