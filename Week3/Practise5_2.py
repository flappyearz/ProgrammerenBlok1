def kaartnummer():
    infile = open('Kaartnummers.txt', 'r')
    fileread = infile.readlines()
    infile.close()

    kaartlijst = fileread
    for name in kaartlijst:
        split1 = name.split(',')
        print('{} heeft kaartnummer: {}'.format(split1[1].strip(),split1[0]))

kaartnummer()