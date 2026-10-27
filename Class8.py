# Класс Hero: name, health, damage; методы to_dict() и from_dict(data); сохранить объект в
# словарь, создать из словаря новый объект и вывести его health

class Hero:
    def __init__(self, name: str, health: int, damage: int):
        self.name = name
        self.health = health
        self.damage = damage

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "health": self.health,
            "damage": self.damage,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Hero":
        return cls(
            name=data["name"],
            health=data["health"],
            damage=data["damage"],
        )

def demo_class8():
    hero1 = Hero("Aragorn", 120, 35)
    data = hero1.to_dict()
    hero2 = Hero.from_dict(data)
    print("Health нового героя:", hero2.health)

demo_class8()
