#import streamlit as st
#st.title("Hello")


import streamlit as st

st.title('Home')
st.chat_input('Enter your name: ')
st.button("Click me")
with open("data.txt", "r") as file:
    st.download_button("Download file", file.read(), file_name="data.txt")
st.link_button("Go to gallery", r"C:\Users\USER\Downloads")