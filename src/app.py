import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.clean_shp import shape_cleaning_page  # Import the shape cleaning function
from src.generate_wells import generate_wells_page  # Import the generate wells function
from src.reduce_wells import reduce_wells_page  # Import the reduce wells function
from src.final_map import final_map_page  # Import the final map function
from translation import translations  # Import translations

# Helper function for translation
def _(text_key):
    return translations[st.session_state.language].get(text_key, text_key)

# Set page configuration
st.set_page_config(page_title=_("page_title"), layout="wide")

# Initialize session state for language if it doesn't exist
if "language" not in st.session_state:
    st.session_state.language = 'en'  # Default to English

# Language selection in the sidebar
with st.sidebar:
    st.selectbox(
        "Language / Nyelv",
        options=["English", "Magyar"],
        index=0 if st.session_state.language == 'en' else 1,
        on_change=lambda: st.session_state.update(
            language='en' if st.session_state.get('language') == 'English' else 'hu'
        )
    )

# Title and Welcome Message
st.title(_("page_title"))
st.markdown(_("welcome_message"))

# Define the access key
ACCESS_KEY = "Asd456"

# Check if the user has already been authenticated
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Access key input and validation
if not st.session_state.authenticated:
    st.subheader(_("access_key_prompt"))
    access_key_input = st.text_input(_("access_key_label"), type="password")
    
    if st.button(_("access_button")):
        if access_key_input == ACCESS_KEY:
            st.session_state.authenticated = True
            st.success(_("access_granted"))
            st.experimental_set_query_params(auth="true")  # This will refresh the page
        else:
            st.error(_("invalid_key"))

# Main app content
if st.session_state.authenticated:
    # Initialize session state for page selection if it doesn't exist
    if "page" not in st.session_state:
        st.session_state.page = "Home"

    # Sidebar Tabs
    def set_page(page):
        st.session_state.page = page

    with st.sidebar:
        st.title(_("navigation"))
        st.button(_("home"), on_click=set_page, args=("Home",))
        st.button(_("shape_cleaning"), on_click=set_page, args=("Shape Cleaning",))
        st.button(_("generate_wells"), on_click=set_page, args=("Generate Wells",))
        st.button(_("clean_wells"), on_click=set_page, args=("Clean Wells",))
        st.button(_("download"), on_click=set_page, args=("Download",))

    # Display content based on the selected page in session state
    if st.session_state.page == "Home":
        st.markdown(f"### {_('how_this_app_works')}")
        st.write(_("app_instructions"))

    elif st.session_state.page == "Shape Cleaning":
        shape_cleaning_page()  # Call the shape cleaning function

    elif st.session_state.page == "Generate Wells":
        generate_wells_page()  # Call the generate wells function

    elif st.session_state.page == "Clean Wells":
        reduce_wells_page()  # Call the reduce wells function

    elif st.session_state.page == "Download":
        final_map_page()  # Call the final map function
