import streamlit as st
from page1 import page_1
from page2 import page_2
# import pandas as pd
#import matplotlib.pyplot as plt

# st.write("mutisa")
# df = pd.DataFrame({
#     'No': [1,2,3,4],
#     'Nama': ['ucup','acep','acip','acup'],
#     'nilai': [100, 100, 100, 100]
# })

# df



def page_3():
    st.title("Halaman 3")
    st.write('Halaman ini digunakan untuk Menampilkan Rumus Matematika')
    
PAGES = {
    "Page 1" : page_1,
    "Page 2" : page_2,
    "Page 3" : page_3
}

st.sidebar.image("marsha.jpg", width=200)
page = st.sidebar.radio("Halaman", list(PAGES.keys()))
PAGES[page]()
