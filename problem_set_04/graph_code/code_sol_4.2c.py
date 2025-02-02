import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Parameters for the pulse equation
b = 1  # amplitude parameter
u = 1  # wave speed
delta_t = 0.5  # small time shift

# Define the function y(x, t)
def y(x, t=0, b=1, u=1):
    return b**3 / (b**2 + (2*x - u*t)**2)

# Generate x values and calculate y for t=0 and shifted time
x_values = np.linspace(-5, 5, 500)
y_original = y(x_values, t=0, b=b, u=u)
y_shifted = y(x_values, t=delta_t, b=b, u=u)

# Create a plot
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x_values, y_original, color="blue", label=r"$y(x, 0)$")
ax.plot(x_values, y_shifted, color="red", label=r"$y(x, \Delta t)$")

# Add title and labels
ax.set_title("Pulse Profile and Its Shift", fontsize=14)
ax.set_xlabel("$x$", fontsize=12)
ax.set_ylabel("$y(x, t)$", fontsize=12)
ax.grid(True)
ax.legend(fontsize=12)

# Save to a PDF
pdf_path = "fig_sol_4.2c.pdf"
with PdfPages(pdf_path) as pdf:
    pdf.savefig(fig)

print(f"PDF saved as {pdf_path}")
