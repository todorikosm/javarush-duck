# Защищайтесь.

# Создайте класс Car, который будет иметь публичный атрибут brand и защищенный атрибут _model.
# Добавьте методы для получения и установки значения защищенного атрибута _model.
# Создайте объект класса Car, установите значения атрибутов и выведите их на экран.

# Напишите тут ваш код

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self._model = model

    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model


car = Car("Mercedes-Benz", "E230")

car.brand = "MB"
print(car.brand)
car.set_model("W124")
print(car.get_model())


