class Flower:
    def __init__(self, name, color, stem_length, price, lifespan):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.price = price
        self.lifespan = lifespan

    def __str__(self):
        return (f"{self.name} ({self.color}) - Длина стебля: {self.stem_length} см, "
                f"Стоимость: {self.price} руб.")


class Rose(Flower):
    def __init__(self, stem_length, price):
        super().__init__("Роза", "Красный", stem_length, price, lifespan=7)


class Tulip(Flower):
    def __init__(self, stem_length, price):
        super().__init__("Тюльпан", "Желтый", stem_length, price, lifespan=5)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def total_cost(self):
        return sum(flower.price for flower in self.flowers)

    def sort_flowers(self, key):
        self.flowers.sort(key=key)

    def average_lifespan(self):
        if not self.flowers:
            return 0
        return sum(flower.lifespan for flower in self.flowers) / len(self.flowers)

    def find_flowers(self, lifespan):
        return [flower for flower in self.flowers if flower.lifespan == lifespan]

    def __str__(self):
        return (f"Букет: {', '.join(str(flower) for flower in self.flowers)}\n"
                f"Общая стоимость: {self.total_cost()} руб.")


rose = Rose(stem_length=50, price=150)
tulip = Tulip(stem_length=30, price=100)

bouquet = Bouquet()
bouquet.add_flower(rose)
bouquet.add_flower(tulip)

print(bouquet)
print(f"Среднее время жизни букета: {bouquet.average_lifespan()} дней")

bouquet.sort_flowers(key=lambda flower: flower.price)
print("После сортировки по стоимости:")
print(bouquet)

found_flowers = bouquet.find_flowers(lifespan=5)
print("Цветы с временем жизни 5 дней:")
for flower in found_flowers:
    print(flower)
