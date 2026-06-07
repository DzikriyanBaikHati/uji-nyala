import streamlit as st
import time
import plotly.graph_objects as go

st.set_page_config(
    page_title="ChemLab Interactive",
    page_icon="🧪",
    layout="wide"
)

# CSS Custom
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #e3f2fd, #f1f8e9);
}

.main-title{
    text-align:center;
    font-size:45px;
    color:#1565c0;
    font-weight:bold;
}

.card{
    padding:20px;
    border-radius:15px;
    background:white;
    box-shadow:0px 4px 15px rgba(0,0,0,0.1);
}

.footer{
    text-align:center;
    color:gray;
    padding-top:20px;
}
</style>
""", unsafe_allow_html=True)
