# Класс Point с методом __str__, возвращающим «(x, y)»; вывести точку одним print

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

def demo_class7():
    p = Point(5, -3)
    print(p)

demo_class7()
