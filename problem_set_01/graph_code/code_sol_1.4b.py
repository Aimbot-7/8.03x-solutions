import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define symbolic variables and function
t, T, B = sp.symbols('t T B')
v = B * sp.cos(2 * sp.pi * t / T)  # Function: v(t) = B * cos(2πt/T)

# Convert symbolic function to a numeric function for plotting
v_numeric = sp.lambdify((t, T, B), v, modules=['numpy'])

# Generate data for one period
T_value = 1  # Assign a value for T (symbolic representation still used in labels)
B_value = 1  # Assign a value for B (symbolic representation used in labels)
t_values = np.linspace(0, T_value, 1000)
v_values = v_numeric(t_values, T_value, B_value)

# Set global font size settings
plt.rcParams.update({
    "font.size": 14,  # Default font size
    "axes.titlesize": 18,  # Title font size
    "axes.labelsize": 16,  # X and Y label size
    "xtick.labelsize": 14,  # X-axis tick label size
    "ytick.labelsize": 14,  # Y-axis tick label size
    "legend.fontsize": 14,  # Legend font size (if used)
})

# Plot the function
plt.figure(figsize=(8, 4))
plt.plot(t_values, v_values)
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')

# Set axis labels and title using LaTeX
plt.xlabel("$t$")
plt.ylabel("$v(t)$")
plt.title("Plot of $v(t)$ for One Period")

# Set x-ticks in terms of T
x_ticks = [0, 0.25*T_value, 0.5*T_value, 0.75*T_value, T_value]
x_tick_labels = [r"$0$", r"$0.25T$", r"$0.5T$", r"$0.75T$", r"$T$"]
plt.xticks(x_ticks, x_tick_labels)

# Set y-ticks to show amplitude
y_ticks = [-B_value, 0, B_value]
y_tick_labels = [r"$-B$", r"$0$", r"$B$"]
plt.yticks(y_ticks, y_tick_labels)

# Add grid
plt.grid(alpha=0.3)

# Save the plot as a high-quality PDF
plt.savefig("fig_sol_1.4b", format="pdf", dpi=300)

# Show the plot
plt.tight_layout()
plt.show()
