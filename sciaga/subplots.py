import pandas as pd
import matplotlib.pyplot as plt

# Example DataFrame
data = {
    'gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
    'age': [25, 30, 45, 22, 35],
    'weight': [180, 150, 200, 120, 160]
}
df = pd.DataFrame(data)

# Map gender to colors
color_map = {'Male': 'blue', 'Female': 'pink'}
df['color'] = df['gender'].map(color_map)

# Create a figure and two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# First subplot
ax1.scatter(df['age'], df['weight'], c=df['color'], s=100, edgecolor='w', alpha=0.7)
ax1.set_title('Scatter Plot 1')
ax1.set_xlabel('Age')
ax1.set_ylabel('Weight')

# Second subplot
ax2.scatter(df['age'], df['weight'], c=df['color'], s=100, edgecolor='w', alpha=0.7)
ax2.set_title('Scatter Plot 2')
ax2.set_xlabel('Age')
ax2.set_ylabel('Weight')

# Add a legend to the entire figure
handles = [plt.Line2D([0], [0], marker='o', color='w', label='Male', markersize=10, markerfacecolor='blue'),
           plt.Line2D([0], [0], marker='o', color='w', label='Female', markersize=10, markerfacecolor='pink')]
fig.legend(handles=handles, title='Gender', loc='upper right')

plt.ylim(None, 1)  # Set the lower limit to 0 and the upper limit to 1
# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
