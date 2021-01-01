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
    x.append(lijst[i][3])
    y.append(lijst[i][0])

plt.bar(x, y)
plt.title('Scatter plot')
plt.xlabel('Arts')
plt.ylabel('Aantal Patienten')
plt.show()