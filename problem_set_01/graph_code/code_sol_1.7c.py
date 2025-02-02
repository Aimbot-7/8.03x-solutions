import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define symbolic variables
t, s_0, gamma, alpha = sp.symbols('t s_0 gamma alpha')

# Define the function s(t)
s = (s_0 * (1/2 - gamma/(4*alpha)) * sp.exp(-t * (gamma/2 + alpha)) +
     s_0 * (1/2 + gamma/(4*alpha)) * sp.exp(-t * (gamma/2 - alpha)))

# Convert symbolic function to a numeric function for plotting
s_numeric = sp.lambdify((t, s_0, gamma, alpha), s, modules=['numpy'])

# Define parameter values
omega_0_value = (3/7) * np.pi  # omega_0 = 3/7 * pi
gamma_value = 3  # gamma = 3
s_0_value = 1  # s_0 = 1
alpha_value = np.sqrt((gamma_value**2)/4 - omega_0_value**2)  # Calculate alpha

# Time values for plotting (extended to allow asymptotic approach to zero)
t_values = np.linspace(0, 10, 1000)  # Time range from 0 to 10 seconds

# Compute s(t) values
s_values = s_numeric(t_values, s_0_value, gamma_value, alpha_value)

# Set global font size settings
plt.rcParams.update({
    "font.size": 18,  # Default font size
    "axes.titlesize": 22,  # Title font size
    "axes.labelsize": 20,  # X and Y label size
    "xtick.labelsize": 18,  # X-axis tick label size
    "ytick.labelsize": 18,  # Y-axis tick label size
})

# Plot the function
plt.figure(figsize=(8, 10))  # Increased figure height for better vertical scaling
plt.plot(t_values, s_values, label=r'$s(t)$')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')

# Set axis labels and title using LaTeX
plt.xlabel("$t$ (seconds)")
plt.ylabel("$s(t)$")
plt.title("Overdamped Response of the Pen")

# Set x-ticks at a reasonable interval
plt.xticks(np.arange(0, 11, 1))  # X-axis values from 0 to 10 with a step of 1

# Set y-ticks to show amplitude in symbolic form
y_ticks = np.linspace(0, s_0_value, 6)  # 6 ticks from 0 to s_0
y_tick_labels = [f"${round(y, 2)}$" for y in y_ticks]  # Format the y-ticks nicely
plt.yticks(y_ticks, y_tick_labels)

# Add grid with lighter opacity for better visibility
plt.grid(alpha=0.4)

# Save the plot as a high-quality PDF
plt.savefig("fig_sol_1.7c.pdf", format="pdf", dpi=300)

# Show the plot
plt.tight_layout()
plt.show()
