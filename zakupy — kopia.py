def zakupy(cennik, lista):
    sumazakupow = 0
    for artykul in lista:
        if artykul in cennik:
            sumazakupow += lista[artykul]*cennik[artykul]
    
    return sumazakupow

def cennik_vat(cennik):
    for artykul in cennik:
        cena_vat = round(0.23 * cennik[artykul], 2)
        cennik[artykul] = round(cennik[artykul]+cena_vat, 2)
        print(cennik[artykul])

    return cennik

cennik = {
    'kawa': 14.99,
    'pomarańcze': 3.49,
    'olej': 4.99
    }
lista = {'olej': 2, 'kawa': 1}
print("Suma zakupów netto to {0} zł".format(zakupy(cennik, lista)))
print("Suma zakupów brutto to {0} zł".format(zakupy(cennik_vat(cennik), lista)))
