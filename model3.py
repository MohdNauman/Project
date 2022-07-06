

import pandas as pd
import matplotlib.pyplot as plt
import pickle

data = pd.read_csv(r'C:\Users\nauman\Desktop\New folder3\features.csv')

data.columns
data.info()

data = data.drop(['sr'], axis = 1)

data = pd.get_dummies(data, columns = ["certification", "placement"], drop_first = True)

X = data.loc[:, data.columns!="price"]

Y = data['price']

from sklearn.model_selection import train_test_split

Xtrain , Xtest , Ytrain , Ytest = train_test_split(X,Y, test_size= 0.3, random_state = 0 )

from sklearn.linear_model import LinearRegression

ln = LinearRegression()
ln.fit(Xtrain, Ytrain)

y_pred = ln.predict(Xtest)

from sklearn.metrics import r2_score

score = r2_score(Ytest , y_pred)

pickle.dump(ln, open('model3.pkl', 'wb'))

model = pickle.load(open('model3.pkl', 'rb'))
print(model.predict([[3000,	50000,	140000,	4500,	2000,	300	,2500,	80000,	9000,	200,	2000,	0, 1]]))
 





























