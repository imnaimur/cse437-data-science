# Print the last item from year and pop
import numpy as np
year = np.arange(1950,2101)
# Logistic growth model parameters
# K = carrying capacity (max population)
# r = growth rate
# t0 = midpoint (year when growth slows)
K = 11       # Max population (billions)
r = 0.03     # Growth rate
t0 = 2025    # Midpoint year

# Logistic growth formula
pop = K / (1 + np.exp(-r * (year - t0)))


print(year[-1])
print(pop[-1])

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year,pop)

# Display the plot with plt.show()
plt.show()
