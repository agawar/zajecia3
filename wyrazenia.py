class Wyrazenie:
    pass


class Zmienna(Wyrazenie):

    def __init__(self, nazwa):
        self.nazwa = nazwa

    def __str__(self):
        return self.nazwa

    def oblicz(self, stan):
        return stan[self.nazwa]

class Stala(Wyrazenie):

    def __init__(self, liczba):
        self.liczba = liczba

    def __str__(self):
        return str(self.liczba)

    def oblicz(self, stan):
        stan = self.liczba
        return stan


class Dodawanie(Wyrazenie):

    def __init__(self, lewy, prawy):
        self.lewy = lewy
        self.prawy = prawy

    def __str__(self):
        return str(self.lewy) + " + " + str(self.prawy)

    def oblicz(self, stan):
        return self.lewy.oblicz(stan) + self.prawy.oblicz(stan)

class Mnozenie(Wyrazenie):

    def __init__(self, czynnik_lewy, czynnik_prawy):
        self.czynniklewy = czynnik_lewy
        self.czynnikprawy = czynnik_prawy

    def __str__(self):
        return str(self.czynniklewy) + " * " + str(self.czynnikprawy)

    def oblicz(self, stan):
        return self.czynniklewy.oblicz(stan) * self.czynnikprawy.oblicz(stan)

wyrazenie = Dodawanie(Dodawanie(Zmienna("x"), Zmienna("y")), Zmienna("z"))

print(wyrazenie)
stan = {'x' : 2, 'y' : 4, 'z' : 6}
print(wyrazenie.oblicz(stan))


wyrazenie2 = Dodawanie(Zmienna("x"), Stala(17))
print(wyrazenie2)
print(wyrazenie2.oblicz(stan))

wyrazenie_mnoz = Mnozenie(Mnozenie(Zmienna("x"), Zmienna("y")), Zmienna("z"))
print(wyrazenie_mnoz)
print(wyrazenie_mnoz.oblicz(stan))