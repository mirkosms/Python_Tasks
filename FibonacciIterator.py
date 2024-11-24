# Własny iterator zwracający kolejne liczby ciągu Fibonacciego z określoną liczbą wyrazów.

class Fibonacci:
    def __init__(self, steps):
        # Inicjalizacja iteratora z maksymalną liczbą wyrazów (steps)
        self.steps = steps
        self.a, self.b = 0, 1
        self.counter = 0

    def __iter__(self):
        # Zwraca samego siebie jako iterator
        return self

    def __next__(self):
        # Zwraca kolejną liczbę Fibonacciego, aż osiągnie maksymalną liczbę kroków
        if self.counter >= self.steps:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        self.counter += 1
        return self.a


# Tworzenie iteratora i drukowanie kolejnych liczb Fibonacciego
fibonacciNumbers = Fibonacci(10)
for number in fibonacciNumbers:
    print(number)

# Opis algorytmu:
# Klasa `Fibonacci` implementuje iterator generujący liczby Fibonacciego.
# Inicjalizacja klasy ustawia maksymalną liczbę wyrazów w sekwencji (steps).
# Metoda `__next__` oblicza kolejną liczbę Fibonacciego, dopóki licznik
# nie osiągnie limitu wyrazów, po czym rzuca wyjątek StopIteration.
# Kod w głównej części programu pokazuje użycie iteratora w pętli for.
