import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Given constants
V0 = 3  # volts
R = 50  # ohms
L = 100e-3  # henries
C = 0.01e-6  # farads

# Derived constants
gamma = R / L  # damping coefficient
omega_0 = 1 / np.sqrt(L * C)  # natural frequency

# Angular frequency range
omega = np.linspace(0, 2 * omega_0, 1000)

# Current amplitude
I0 = (omega * V0 / L) / np.sqrt((omega_0**2 - omega**2)**2 + (gamma * omega)**2)

# Create a PDF file to save the plot
pdf_file = "fig_sol_2.5d.pdf"
with PdfPages(pdf_file) as pdf:
    # Plotting
    plt.figure(figsize=(12, 8))
    plt.plot(omega, I0, label="Current Amplitude $I_0$", color='b')

    # Titles and labels
    plt.title("Amplitude of Current $I_0$ vs Angular Frequency $\\omega$", fontsize=18)
    plt.xlabel("Angular Frequency $\\omega$ (rad/s)", fontsize=16)
    plt.ylabel("Amplitude of Current $I_0$ (A)", fontsize=16)
    plt.axvline(x=omega_0, color='r', linestyle='--', label="Resonance Frequency $\\omega_0$")

    # Adjust tick parameters for larger text
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)

    # Additional information
    plt.grid(True)
    plt.legend(fontsize=14)
    plt.tight_layout()

    # Save the current figure to the PDF
    pdf.savefig()
    plt.close()

print("The plot has been saved to {pdf_file}")
