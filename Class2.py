# К классу Point добавить метод shift(dx, dy), меняющий координаты; применить и вывести поля

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def shift(self, dx, dy):
        self.x += dx
        self.y += dy

def demo_class2():
    p = Point(1, 2)
    print(f"До сдвига: x={p.x}, y={p.y}")
    p.shift(3, -1)
    print(f"После shift(3, -1): x={p.x}, y={p.y}")

demo_class2()
