#import numpy as np
import pandas as pd

# ------------------------------------------------------------------------------- DataFrame 

train = pd.read_csv('train.csv')

#remove columns not being considered
train = train.drop(['Name','SibSp','Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],axis=1)

#add Alive (my custom prediction column calculated to guess if they survived)
train['Alive'] = '1'

#male/female to 0/1
for df in [train]:
    df['Sex'] = df['Sex'].map({'female':0,'male':1})

#fill n/a in as 0
train['Age'] = train['Age'].fillna(0)

#turn str data into int data
train['Pclass'] = pd.to_numeric(train['Pclass'])
train['Age'] = pd.to_numeric(train['Age'])
train['Sex'] = pd.to_numeric(train['Sex'])
train['Alive'] = pd.to_numeric(train['Alive'])

# ------------------------------------------------------------------------------- Prediction

#global variables
passengers = len(train)
alive_count = 0

# #create boolean mask of passengers predicted to die
# #predicted_to_die if 3rd class, non-child, and male
# predicted_to_die = (train[passengers].Pclass > 2) & (train[passengers].Age > 18) & (train[passengers].Sex > 0)

# #selects rows and updates column
# train[passengers]['Alive'][predicted_to_die] = 0

#iterate through passenger rows
for index, row in train.iterrows():
    if (train.at[index,'Pclass'] > 2):
        train.at[index,'Alive'] = 0

    if (train.at[index,'Age'] > 18):
        train.at[index,'Alive'] = 0

    if (train.at[index,'Sex'] > 0):
        train.at[index,'Alive'] = 0

alive_count = train['Alive'].sum()

for index, row in train.iterrows():
    if (train.at[index,'Alive'] == 1):
        print(row['Pclass'],row['Age'],row['Sex'])

print(f'Out of {passengers} passengers. Only {alive_count} survived.')

prediction = pd.DataFrame({'PassengerId':train['PassengerId'],'Alive':train['Alive']})

filename = 'Predicitons.csv'
prediction.to_csv(filename, index=False)
