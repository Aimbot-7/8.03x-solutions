import numpy as np
import matplotlib.pyplot as plt

# Parameters
F_0 = 96
omega = 2 * np.pi
omega_0 = 0.5 * np.pi
m = 1
gamma = 0.5  # Damping factor
amplitude = F_0 / m / np.sqrt((omega_0**2 - omega**2)**2 + (gamma * omega)**2)

# Phase shifts to make both functions zero at t = 0, 5, 10, 15, 20
# Set phase shift for x(t) and F(t)
# Choose delta and phi such that both functions go through zero at t=0
delta = np.pi / 2  # Phase for displacement x(t)
phi = np.pi / 2    # Phase for forcing function F(t)

# Time range (extend the curve)
t_transient = np.linspace(0, 8, 1000)  # Transient range (for context)
t_steady = np.linspace(8, 20, 2000)    # Steady-state range (from 0 to 20 seconds)

# Displacement x(t)
x_transient = amplitude * np.cos(omega * t_transient - delta)  # Approximate transient (for continuity)
x_steady = amplitude * np.cos(omega * t_steady - delta)        # Steady-state continuation

# Forcing function F(t)
F_transient = F_0 * np.cos(omega * t_transient + phi)  # Force during transient
F_steady = F_0 * np.cos(omega * t_steady + phi)        # Force during steady-state

# Combine transient and steady-state for the complete curve
t_full = np.concatenate((t_transient, t_steady))
x_full = np.concatenate((x_transient, x_steady))
F_full = np.concatenate((F_transient, F_steady))

# Plotting
plt.figure(figsize=(12, 5))  # Increased width for a wider graph
plt.plot(t_full, x_full, color='blue', linewidth=2, label='x(t) (Displacement)')
plt.plot(t_full, F_full / F_0 * amplitude, color='red', linestyle='--', linewidth=2, label='F(t) (Scaled Forcing)')
plt.title('Displacement and Forcing Function', fontsize=12)
plt.xlabel('Time (t)', fontsize=10)
plt.ylabel('Displacement / Force (scaled)', fontsize=10)
plt.ylim(-4, 4)  # Set vertical axis range from -4 to +4
plt.xlim(0, 20)  # Keep x-axis range from 0 to 20 seconds

# Increase space between tick intervals and adjust ticks to make the graph less clustered
plt.xticks(np.arange(0, 21, 5), fontsize=10)  # Set x-axis ticks at 0, 5, 10, 15, 20
plt.yticks(np.arange(-4, 5, 2), fontsize=10)  # Set y-axis ticks at -4, -2, 0, 2, 4

# Add grid and axes lines
plt.axhline(0, color='gray', linestyle='--', linewidth=0.8)  # Horizontal line at y=0
plt.axvline(0, color='gray', linestyle='--', linewidth=0.8)  # Vertical line at x=0
plt.grid(True, linestyle='--', alpha=0.6)

# Add legend and adjust layout
plt.legend(fontsize=10)
plt.tight_layout()

# Save to PDF
plt.savefig('fig_sol_2.4e.pdf', format='pdf')
plt.show()
