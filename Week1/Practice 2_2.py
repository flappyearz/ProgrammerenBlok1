cijferICOR = 7
cijferPROG = 9
cijferCSN = 6.5

gemiddelde = (cijferCSN+cijferICOR+cijferPROG)/3
beloning = (cijferCSN+cijferICOR+cijferPROG)*30

overzicht = 'Mijn cijfers (gemiddeld een '+str(gemiddelde)+ ') leveren een beloning van €'+str(beloning)+' op!'

print(overzicht)