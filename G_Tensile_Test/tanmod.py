import matplotlib.pyplot as plt
from scipy import stats
import csv

with open("btrdata.csv", "r") as file:
    data = csv.reader(file)
    data = list(data)

S = [float(data[i][0]) for i in range(1, 2196)]
e = [float(data[i][1]) for i in range(1, 2196)]

# linear regression
tan_mod, intercept, r, p, std_err = stats.linregress(e, S)

# Tangent Modulus
print(tan_mod)

fig, ax = plt.subplots()
ax.plot(e, S, label="Data")
ax.plot(e, [tan_mod * x + intercept for x in e], label="Linear Model")
ax.text(
    0.05,
    0.95,
    f"Slope: {tan_mod:.2f}",
    transform=ax.transAxes,
    fontsize=12,
    verticalalignment="top",
)

ax.set_xlabel("Engineering Strain")
ax.set_ylabel("Engineering Stress (MPa)")
ax.set_title("Tangent Modulus")

# plt.savefig("tanmod.png", dpi=300)
plt.show()
