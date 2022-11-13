import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.DataFrame({'Pearson Correlation Coefficient': [0.142,-0.125,-0.070,-0.174,-0.142,0.0592,0.0234,0.0120]}, index = ["days_last_order","total_orders","total_value","unique_days_visited","total_sessions","avg_duration_btw_login","avg_session_time","avg_page_visits"])
print(data.head())
plt.subplots(figsize=(1, 9))
sns.heatmap(data, annot=True, cmap="YlOrBr")
plt.title("Heat Map of Pearson's Correlation Coefficient")
plt.show()