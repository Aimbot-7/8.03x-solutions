import matplotlib.pyplot as plt
import numpy as np

# Data points for the first graph
x1_shifted = [-2, -1.5, 0, 1]
y1_corrected = [0, -0.5, 2, 0]

# Data points for the second graph (shifted 0.5 units to the right)
x2_interface_shifted = [-1.5, -1, -0.5, 0.5, 1, 1.5, 2]
y2_corrected = [0, -0.5, 0, 0, 1, 2, 0]

# Interface position for the second graph (set at x = 0)
interface_position_second_graph = 0

# Color for the lines (same for both)
line_color = 'red'

# Plot the first graph
plt.figure(figsize=(8, 6))
plt.plot(x1_shifted, y1_corrected, color=line_color, linewidth=2)
plt.axvline(0, color='blue', linestyle='--', label='interface')  # Interface at x=0

# Add a line at y=0 for x < -2 and x > 1.5
plt.plot(np.linspace(-2.5, -2, 100), np.zeros(100), color=line_color, linewidth=2)
plt.plot(np.linspace(1, 1.5, 100), np.zeros(100), color=line_color, linewidth=2)

# Add gridlines and hide axis ticks
plt.gca().xaxis.set_ticks_position('none')
plt.gca().yaxis.set_ticks_position('none')
plt.xticks(np.arange(-2, 2.1, 0.5))  # Add x-ticks at regular intervals
plt.yticks(np.arange(-1, 3, 1))  # Add y-ticks at regular intervals

plt.xlabel('$x$ (m)')
plt.ylabel('$y$')
plt.title('Total Deformation at Interface')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)  # Add gridlines
plt.savefig('fig_sol_4.3b.pdf')
plt.close()

# Plot the second graph with updated line and interface
plt.figure(figsize=(8, 6))
plt.plot(x2_interface_shifted, y2_corrected, color=line_color, linewidth=2)

# Add a line at y=0 for x < -1.5
plt.plot(np.linspace(-2.5, -1.5, 100), np.zeros(100), color=line_color, linewidth=2)
plt.plot(np.linspace(2, 2.5, 100), np.zeros(100), color=line_color, linewidth=2)

plt.axvline(interface_position_second_graph, color='blue', linestyle='--', label='interface')  # Interface at x=0

# Add gridlines and hide axis ticks
plt.gca().xaxis.set_ticks_position('none')
plt.gca().yaxis.set_ticks_position('none')
plt.xticks(np.arange(-2, 2.1, 0.5))  # Add x-ticks at regular intervals
plt.yticks(np.arange(-1, 3, 1))  # Add y-ticks at regular intervals

plt.xlabel('$x$ (m)')
plt.ylabel('$y$')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)  # Add gridlines
plt.savefig('fig_sol_4.3c.pdf')
plt.close()
