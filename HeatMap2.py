import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.DataFrame({'Normalized Coefficients': [0.0361, -0.0266, -0.0000526, -0.0105, 0.0000413, 0.00115, 0.000177, 0.00116]}, index = ["days_last_order","total_orders","total_value","unique_days_visited","total_sessions","avg_duration_btw_login","avg_session_time","avg_page_visits"])
print(data.head())
plt.subplots(figsize=(1, 9))
sns.heatmap(data, annot=True, cmap="YlOrBr")
plt.title("Heat Map of Normalized Model Coefficients")
plt.show()