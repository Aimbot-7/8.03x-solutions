import numpy as np
import matplotlib.pyplot as plt

# Define parameters
x = np.linspace(0, np.pi, 100)  # X values from 0 to π
n_values = [1, 2, 3, 4, 5]  # Different mode numbers

fig, axes = plt.subplots(len(n_values), 2, figsize=(8, 10))  # Create subplots

for i, n in enumerate(n_values):
    y = np.sin(n * x)  # Generate smooth sine wave
    
    # Left column: smooth sine wave
    axes[i, 0].plot(x, y, 'k')  # Smooth wave
    axes[i, 0].axhline(0, color='black', linestyle='dashed')  # Dashed centerline
    axes[i, 0].set_ylim(-1.2, 1.2)
    axes[i, 0].set_xticks([])
    axes[i, 0].set_yticks([])
    axes[i, 0].set_frame_on(False)
    axes[i, 0].text(-0.2, 0, f"n={n}", fontsize=12, verticalalignment='center')

    # Right column: Correct piecewise linear approximation
    num_points = n + 2  # Number of discrete points (nodes)
    sample_x = np.linspace(0, np.pi, num_points)  # Sampled x values
    sample_y = np.sin(n * sample_x)  # Corresponding y values

    # Plot nodes (circle markers)
    axes[i, 1].plot(sample_x, sample_y, 'ko')  

    # Draw straight-line segments connecting the nodes
    axes[i, 1].plot(sample_x, sample_y, 'k-')  

    axes[i, 1].axhline(0, color='black', linestyle='dashed')  # Dashed centerline
    axes[i, 1].set_ylim(-1.2, 1.2)
    axes[i, 1].set_xticks([])
    axes[i, 1].set_yticks([])
    axes[i, 1].set_frame_on(False)

# Adjust layout and save as PDF
plt.tight_layout()
plt.savefig("fig_sol_4.6d.pdf", format="pdf", bbox_inches="tight")
plt.show()
