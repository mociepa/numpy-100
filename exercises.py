# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:27:06 2024

@author: Admin
"""

import numpy as np

#np.__version__
#np.show_config()

print(np.zeros(10))

np.size(np.zeros(10))

np.info(np.add)


z = np.zeros(10)
z[4] = 1
print(z)

bb = np.arange(10, 50)
bb[: :-1]

print(np.arange(0, 9).reshape(3, 3))

z = np.nonzero([1,2,0,0,4,0])

np.seterr(over = "warn")

np.exp(1000)

import matplotlib.pyplot as plt

car = np.array(["Caterham", "Tesla", "Audi",  "BMW", "Ford", "Jeep"])
weight = np.array([0.48, 1.7, 2, 2, 2.3, 3 ])

# set colors and sizes
colors = np.array([0, 1, 2, 3, 4, 5])
sizes = np.array([20, 40, 60, 80, 100, 120])

plt.scatter(car, weight, c=colors, s=sizes)
plt.show()