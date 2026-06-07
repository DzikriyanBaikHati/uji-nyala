import streamlit as st

st.set_page_config(
    page_title="ChemLearN Hub",
    page_icon="🧪",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
    background: linear-gradient(
    135deg,
    #0f172a,
    #1e293b,
    #111827);
    color:white;
}

.main-title{
    text-align:center;
    font-size:55px;
    font-weight:bold;
    background: linear-gradient(90deg,#38bdf8,#22c55e,#f97316);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.card{
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(15px);
    padding:25px;
    border-radius:20px;
    border:1px solid rgba(255,255,255,0.2);
    margin-bottom:20px;
}

.card:hover{
    transform:scale(1.02);
    transition:0.3s;
}

.badge{
    background:#22c55e;
    padding:5px 12px;
    border-radius:20px;
    color:white;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)
