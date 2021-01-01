import matplotlib.pyplot as plt
bestand = open("csv.csv","r")
lijst = []
regel = bestand.readline()
for regel in bestand:
    regel = regel.replace("\n","")
    lijst.append(regel.split(","))

for i in range(len(lijst)):
    lijst[i][1] = int(lijst[i][1])
    lijst[i][2] = int(lijst[i][2])

xJanssen = []
yJanssen = []
xBerends = []
yBerends = []

for i in range(len(lijst)):
    if "Janssen" in lijst[i][3]:
        xJanssen.append(lijst[i][1])
        yJanssen.append(lijst[i][2])

    if "Berends" in lijst[i][3]:
        xBerends.append(lijst[i][1])
        yBerends.append(lijst[i][2])

plt.scatter(xJanssen, yJanssen, c="red", label="Janssen")
plt.scatter(xBerends, yBerends, c="blue", label="Berends")
plt.title('Scatter plot')
plt.xlabel('Medicijn A')
plt.ylabel('Medicijn B')
plt.show()