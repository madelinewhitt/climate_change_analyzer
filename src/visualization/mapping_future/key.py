import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Define a color map for different disaster types
disaster_colors = {
    'Earthquake': 'red',
    'Flood': 'blue',
    'Storm': 'green',
    'Drought': 'orange',
    'Volcanic activity': 'purple'
}

# Create a new figure
plt.figure(figsize=(8, 6))  # Increased figure size for larger legend

# Create legend handles
handles = [mpatches.Patch(color=color, label=disaster) for disaster, color in disaster_colors.items()]

# Create the legend with disaster types, centered and with a larger font size
plt.legend(handles=handles, title="Disaster Types", loc='center', fontsize=14, title_fontsize=16, bbox_to_anchor=(0.5, 0.5))

# Set the title and axis labels (optional)
plt.axis('off')  # Turn off axis

# Save the plot to a file
output_path = "disaster_types_key.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')

# Close the figure to free memory
plt.close()

print(f"Key saved as {output_path}")
