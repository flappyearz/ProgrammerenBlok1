def stringlijst():
    list = eval(input("Geef lijst met minimaal 10 string: "))
    for inlezen in list:
        if len(inlezen) == 4:
            list = []
            list.append(inlezen)

    print("De nieuwe-gemaakte lijst met alle vier-letter string is: ")
    print(list)

stringlijst()
