import matplotlib.pyplot as plt
labels = "Groep 1", "Groep 2", "Groep 3"
sizes = [100, 150, 125]
colors = ["green", "lightskyblue", "gold"]
plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", shadow=True, startangle=140)
plt.axis("equal")
plt.show()