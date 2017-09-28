def deel1():
    infile = open('Kaartnummers.txt', 'r')
    inhoud = infile.readlines()
    lengteinhoud = len(inhoud)
    print('Deze file telt '+str(lengteinhoud)+' regels')

def deel2():
    infile = open('Kaartnummers.txt', 'r')
    lines = infile.readlines()
    lines.split('0','1','2')
    print(lines)

deel1()
deel2()

