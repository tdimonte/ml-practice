from sklearn.datasets import make_classification
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
import pandas as pd
import random

#read, features and labels
df1 = pd.read_csv('train.csv')
df2 = pd.read_csv('test.csv')

#randomize data for n-fold cross validation
n = random.randint(1,100)
df1 = df.sample(frac = n)

#grid-search procedure
#grid create
graph_x = []
graph_y = []
graph_z = []

#change arrang(vals) lower and higher based on what you want to test
for alpha_value in df1.arange(-1,0,1):
    alpha_value = pow(10,alpha_value)
    graph_x_row = []
    graph_y_row = []
    graph_z_row = []

#change arrang(vals) lower and higher based on what you want to test
for alpha_value in df2.arange(-1,0,1):
    alpha_value = pow(10,alpha_value)
    graph_x_row = []
    graph_y_row = []
    graph_z_row = []


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

