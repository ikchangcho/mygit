import numpy as np
import matplotlib.pyplot as plt

# Example data
x = np.linspace(0, 10, 100)

for i in range(3):
    # Create a new figure for each iteration
    fig = plt.figure()

    # Plot on the current figure
    y = np.sin(x) + i  # Replace this with your own data or function
    plt.plot(x, y, label=f'Iteration {i}')

    # Add labels and title
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title(f'Graph for Iteration {i}')

    # Display legend
    plt.legend()

# Show all the plots
plt.show()
