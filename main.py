# import streamlit as st
# import pandas as pd
# import seaborn as sns

# df = sns.load_dataset("iris")
# st.write(df)
# st.write("Hello World")
# st.title("My title")
# #st.image("./ram3.jpg")
# st.number_input("Pick a number", 0, 10)
# st.date_input("Your Birthday")
# st.slider("Slider it:", 0, 100, 25)
# # st.file_uploader("Upload a CSV")
# with st.sidebar:
#     st.text_input("Filter by name")
#     st.selectbox("Sort by",["A-Z","Z-A"])
#     st.file_uploader("Upload a CSV")


import streamlit as st
#import seaborn as sns
import pandas as pd

# st.title("data visualization")
st.set_page_config(page_title="data visualization",page_icon="😂")


st.write("HI this is new chnages")

st.title("Data visulizatinon with streamlit")

with st.sidebar:

	upload = st.file_uploader("upload csv")
if upload is not None:
	df = pd.read_csv(upload)
	st.dataframe(df.head())