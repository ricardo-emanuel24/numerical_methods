import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-6, 6, 100)  # Create a list of evenly-spaced numbers over the range
f = x*np.sin(x) + 3*np.cos(x) - x
plt.plot(x, f)       # Plot the sine of each x point
plt.show()

