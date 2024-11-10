import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.clean_shp import shape_cleaning_page
from src.generate_wells import generate_wells_page
from src.reduce_wells import reduce_wells_page
from src.final_map import final_map_page

# Import translations for each section
from translations.app import translations as app_translations
from translations.shape_cleaning import translations as shape_cleaning_translations
from translations.generate_wells import translations as generate_wells_translations
from translations.reduce_wells import translations as reduce_wells_translations
from translations.final_map import translations as final_map_translations

# Initialize session state for language if it doesn't exist
if "language" not in st.session_state:
    st.session_state.language = 'en'  # Default to English

# Helper function for translation
def _(text_key, page_translations):
    return page_translations[st.session_state.language].get(text_key, text_key)

# Set page configuration
st.set_page_config(page_title=_(text_key="page_title", page_translations=app_translations), layout="wide")

# Language selection in the sidebar
with st.sidebar:
    language = st.selectbox(
        "Language / Nyelv",
        options=["English", "Magyar"],
        index=0 if st.session_state.language == 'en' else 1
    )
    # Update language in session state based on selection
    st.session_state.language = 'en' if language == "English" else 'hu'

# Title and Welcome Message
st.title(_(text_key="page_title", page_translations=app_translations))
st.markdown(_(text_key="welcome_message", page_translations=app_translations))

# Define the access key
ACCESS_KEY = "Asd456"

# Check if the user has already been authenticated
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Access key input and validation
if not st.session_state.authenticated:
    st.subheader(_(text_key="access_key_prompt", page_translations=app_translations))
    access_key_input = st.text_input(_(text_key="access_key_label", page_translations=app_translations), type="password")
    
    if st.button(_(text_key="access_button", page_translations=app_translations)):
        if access_key_input == ACCESS_KEY:
            st.session_state.authenticated = True
            st.success(_(text_key="access_granted", page_translations=app_translations))
            st.experimental_set_query_params(auth="true")  # This will refresh the page
        else:
            st.error(_(text_key="invalid_key", page_translations=app_translations))

# Main app content
if st.session_state.authenticated:
    # Initialize session state for page selection if it doesn't exist
    if "page" not in st.session_state:
        st.session_state.page = "Home"

    # Sidebar Tabs
    def set_page(page):
        st.session_state.page = page

    with st.sidebar:
        st.title(_(text_key="navigation", page_translations=app_translations))
        st.button(_(text_key="home", page_translations=app_translations), on_click=set_page, args=("Home",))
        st.button(_(text_key="shape_cleaning", page_translations=app_translations), on_click=set_page, args=("Shape Cleaning",))
        st.button(_(text_key="generate_wells", page_translations=app_translations), on_click=set_page, args=("Generate Wells",))
        st.button(_(text_key="clean_wells", page_translations=app_translations), on_click=set_page, args=("Clean Wells",))
        st.button(_(text_key="download", page_translations=app_translations), on_click=set_page, args=("Download",))

    # Display content based on the selected page in session state
    if st.session_state.page == "Home":
        st.markdown(f"### {_('how_this_app_works', app_translations)}")
        st.write(_(text_key="app_instructions", page_translations=app_translations))

    elif st.session_state.page == "Shape Cleaning":
        shape_cleaning_page(lambda text_key: _(text_key, shape_cleaning_translations))

    elif st.session_state.page == "Generate Wells":
        generate_wells_page(lambda text_key: _(text_key, generate_wells_translations))

    elif st.session_state.page == "Clean Wells":
        reduce_wells_page(lambda text_key: _(text_key, reduce_wells_translations))

    elif st.session_state.page == "Download":
        final_map_page(lambda text_key: _(text_key, final_map_translations))
