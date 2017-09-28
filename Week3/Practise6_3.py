invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
l1 = invoer.split("-")
l1.sort()

print('Gesorteerde list van ints:' +str(l1))
print('Grooste getal: ' +str(l1[-1])+ ' en Kleinste getal: '+str(l1[0]))
print('Aantal getallen:' +str(len(l1))+ ' en Som van de getallen: '+str(sum(int(x) for x in l1)))
print('Gemiddelde:' +str(sum(int(x) for x in l1) / (len(l1))))