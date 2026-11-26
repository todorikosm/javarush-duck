# Создаем объекты.

# Создайте класс Car с атрибутами make, model и year.
# Добавьте метод display_info(), который выводит информацию о машине.
# Затем создайте объект этого класса и вызовите метод display_info().

# Напишите тут ваш код

class Car:
    make = "Mercedes-Benz"
    model = "E230 W124"
    year = 1991


    def display_info(self):
        print(self.make, self.model, self.year)

car = Car()
car.display_info()