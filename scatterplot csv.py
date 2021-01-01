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

x = []
y = []
for i in range(len(lijst)):
    x.append(lijst[i][1])
    y.append(lijst[i][2])

plt.scatter(x, y)
plt.title('Scatter plot')
plt.xlabel('Medicijn A')
plt.ylabel('Medicijn B')
plt.show()