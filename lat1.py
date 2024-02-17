import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("mutisa")
df = pd.DataFrame({
    'No': [1,2,3,4],
    'Nama': ['ucup','acep','acip','acup'],
    'nilai': [100, 100, 100, 100]
})

df
