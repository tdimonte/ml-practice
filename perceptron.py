import pandas as pd

#read, features and labels
df = pd.read_csv('nonlinear.csv')

#to numpy array, split features and labels
csv_array = df.to_numpy()
features = csv_array[:, [0, 1, 2, 3]]
labels = csv_array[:, [4]]

#initialize weights
w = [0.1, 0.1, 0.1, 0.1]

#initialize threshold
threshold = 0.5

#initialize learning rate
learn_rate = 0.1

#initialize epoch times
epoch = 200

#use step fucntion (activation function)
def predict(sum):
    if sum > threshold:
        ans = 1
        return int(ans)
    else:
        ans = 0
        return int(ans)

#features.shape returns size of array ... (40)
for j in range(0, epoch):
    print('epoch ', j)

    for i in range(0, features.shape[0]):
        f = features[i]
        label = labels[i]

        x0 = f[0]
        x1 = f[1]
        x2 = f[2]
        x3 = f[3]

        sum = x0 * w[0] + x1 * w[1] + x2 * w[2] + x3 * w[3]

        predict(sum)
        error = int(label) - predict(sum)

        print('prediction: ', predict(sum), 'label: ', int(label), 'error: ', error)
        #print(type(sum))

        w[0] = w[0] + error * learn_rate
        w[1] = w[1] + error * learn_rate
        w[2] = w[2] + error * learn_rate
        w[3] = w[3] + error * learn_rate

    print('---------------------------------------')


