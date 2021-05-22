import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import pickle


data  = pd.read_csv("IRIS.csv")
x = data.drop(['species'], axis=1)
y =data['species']

x_train, x_test, y_train, y_test = train_test_split(x, y)

lr = LogisticRegression()
lr.fit(x_train, y_train)


with open('iris_save.pkl', 'wb') as f:
    pickle.dump(lr, f)

# lg = pickle.load(open('iris_save.pkl', 'rb'))
# print(lg.predict([[1, 1 ,1, 1]]))