import numpy as np

income = input("How much were you paid? ")

splurge = np.round(float(income) * 0.075, 2)
smile = np.round(float(income) * 0.1, 2)
fire = np.round(float(income) * 0.15, 2)

print("Transfer Amounts:")
print("Splurge: $" + str(splurge))
print("Smile: $" + str(smile))
print("Fire Extinguisher: $" + str(fire))