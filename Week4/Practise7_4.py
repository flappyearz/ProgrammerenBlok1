def ticker(filename):
    infile = open(filename, 'r')
    inhoud = infile.readlines()
    ticker_dict = {}

    for regel in inhoud:
        tickerinfo_lijst = regel.split(':')
        companyname = tickerinfo_lijst[0]
        symbol = tickerinfo_lijst[1]

        ticker_dict[symbol] = companyname

    return ticker_dict
