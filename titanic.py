#import numpy as np
import pandas as pd

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

#remove tables not being considered
train = train.drop(['Name','SibSp','Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],axis=1)
test = test.drop(['Name','SibSp','Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],axis=1)

#male/female to 0/1
for df in [train]:
    df['Sex'] = df['Sex'].map({'female':0,'male':1})

#fill n/a in as 0
train['Age'] = train['Age'].fillna(0)
test['Age'] = test['Age'].fillna(0)

features = ['Pclass','Age','Sex']
target = 'Survived'

print(train[features].head(3))