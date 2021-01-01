import matplotlib.pyplot as plt
labels = "> of = aan 50", "40 tot 50", "< 40"
bestand = open("csv.csv","r")
lijst = []
regel = bestand.readline()
for regel in bestand:
    regel = regel.replace("\n","")
    lijst.append(regel.split(","))

groter = 0
midden = 0
kleiner = 0
for i in range(0,len(lijst)):
    if int(lijst[i][2]) > 49:
        groter += 1
    if int(lijst[i][2]) > 39 and int(lijst[i][2]) < 50:
        midden += 1
    if int(lijst[i][2]) < 40:
        kleiner += 1
totaal = groter+midden+kleiner
pgroter = (groter/totaal) * 100
pmidden = (midden/totaal) * 100
pkleiner = (kleiner/totaal) * 100
sizes = [pgroter, pmidden, pkleiner]
colors = ["green", "blue", "yellow"]
plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", shadow=True, startangle=90)
plt.show()