import pandas as pd

data = pd.DataFrame({'Churn': [0, 1], 'Frequency': [3849, 958]})
print(data.head())
import seaborn as sns
import matplotlib.pyplot as plt

# read a titanic.csv file
# from seaborn libraray

# who v/s fare barplot
sns.barplot(x='Churn',
            y='Frequency',
            data=data, color='darkorange')
plt.title("Customer Churned in Sample Data")
# Show the plot
plt.show()