import csv
import numpy as np

with open("data.csv", "r") as f:
    data = csv.reader(f)
    next(data)

F = []
delta_l = []

for row in data:
    F.append(float(row[1]))
    delta_l.append(float(row[0]))

d = 8.25  # in mm
A = np.pi * (d / 2) ** 2
l_0 = 29.4869  # in mm

# Engineering Stress
S = [f / A for f in F]  # in MPa

# Engineering Strain
e = [dl / l_0 for dl in delta_l]

# True Stress
sigma = [S[i] * (1 + e[i]) for i in range(len(S))]

# True Strain
epsilon = [np.log(1 + e[i]) for i in range(len(e))]

# Exporting all 4 data, tangent modulus and %difference in True and Engineering Stress
# with open('btrdata.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Engineering Stress (MPa)', 'Engineering Strain', 'True Stress (MPa)', 'True Strain', 'Tangent Modulus (MPa)', '%Difference in True and Engineering Stress'])
#     for i in range(len(S)):
#         if e[i] == 0:
#             writer.writerow([S[i], e[i], sigma[i], epsilon[i], 0, 0])
#             continue
#         writer.writerow([S[i], e[i], sigma[i], epsilon[i], S[i]/e[i], abs(S[i] - sigma[i])/S[i] * 100])

# Required sample data for the table
with open("table.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(
        [
            "Sl No.",
            "Extension",
            "Force",
            "Engineering Stress (MPa)",
            "Engineering Strain",
            "True Stress (MPa)",
            "True Strain",
        ]
    )
    for i in range(20):
        writer.writerow([i + 1, delta_l[i], F[i], S[i], e[i], sigma[i], epsilon[i]])
