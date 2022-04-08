from random import randint
from random import seed
from random import randint

"""
Part 1
클래스에 대해서 알아봅니다.
Product 클래스와 Tea 클래스를 만들어 봅니다.
"""

class Product:
    def __init__(self, name):

        self.name = name
        self.price = 30
        self.size = 20
        self.warmness = 0.5
        self.sweetness = 0.5
        self.identifier = randint(1000000, 9999999)

    def sellability(self):
        sellable = self.size / self.price

        if sellable < 0.5:
            return "Not so sellable..."
        elif (0.5 <= sellable) and (sellable < 1.0):
            return "Kinda sellable."
        else:
            return "Very sellable!"


    def calory(self):
        cal = self.size * self.sweetness

        if cal < 10:
            return "...it's light"
        elif (10 <= cal) and (cal < 50):
            return "It's adequate."
        else:
            return "It's really heavy..!!"
        

class Tea(Product):
    def __init__(self, name):
        """
        여기에 코드를 작성합니다.
        상속할 때는 super 를 사용하는 방법도 찾아보세요.
        """
        super().__init__(name)
        self.size = 10

    def calory(self):
        return "...it's a tea. Only a few calories"

    def drink(self):

        if self.warmness < 0.5:
            return "it's too cold..."
        elif (0.5 <= self.warmness) and (self.warmness < 1.0):
            return "Oh, it's warm!"
        else: 
            return "It's too hot!!"