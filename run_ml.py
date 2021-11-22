import pandas as pd
import pickle
from imblearn.ensemble import BalancedRandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def predictions(month, tourist, location):
    loaded_model = pickle.load(open("disney_branch.pkl", 'rb'))

    return loaded_model.predict([[5, month, 2022, tourist, location]])