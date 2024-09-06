import matplotlib.pyplot as plt
import csv

with open("data.csv", "r") as file:
    data = csv.reader(file)
    next(data)

    F = []
    d = []

    for row in data:
        F.append(float(row[0]))
        d.append(float(row[1]))

fig, ax = plt.subplots()
ax.plot(F, d)
ax.set_xlabel("Extension (mm)")
ax.set_ylabel("Force (N)")
# ax.set_xlim(0, 5)

# Add a thin black border around the entire figure
fig.patch.set_edgecolor("black")
fig.patch.set_linewidth(1)

# plt.savefig('fdcurve.png', dpi=300)
plt.show()
