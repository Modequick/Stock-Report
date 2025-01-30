import streamlit as st
import random
from function_list import scorecard
from datetime import datetime, timedelta


st.markdown("<h1 style='text-align: center;'>Stock Automated Report</h1>",unsafe_allow_html=True)

st.markdown("<h3 style='text-align:center'> Keep you updated about the stock </h3>",unsafe_allow_html=True)

option = st.selectbox(
    "List of Stock:",  # Dropdown label
    ["IHSG","BBCA"]  # Options
)

opt1, opt2 = st.columns(2)
with opt1:
    date_range = st.date_input(
        "Select Date Range",
        value=(datetime.today() - timedelta(days=30), datetime.today()),  # Default: last 7 days
        format="YYYY-MM-DD")
with opt2 : 
    st.selectbox("Granularity",["Daily","Weekly","Monthly"])


st.markdown(
    "<div style='display: flex; justify-content: center;'>"
    "<button style='padding: 10px 20px; font-size: 16px;'>Generate</button>"
    "</div>",
    unsafe_allow_html=True
)


st.write("")

col1, col2, col3  = st.columns(3)
with col1 : 
    st.markdown(scorecard ("Market Cap", option),unsafe_allow_html = True)
with col2 :
    st.markdown(scorecard ("% Market Cap", 123),unsafe_allow_html = True)
with col3 :
    st.markdown(scorecard ("Rank", 123),unsafe_allow_html = True)