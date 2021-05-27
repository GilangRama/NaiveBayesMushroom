import streamlit as st
import pandas as pd
import pickle
from sklearn.naive_bayes import CategoricalNB
import numpy as np

uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
    def user_input_feature():
        cap_shape = st.sidebar.selectbox('cap_shape', ('b', 'c', 'x', 'f', 'k', 's'))
        cap_surface = st.sidebar.selectbox('cap_surface', ('f', 'g', 'y', 's'))
        cap_color = st.sidebar.selectbox('cap_color', ('n', 'b', 'c', 'g', 'r', 'p', 'u', 'e', 'w', 'y'))
        odor = st.sidebar.selectbox('odor', ('a', 'l', 'c', 'y', 'f', 'm', 'n', 'p', 's'))
        gill_spacing = st.sidebar.selectbox('gill_spacing', ('c', 'w', 'd'))
        gill_size = st.sidebar.selectbox('gill_size', ('b', 'n'))
        gill_color = st.sidebar.selectbox('gill_color', ('k', 'n', 'b', 'h', 'g', 'r', 'o', 'p', 'u', 'e', 'w', 'y'))
        stalk_shape = st.sidebar.selectbox('stalk_shape', ('e', 't'))
        stalk_root = st.sidebar.selectbox('stalk_root', ('b', 'c', 'u', 'e', 'z', 'r', '?'))
        stalk_surface_above_ring = st.sidebar.selectbox('stalk_surface_above_ring', ('f', 'y', 'k', 's'))
        stalk_surface_below_ring = st.sidebar.selectbox('stalk_surface_below_ring', ('f', 'y', 'k', 's'))
        stalk_color_above_ring = st.sidebar.selectbox('stalk_color_above_ring', ('n', 'b', 'c', 'g', 'o', 'p', 'e', 'w', 'y'))
        stalk_color_below_ring = st.sidebar.selectbox('stalk_color_below_ring', ('n', 'b', 'c', 'g', 'o', 'p', 'e', 'w', 'y'))
        veil_color = st.sidebar.selectbox('veil_color', ('n', 'o', 'w', 'y'))
        ring_number = st.sidebar.selectbox('ring_number', ('n', 'o', 't'))
        ring_type = st.sidebar.selectbox('ring_type', ('c', 'e', 'f', 'l', 'n', 'p', 's', 'z'))
        spore_print_color = st.sidebar.selectbox('spore_print_color', ('k', 'n', 'b', 'h', 'r', 'o','u', 'w', 'y'))
        population = st.sidebar.selectbox('population', ('a', 'c', 'n', 's', 'v', 'y'))
        habitat = st.sidebar.selectbox('habitat', ('g', 'l', 'm', 'p', 'u', 'w', 'd'))
        data = {'cap_shape' : cap_shape,
                'cap_surface' : cap_surface,
                'cap_color' : cap_color,
                'odor' : odor,
                'gill_spacing' : gill_spacing,
                'gill_size' : gill_size,
                'gill_color' : gill_color,
                'stalk_shape' : stalk_shape,
                'stalk_root' : stalk_root,
                'stalk_surface_above_ring' : stalk_surface_above_ring,
                'stalk_surface_below_ring' : stalk_surface_below_ring,
                'stalk_color_above_ring' : stalk_color_above_ring,
                'stalk_color_below_ring' : stalk_color_below_ring,
                'veil_color' : veil_color,
                'ring_number' : ring_number,
                'ring_type' : ring_type,
                'spore_print_color' : spore_print_color,
                'population' : population,
                'habitat' : habitat}
        feature = pd.DataFrame(data, index=[0])
        return feature
    input_df = user_input_feature()

mushroom_raw = pd.read_csv('jamur.csv')
mushroom = mushroom_raw.drop(columns=['class'])
df = pd.concat([input_df, mushroom], axis=0)

# encode
encode = ['cap_shape', 'cap_surface', 'cap_color', 'odor',
          'gill_spacing', 'gill_size', 'gill_color',
          'stalk_shape', 'stalk_root', 'stalk_surface_above_ring',
          'stalk_surface_below_ring', 'stalk_color_above_ring',
          'stalk_color_below_ring', 'veil_color', 'ring_number',
          'ring_type', 'spore_print_color', 'population', 'habitat']
for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df, dummy], axis=1)
    del df[col]
df = df[:1]

# display user input
st.subheader('User Input features')

if uploaded_file is not None:
    st.write(df)
else:
    st.write('Awaiting CSV file to be uploaded. Currently using example input parameters (shown below).')
    st.write(df)

load_cn = pickle.load(open('bissmillah.pkl', 'rb'))

try:
    prediction = load_cn.predict(df)
except ValueError:
    st.error('Please enter valid format')

try:
    prediction_proba = load_cn.predict_proba(df)
except ValueError:
    st.error('Please enter valid input')

prediction = load_cn.predict(df)
prediction_proba = load_cn.predict_proba(df)

st.subheader('Prediction')
mushroom_class = np.array(['e', 'p'])
st.write(mushroom_class[prediction])

st.subheader('Prediction Proba')
st.write(prediction_proba)




