import matplotlib.pyplot as plt
bestand = open("csv.csv","r")
lijst = []
regel = bestand.readline()
for regel in bestand:
    regel = regel.replace("\n","")
    lijst.append(regel.split(","))
x = []
y = []
for i in range(len(lijst)):
    x.append(lijst[i][0])
    y.append(lijst[i][1])

plt.plot(x, y)
plt.title('Lijndiagram')
plt.xlabel('Patientnummer')
plt.ylabel('Medicijn A mg')
plt.show()