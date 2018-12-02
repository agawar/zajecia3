def statystyka(nazwa_pliku):
    suma_znakow = 0
    suma_slow = 0
    suma_zdan = 0

    with open(nazwa_pliku, 'r') as fh:
        tekst = fh.read
        suma_znakow = len(tekst)


