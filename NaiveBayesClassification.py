import pandas as pd
import pickle
import numpy as np

from sklearn.naive_bayes import CategoricalNB, BernoulliNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder

mushroom = pd.read_csv("jamur.csv")
df = mushroom.copy()

target = 'class'
encode = ['cap_shape', 'cap_surface', 'cap_color', 'odor',
          'gill_spacing', 'gill_size', 'gill_color',
          'stalk_shape', 'stalk_root', 'stalk_surface_above_ring',
          'stalk_surface_below_ring', 'stalk_color_above_ring',
          'stalk_color_below_ring', 'veil_color', 'ring_number',
          'ring_type', 'spore_print_color', 'population', 'habitat']

for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df,dummy], axis=1)
    del df[col]

target_mapper = {'e':0, 'p':1}
def target_encode(val):
    return target_mapper[val]

df['class'] = df['class'].apply(target_encode)

X = df.drop('class', axis=1)
Y = df['class']

cn = CategoricalNB()
cn.fit(X, Y)

pickle.dump(cn, open('bissmillah.pkl', 'wb'))

