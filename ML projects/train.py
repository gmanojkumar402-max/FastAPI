import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("housing.csv").iloc[:,:-1].dropna()
X = df.drop(columns = "median_house_value")
y = df.median_house_value.copy()

linearregression = LinearRegression().fit(X,y)
print("Trained the model")
# now trained model is to saved and serialized

joblib.dump(linearregression,'linearregression.joblib')
# model saved 


