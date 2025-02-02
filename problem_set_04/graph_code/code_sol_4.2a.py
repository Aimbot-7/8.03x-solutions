import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Parameters for the pulse equation
b = 1  # amplitude parameter
u = 1  # wave speed

# Define the function y(x, t)
def y(x, t=0, b=1, u=1):
    return b**3 / (b**2 + (2*x - u*t)**2)

# Generate x values and calculate y for t=0
x_values = np.linspace(-5, 5, 500)
y_values = y(x_values, t=0, b=b, u=u)

# Create a plot
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x_values, y_values, color="blue")
ax.set_title("Pulse Profile at $t=0$", fontsize=14)
ax.set_xlabel("$x$", fontsize=12)
ax.set_ylabel("$y(x, t=0)$", fontsize=12)
ax.grid(True)

# Save to a PDF
pdf_path = "fig_sol_4.2a.pdf"
with PdfPages(pdf_path) as pdf:
    pdf.savefig(fig)

print(f"PDF saved as {pdf_path}")
