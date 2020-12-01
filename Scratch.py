import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('darkgrid', {"axes.facecolor": ".8"})

# To show that data is skewed

skewed = pd.read_csv('PredictiveData/HI_Pred_train.csv')
sns.countplot(skewed.Response)
plt.show()

# To show unskewed data

unskewed = pd.read_csv('PredictiveData/HI_Pred_Balanced_Train.csv')
sns.countplot(unskewed.Response)
plt.show()

