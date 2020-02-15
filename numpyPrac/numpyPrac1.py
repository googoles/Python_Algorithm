
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi)

plt.plot(x, np.cos(x))
plt.plot(x, np.sin(x))
plt.show()