import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import sklearn.metrics as metrics 
from sklearn.linear_model import LogisticRegression 
import numpy as np 
data = pd.read_csv('Crop_recommendation.csv')


features = data[['N', 'P', 'K', 'temperature', 
                 'humidity', 'ph']] 
  
labels = data['label'] 

model = DecisionTreeClassifier()

X_train, X_test, Y_train, Y_test = train_test_split(features, 
                                       labels, 
                                       test_size=0.2, 
                                       random_state=42) 
LogReg = LogisticRegression(random_state=42).fit(X_train, Y_train) 
predicted_values = LogReg.predict(X_test)
accuracy = metrics.accuracy_score(Y_test, 
                                  predicted_values) 
print("Logistic Regression accuracy: ", accuracy)

def recommend_crop(N, P, K,ph, temperature, humidity):
    try:
        N = int(N)
        P = int(P)
        K = int(K)
        ph = int(ph)
        temperature = float(temperature)
        
        input_data = [[N, P, K , temperature, humidity,ph]]
        predicted_crop = LogReg.predict(input_data)
        # predicted_crop = model.predict(input_data)
        print(predicted_crop[0])
        print("Recommended Crop is:", predicted_crop[0])
        return predicted_crop[0]
    except Exception as e:
        print(e)
        return "error"

