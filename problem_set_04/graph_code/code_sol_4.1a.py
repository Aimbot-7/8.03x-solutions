import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Define the spatial range for the string
x = np.linspace(45, 55, 500)  # Zoomed in around the pulse (45 m to 55 m)

# Define the pulse shape (simplified model)
pulse = -np.exp(-((x - 50) / 1)**2)  # Gaussian pulse centered at 50 m

# Calculate transverse velocity (derivative of pulse)
transverse_velocity = -2 * (x - 50) * pulse  # Derivative of the pulse w.r.t. x

# Create the plot
fig, ax = plt.subplots(figsize=(8, 6))

# Transverse velocity curve
ax.plot(x, transverse_velocity, color="blue", linestyle="solid")

# Formatting the plot
ax.axhline(0, color="black", linewidth=0.8, linestyle="--")  # Horizontal axis
ax.set_title("Transverse Velocity of the String", fontsize=14)
ax.set_xlabel("Position along the string ($x$)", fontsize=12)
ax.set_ylabel("Transverse Velocity", fontsize=12)
ax.grid(True)
ax.set_xticks([])  # Remove numerical values for x-axis

# Save the plot to a PDF
pdf_path = "fig_sol_4.1a.pdf"
with PdfPages(pdf_path) as pdf:
    pdf.savefig(fig)

print(f"PDF saved as {pdf_path}")
