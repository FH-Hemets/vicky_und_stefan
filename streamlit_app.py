import streamlit as st

photo = st.camera_input("Foto machen")
file = st.file_uploader('Foto hochladen')
