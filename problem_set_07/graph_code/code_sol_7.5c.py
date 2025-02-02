import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os

# Define parameters
time = np.linspace(-25, 25, 500)  # Time in seconds
transmitted_frequency = 1000  # Whistle frequency in Hz

# Correct observed frequency curve: higher when approaching, lower when receding
frequency_corrected = 1000 + (60 * np.tanh(-0.15 * time))

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(time, frequency_corrected, color='blue', linewidth=2, label="Observed Frequency")
plt.axhline(y=transmitted_frequency, color='red', linestyle='dashed', linewidth=1.5, label="Transmitted Frequency (t=0)")

# Add titles, labels, grid, and legend
plt.title("Observed Frequency vs. Time for Train Whistle", fontsize=14)
plt.xlabel("Time (s)", fontsize=12)
plt.ylabel("Frequency (Hz)", fontsize=12)
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend(fontsize=10)
plt.tight_layout()

# Save the plot to a PDF in the current working directory
pdf_filename = "fig_sol_7.5c.pdf"
pdf_path = os.path.join(os.getcwd(), pdf_filename)

with PdfPages(pdf_path) as pdf:
    pdf.savefig()  # Save the plot in the PDF
    plt.close()

print(f"PDF saved successfully at: {pdf_path}")
