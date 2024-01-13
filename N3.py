class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print('Двигатель заведен')

    def end(self):
        print('Двигатель отключен')


car = Car(color='black', type='BMW', year=2005)
car.start()
print(car.type, car.color, car.year, sep=' ')
car.end()
