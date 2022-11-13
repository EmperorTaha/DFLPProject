import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt
plt.rc("font", size=14)
import seaborn as sns
sns.set(style="white") #white background style for seaborn plots
sns.set(style="whitegrid", color_codes=True)
from scipy import stats

import warnings
warnings.simplefilter(action='ignore')

from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE

train = pd.read_csv("dflp_case_sample_data.csv")
train.head()

print('The number of samples into the train data is {}.'.format(train.shape[0]))


cols = ["days_last_order","total_orders","total_value","unique_days_visited","total_sessions","avg_duration_btw_login","avg_session_time","avg_page_visits"]
X = train[cols]
y = train['label']
# Build a logreg and compute the feature importances
model = LogisticRegression()
# create the RFE model and select 8 attributes
rfe = RFE(model, 8)
rfe = rfe.fit(X, y)
# summarize the selection of the attributes
print('Selected features: %s' % list(X.columns[rfe.support_]))
Selected_features = ["days_last_order","total_orders","total_value","unique_days_visited","total_sessions","avg_duration_btw_login","avg_session_time","avg_page_visits","label"]
X = train[Selected_features]
#sns.scatterplot(x=train['unique_days_visited'], y=train['label'], hue=train['label'])
#plt.show()
#plt.figure(figsize=(15,8))
#ax = sns.kdeplot(train["total_sessions"][train.label == 1], color="darkturquoise", shade=True)
#sns.kdeplot(train["total_sessions"][train.label == 0], color="lightcoral", shade=True)
#plt.legend(['Churned', 'Retained'])
#plt.title('Density Plot of Total Sessions and Customer Retention')
#ax.set(xlabel='Total Sessions')

#sns.barplot(x='class', y='frequencies', data=train, palette='pastel')

# Plot histogram
#sns.histplot(data=train, x="label", stat="probability", binwidth=0.2, discrete=False)
#plt.show()
corre = X.corr()
print(corre.head(9))
YASS = corre['label']
YASS = YASS[:8]

plt.subplots(figsize=(1, 9))
sns.heatmap(YASS.to_frame(), annot=True, cmap="Greys")
plt.title("Heat Map of Pearson's Coorelation")
plt.show()


