# Klasa implementująca liczby zespolone z przeciążonymi operatorami dodawania i odejmowania.
class Complex:
    def __init__(self, re, im=0.0):
        # Inicjalizacja liczby zespolonej: część rzeczywista (re) i urojona (im)
        self.re = re
        self.im = im

    def __add__(self, other):
        # Przeciążenie operatora dodawania: dodawanie części rzeczywistych i urojonych
        return Complex(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        # Przeciążenie operatora odejmowania: odejmowanie części rzeczywistych i urojonych
        return Complex(self.re - other.re, self.im - other.im)

    def __str__(self):
        # Metoda zwracająca czytelną reprezentację liczby zespolonej
        return f"{self.re} + {self.im}i"


# Tworzenie dwóch liczb zespolonych
number1 = Complex(5, 2)
number2 = Complex(10, 4)

# Dodawanie i odejmowanie liczb zespolonych
print(number2 + number1)  # Output: 15 + 6i
print(number1 - number2)  # Output: -5 - 2i

# Opis algorytmu:
# Klasa `Complex` reprezentuje liczby zespolone z przeciążonymi operatorami
# dodawania i odejmowania. Konstruktor inicjalizuje liczbę zespoloną z częściami
# rzeczywistą i urojoną. Operator dodawania (__add__) oraz odejmowania (__sub__)
# działają na częściach liczby zespolonej, co pozwala wykonywać działania na obiektach
# klasy `Complex` jak na standardowych liczbach zespolonych.
