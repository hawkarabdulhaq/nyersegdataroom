import streamlit as st

st.set_page_config(page_title="Nyerseg Data Room", layout="wide")

st.title("Nyerseg Data Room")
st.sidebar.title("Navigation")

# Display the sidebar navigation options
st.sidebar.write("Select a page:")
st.sidebar.write("1. Clean SHP")
st.sidebar.write("2. Generate Wells")
st.sidebar.write("3. Reduce Wells")

st.write("Welcome to the Nyerseg Data Room App! Select a page from the sidebar to proceed.")
