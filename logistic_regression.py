from sklearn.datasets import make_classification
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
import pandas as pd

#read, features and labels
df1 = pd.read_csv('lr_train1.csv')
df2 = pd.read_csv('lr_train2.csv')

#to numpy array, split features and labels
csv_array1 = df1.to_numpy()
features1 = csv_array1[:, [0, 1, 2, 3]]
labels1 = csv_array1[:, [4]]

csv_array2 = df2.to_numpy()
features2 = csv_array2[:, [0, 1, 2, 3]]
labels2 = csv_array2[:, [4]]

#initialize classifier parameters
class_param = [0.1, 0.1, 0.1, 0.1]

#classification tester
x, y = make_classification(
    n_samples=445
)

#create a scatter plot
plt.scatter(df1, df2, c=y, cmap='rainbow')
plt.title('Logistic Regression')
plt.show()

#create the logistic regression
lr = LogisticRegression()
lr.fit(df1, df2)

