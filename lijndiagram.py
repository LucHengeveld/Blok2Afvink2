import matplotlib.pyplot as plt

x_values = [10,20,30,40,50,60,70,80]
y_values = [3,5,8,10,12,15,18,20]
more_y_values = [1,2,3,4,5,6,7,8]

plt.xlabel("Tientallen")
plt.ylabel("Willekeurige waardes")
plt.title("Oefengrafiek")
plt.plot(x_values, y_values)
plt.plot(x_values, more_y_values)
plt.show()