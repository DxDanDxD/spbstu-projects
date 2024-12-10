import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file = 'C:\Users\User\spbstu-projects\Mall_Customers.csv'
data = pd.read_csv(file)
data.head(), data.info()

'''nomer 2'''

average_income_women = data[data['Genre'] == 'Female']['Annual Income (k$)'].mean()

'''nomer 3'''

highest_spender_male = data[data['Genre'] == 'Male'].sort_values(by='Spending Score (1-100)', ascending=False).iloc[0]
highest_spender_female = data[data['Genre'] == 'Female'].sort_values(by='Spending Score (1-100)', ascending=False).iloc[0]

'''nomer 4'''

male_data = data[data['Genre'] == 'Male']
plt.figure(figsize=(10, 6))
sns.lineplot(x='Age', y='Annual Income (k$)', data=male_data, marker='o', color='blue')
plt.title('Male income dependencies:')
plt.xlabel('Age')
plt.ylabel('Yearly income:')
plt.grid(True)
plt.show()

'''nomer 5'''

plt.figure(figsize=(12, 8))
sns.histplot(data=data, x='Annual Income (k$)', hue='Genre', weights='Spending Score (1-100)', multiple='dodge', kde=False, palette={'Male': 'blue', 'Female': 'pink'}, bins=15)
plt.title('Dependencies of spendings from income:')
plt.xlabel('Yearly spendings:')
plt.ylabel('General spending:')
plt.grid(axis='y')
plt.show()
print(average_income_women, highest_spender_male, highest_spender_female)
