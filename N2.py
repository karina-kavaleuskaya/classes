class Math:
    def __init__(self):
        pass

    def addition(self, value_one, value_two):
        return value_one + value_two

    def subtraction(self, value_one, value_two):
        return value_one - value_two

    def multiplication(self, value_one, value_two):
        return value_one * value_two

    def division(self, value_one, value_two):
        if value_two != 0:
            return value_one / value_two
        else:
            return None

# Пример использования
math = Math()
print(f'Сложение 3 и 5 равно: {math.addition(5, 3)}')
print(f'Вычитание 10 и 4 равно: {math.subtraction(10, 4)}')
print(f'Умножение 6 и 7 равно:{math.multiplication(6, 7)}')
print(f'Деление 8 и 2 равно:{math.division(8, 2)}')
