class Soda:
    def __init__(self, taste=None):
        self.taste = taste

    def __str__(self):
        if self.taste:
            return f'У вас газировка с {self.taste} вкусом'
        else:
            return 'У вас обычная газировка'




soda1 = Soda('клубничным')
print(soda1)

soda2 = Soda()
print(soda2)