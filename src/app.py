import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.clean_shp import shape_cleaning_page  # Import the shape cleaning function
from src.generate_wells import generate_wells_page  # Import the generate wells function
from src.reduce_wells import reduce_wells_page  # Import the reduce wells function
from src.final_map import final_map_page  # Import the final map function

# Set page configuration
st.set_page_config(page_title="Nyerseg Dataroom", layout="wide")

# Title and Welcome Message
st.title("Nyerseg Dataroom")
st.markdown("""
**Welcome to the Nyerseg Dataroom by Hawkar Ali Abdulhaq, Szeged University**  
**Contact**: [hawkar.ali.abdulhaq@szte.hu](mailto:hawkar.ali.abdulhaq@szte.hu)
""")

# Define the access key
ACCESS_KEY = "Asd456"

# Check if the user has already been authenticated
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Access key input and validation
if not st.session_state.authenticated:
    st.subheader("Please enter the access key to proceed:")
    access_key_input = st.text_input("Access Key", type="password")
    
    if st.button("Access"):
        if access_key_input == ACCESS_KEY:
            st.session_state.authenticated = True
            st.success("Access granted! You may now use the app.")
            st.experimental_set_query_params(auth="true")  # This will refresh the page
        else:
            st.error("Invalid access key. Please try again.")

# Main app content
if st.session_state.authenticated:
    # Initialize session state for page selection if it doesn't exist
    if "page" not in st.session_state:
        st.session_state.page = "Home"

    # Sidebar Tabs
    def set_page(page):
        st.session_state.page = page

    with st.sidebar:
        st.title("Navigation")
        st.button("Home", on_click=set_page, args=("Home",))
        st.button("Shape Cleaning", on_click=set_page, args=("Shape Cleaning",))
        st.button("Generate Wells", on_click=set_page, args=("Generate Wells",))
        st.button("Clean Wells", on_click=set_page, args=("Clean Wells",))
        st.button("Download", on_click=set_page, args=("Download",))

    # Display content based on the selected page in session state
    if st.session_state.page == "Home":
        st.markdown("### How This App Works")
        st.write("""
        This app follows a sequential workflow to prepare and visualize well data. Each page offers a specific function, allowing you to process and interact with the data in a logical order. Below is a guide to each page's purpose:

        1. **Shape Cleaning**:  
           - This page loads the initial field shapefile and consolidates fields that are close to each other.
           - Adjust the buffer distance, run the cleaning, and see "before and after" comparisons to ensure accuracy.

        2. **Generate Wells**:  
           - Based on field size, this page generates virtual wells within each field, placing wells randomly around the centroid of each field.
           - Customize parameters, such as the offset range and number of wells per field size category.

        3. **Clean Wells**:  
           - This page filters generated wells to remove any that are too close to each other or real wells, ensuring optimal spacing.
           - Adjust minimum distance criteria and visualize the results on a filtered map.

        4. **Download**:  
           - View the final interactive map showing only real and filtered generated wells.
           - Download the map as an HTML file for external sharing or offline viewing.

        By following these steps in sequence, you can prepare a clean, well-organized dataset that is ready for visualization and download.
        """)

    elif st.session_state.page == "Shape Cleaning":
        shape_cleaning_page()  # Call the shape cleaning function

    elif st.session_state.page == "Generate Wells":
        generate_wells_page()  # Call the generate wells function

    elif st.session_state.page == "Clean Wells":
        reduce_wells_page()  # Call the reduce wells function

    elif st.session_state.page == "Download":
        final_map_page()  # Call the final map function
