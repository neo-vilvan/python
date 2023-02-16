import matplotlib.pyplot as plt
import numpy as np

# Generate some example data
np.random.seed(0)
x = np.random.rand(100, 1)
y = 2 + 6 * x + np.random.rand(100, 1)

# Fit a linear regression model to the data
A = np.hstack((np.ones((100, 1)), x))
w = np.linalg.inv(A.T.dot(A)).dot(A.T).dot(y)

# Plot the data points and the best fit line
plt.scatter(x, y, marker='o')
plt.plot(x, w[0] + w[1] * x, 'r')
plt.show()
