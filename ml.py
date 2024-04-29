# Import the libraries
import pandas as pd
import pickle
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing

# Load the csv file
df = pd.read_csv('crop_recommendation.csv')

# Instantiate the model
model = KNeighborsClassifier(n_neighbors=5)

# Select the independent variable
features = list(zip(df["N"], df["P"], df["K"], df["temperature"], df["humidity"], df["ph"], df["rainfall"]))

# Fit the model
model.fit(features,df["crop"])

# Save the model in a pickle file
pickle.dump(model, open('model.pkl','wb'))
