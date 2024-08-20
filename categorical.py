import pandas as pd
import matplotlib.pyplot as plt

file_path = 'sample_dataset.xlsx'
data = pd.read_excel(file_path)

plt.figure(figsize=(10, 6))
plt.hist(data['Age'], bins=10, color='blue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
gender_counts = data['Gender'].value_counts()
gender_counts.plot(kind='bar', color=['blue', 'pink'])
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Number of Individuals')
plt.xticks(rotation=0)
plt.grid(True)
plt.show()
