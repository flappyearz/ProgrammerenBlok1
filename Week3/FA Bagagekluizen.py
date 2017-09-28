print("1: Ik wil weten hoeveel kluizen nog vrij zijn")
print("2: Ik wil een nieuwe kluis")
print("3: Ik wil even iets uit mijn kluis halen")
print("4: Ik geef mijn kluis terug")
print("Wat wilt u doen?")
optie = int(input())


def toon_aantal_kluizen_vrij():
    infile = open("kluizen.txt", 'r')
    lines = infile.readlines()
    regels = 12 - len(lines)
    print("Er zijn nog "+ str(regels) + " kluizen vrij.")

def nieuwe_kluis():
    kluisnummers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    infile = open('kluizen.txt')
    lines = infile.readlines()
    infile.close()

    for regel in lines:
        kluisinfo = regel.split(';')
        kluisnummer = int(kluisinfo[0])
        kluisnummers.remove(kluisnummer)

    if (len(kluisnummers) > 0):
        nieuwe_code = input('Geef een kluiscode op: ')
        nieuwe_nummer = kluisnummers[0]
        print('Uw nieuwe kluisnummr is: ' + str(nieuwe_nummer))
        outfile = open('kluizen.txt', 'a')
        outfile.write(str(nieuwe_nummer) + ';' + nieuwe_code + '\n')
        outfile.close()

def kluis_openen():
    kluisnummer = input("Voer uw kluisnummer in:")
    kluiscode = input("Voer uw kluiscode in:")
    infile = open('kluizen.txt', 'r')
    lines = infile.readlines()
    for controleren in lines:
        kluisinfo = controleren.split(';')
        if kluisnummer == kluisinfo[0] and kluiscode == kluisinfo[1]:
            print("Uw heeft de correcte combinatie ingevoerd!")


    print("Deze combinatie is ongeldig!")
    print(kluisinfo[0], kluisinfo[1])


def kluis_teruggeven():
    print("4")



if optie > 0 and optie < 5:
    if optie == 1:
        toon_aantal_kluizen_vrij()
    elif optie == 2:
        nieuwe_kluis()
    elif optie == 3:
        kluis_openen()
    elif optie == 4:
        kluis_teruggeven()
else:
    print("Oeps! Deze optie bestaat niet probeer opnieuw")