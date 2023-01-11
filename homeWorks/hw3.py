class Bank:
    def __init__(self, name, balanse):
        self._name = name
        self._balanse = balanse

    def moneyX(self):
        ad = input(f'сколько добавишь к своим {self._balanse} введи сумму: ')
        print(self._balanse + int(ad))

    def __kill(self):
        if self._balanse > 0:
            print('теперь у тебя все наличкой')
            return self._balanse - self._balanse
        else:
            print('ты и так бомж, на счету нету денег')
            return self._balanse

    def _jeckpot(self):
        print(self._balanse * 10)

    def __cygan(self, other):
        print(f'{self._balanse + other._balanse} and {other._balanse}')

bank = Bank('mbank', 20)
load = Bank('optima', 100)
bank.moneyX()
print(bank._Bank__kill())
bank._Bank__cygan(load)
bank._jeckpot()
class Calkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self):
        return self.a + self.b

    def __sub__(self):
        return self.a - self.b

    def __mul__(self):
        return self.a * self.b

    def __truediv__(self):
        return self.a / self.b
calkulator = Calkulator(100,100)
print(f'сложение: {calkulator.__add__()}')
print(f'вычитание: {calkulator.__sub__()}')
print(f'умножение: {calkulator.__mul__()}')
print(f'деление: {calkulator.__truediv__()}')
