import streamlit as st

def page_4():
    st.title("Halaman 4")
    st.write('Halaman ini digunakan untuk menghitung Luas Persegi Panjang')
    
    panjang = st.number_input("Masukkan Nilai Panjang", 0)
    lebar = st.number_input("Masukkan Nilai Lebar", 0)
    hitung = st.button("Hitung Luas")
    
    if hitung :
        luas = panjang * lebar
        st.success(f"Luas Persegi Panjang Adalah = {luas}")