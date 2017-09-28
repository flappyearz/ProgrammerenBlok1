def seizoen(maand):
    if maand == 3 or maand == 4 or maand == 5:
        seizoen = 'lente'
        return seizoen
    elif maand == 9 or maand == 10 or maand == 11:
        seizoen = 'herfst'
        return seizoen

print(seizoen(10))