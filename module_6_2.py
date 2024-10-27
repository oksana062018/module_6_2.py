class Vehicle:
    __COLOR_VARIANTS = ['red', 'grey', 'yellow', 'black', 'silver', 'dark_blue']
    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color


    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец авто: {self.owner}")

    # Метод set_color - принимает аргумент new_color(str), меняет цвет __color на new_color,
    # если он есть в списке __COLOR_VARIANTS, в противном случае выводит на экран надпись:
    # "Нельзя сменить цвет на <новый цвет>".
    def set_color(self, new_color: str):

        if new_color in  self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5



vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()