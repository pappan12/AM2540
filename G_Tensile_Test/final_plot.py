import csv
import matplotlib.pyplot as plt

with open("btrdata.csv", "r") as f:
    data = list(csv.reader(f))

S = [float(i[0]) for i in data[1:]]
e = [float(i[1]) for i in data[1:]]
sigma = [float(i[2]) for i in data[1:]]
epsilon = [float(i[3]) for i in data[1:]]

fig, ax = plt.subplots()
ax.plot(e, S, label="Engineering Stress-Strain")
# ax.plot(epsilon, sigma, label='True Stress-Strain')
ax.set_xlabel("Strain")
ax.set_ylabel("Stress (MPa)")
ax.legend()

# Points to highlight and label
points_to_label = [
    (e[2100], S[2100], "Proportionality Limit"),
    (e[2196], S[2196], "Upper Yield Point"),
    (e[2781], S[2781], "Lower Yield Point"),
    (e[11665], S[11665], "Ultimate Tensile Strength"),
    (e[-1], S[-1], "Breaking Point"),
]

# Highlight and label the points
for x, y, label in points_to_label:
    ax.scatter(x, y, color="black")
    ax.text(x + 0.0001, y + 10, label)

# Add a thin black border around the entire figure
fig.patch.set_edgecolor("black")
fig.patch.set_linewidth(1)

# plt.savefig('points.png', dpi=300)
plt.show()
