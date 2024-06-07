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

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['age'], df['weight'], c=df['color'], s=100, edgecolor='w', alpha=0.7)

# Add titles and labels
plt.title('Scatter Plot of Age vs Weight')
plt.xlabel('Age')
plt.ylabel('Weight')

# Add a legend
handles = [plt.Line2D([0], [0], marker='o', color='w', label='Male', markersize=10, markerfacecolor='blue'),
           plt.Line2D([0], [0], marker='o', color='w', label='Female', markersize=10, markerfacecolor='pink')]
plt.legend(title='Gender', handles=handles)

# Show the plot
plt.show()
