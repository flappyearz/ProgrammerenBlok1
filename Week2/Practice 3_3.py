leeftijd = int(input("Geef je leeftijd:"))
paspoort = input("Nederlands paspoort:")

if leeftijd >= 18 and paspoort == "Ja":
    print("Je mag stemmen!!!!")
else:
    print("JAMMER JOH!")