import matplotlib.patches as mpatches
import numpy as np
import matplotlib.pyplot as plt
bestand = open("yeast_genes.csv","r")
lijst = []
regel = bestand.readline()
for regel in bestand:
    regel = regel.replace("\n","")
    lijst.append(regel.split(","))

status = []
i = 0
for i in range(len(lijst)):
    if lijst[i][1] not in status:
        status.append(lijst[i][1])

print("De verschillende statussen dat een lijst kan hebben zijn:", status)

y = []

verified = 0
dubious = 0
uncharacterized = 0
na = 0
verified_silenced_gene = 0

for i in range(len(lijst)):
    verified += lijst[i][1].count("Verified")
    dubious += lijst[i][1].count("Dubious")
    uncharacterized += lijst[i][1].count("Uncharacterized")
    na += lijst[i][1].count("NA")
    verified_silenced_gene += lijst[i][1].count("Verified|silenced_gene")

y.append(verified)
y.append(dubious)
y.append(uncharacterized)
y.append(na)
y.append(verified_silenced_gene)

plt.bar(status, y, color=["blue", "red", "green", "yellow", "black"])
plt.title('Bar plot')
plt.xlabel('Status')
plt.ylabel('Aantal keer voorkomen')

legenda1 = mpatches.Patch(color="blue", label="Verified")
legenda2 = mpatches.Patch(color="red", label="Dubious")
legenda3 = mpatches.Patch(color="green", label="Uncharacterized")
legenda4 = mpatches.Patch(color="yellow", label="NA")
legenda5 = mpatches.Patch(color="black", label="Verified|silenced_gene")

plt.legend(handles=[legenda1, legenda2, legenda3, legenda4, legenda5])
plt.show()
