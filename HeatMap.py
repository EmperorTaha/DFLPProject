import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.DataFrame({'Coefficients': [0.00616, -0.00104, -0.0000000303, -0.00184, 0.0000905, -0.00157, 0.0000367, 0.0000434]}, index = ["days_last_order","total_orders","total_value","unique_days_visited","total_sessions","avg_duration_btw_login","avg_session_time","avg_page_visits"])
print(data.head())
plt.subplots(figsize=(1, 9))
sns.heatmap(data, annot=True, cmap="YlOrBr")
plt.title("Heat Map of Model Coefficients")
plt.show()