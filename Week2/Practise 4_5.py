def kwadraten_som(grondgetallen):
    lijst = [0]
    for grondgetal in grondgetallen:
        if grondgetal >= 0:
            kwadraat = grondgetal**2
            lijst.append(kwadraat)

    uitkomst = sum(lijst)
    print(lijst)
    print(uitkomst)


print(kwadraten_som([4, 5, 3, -81]))