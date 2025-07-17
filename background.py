import streamlit as st
import base64

def set_background(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-attachment: fixed;
            background-repeat: no-repeat;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
