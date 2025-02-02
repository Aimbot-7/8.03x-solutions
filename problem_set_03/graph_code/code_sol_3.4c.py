import numpy as np
import matplotlib.pyplot as plt

# Physical parameters (example values)
k = 1.0  # spring constant
M = 1.0  # mass
l = 1.0  # length of the spring
X_0 = 1.0  # driving amplitude
g = 1.0  # constant g

# Frequency range (from 0 to 2.5 to focus more on the relevant region)
omega_vals = np.linspace(0.0, 2.5, 500)

# Calculating C1 and C2 amplitudes
def calculate_C1_C2(omega, k, M, l, X_0, g):
    # Denominators for the amplitude formulas
    denom = k * g + M * l * omega**4 - (k * l + 2 * M * g) * omega**2
    
    C1 = (k * X_0 * (g - l * omega**2)) / denom
    C2 = (k * g * X_0) / denom
    
    return C1, C2

# Get the amplitudes for each omega
C1_vals = np.zeros_like(omega_vals)
C2_vals = np.zeros_like(omega_vals)
for i, omega in enumerate(omega_vals):
    C1_vals[i], C2_vals[i] = calculate_C1_C2(omega, k, M, l, X_0, g)

# Normalize by X_0 (C/X_0)
C1_vals_normalized = C1_vals / X_0
C2_vals_normalized = C2_vals / X_0

# Pendulum-only oscillation frequency (ω = g/l)
omega_pendulum = np.sqrt(g / l)

# Plotting the results
plt.figure(figsize=(10, 6))

# Plot for C1 and C2 normalized by X_0
plt.plot(omega_vals, C1_vals_normalized, label=r"$C_1$", color='blue')
plt.plot(omega_vals, C2_vals_normalized, label=r"$C_2$", color='red')

# Marking the frequency where only the pendulum oscillates (ω = g/l)
plt.axvline(x=omega_pendulum, color='green', linestyle=':', label=r'$\omega_p$')

# Assigning x = 0.619 ω_- with black color (shifted to x = 0.619)
omega_minus = 0.619 * np.sqrt(g / l)  # Shifted to x = 0.619
plt.axvline(x=omega_minus, color='black', linestyle='-', label=r'$\omega_-$')

# Assigning x = 1.614 ω_+ with purple color
omega_plus = 1.614 * np.sqrt(g / l)  # example for omega_+ with the scaling factor
plt.axvline(x=omega_plus, color='purple', linestyle='-', label=r'$\omega_+$')

# Adding title, labels, and legend with increased font size
plt.title("Amplitude of the Two Masses as a Function of Frequency (ω)", fontsize=16)
plt.xlabel("Frequency (ω)", fontsize=14)
plt.ylabel("Amplitude", fontsize=14)
plt.legend(fontsize=12)

# Adjusting the y-axis limits to prevent zooming in too much
plt.ylim(-5, 5)  # Increased y-axis range to better show oscillations and resonance peaks

# Adjusting the x-axis limits to zoom in on the relevant region (0 to 2.5)
plt.xlim(0.0, 2.5)  # Adjusted range for better focus

# Removing all gridlines except y=0
plt.grid(axis='y', linestyle='-', linewidth=0.5)  # Only horizontal gridlines at y=0

# Removing numerical values from axes except the zero values
plt.xticks([0])  # Only show 0 on x-axis
plt.yticks([0])  # Only show 0 on y-axis

# Save the plot as a PDF
plt.tight_layout()
plt.savefig("fig_sol_3.4c.pdf")

# Show the plot
plt.show()
