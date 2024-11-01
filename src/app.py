import streamlit as st

# Set page configuration
st.set_page_config(page_title="Nyerseg Dataroom", layout="wide")

# Title and Welcome Message
st.title("Nyerseg Dataroom")
st.markdown("""
**Welcome to the Nyerseg Dataroom by Hawkar Ali Abdulhaq, Szeged University**  
**Contact**: [hawkar.ali.abdulhaq@szte.hu](mailto:hawkar.ali.abdulhaq@szte.hu)
""")

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
       - Download the map as an HTML file for further analysis or external sharing.

    By following these steps in sequence, you can prepare a clean, well-organized dataset that is ready for visualization and download.
    """)
    st.write("**Enjoy using the Nyerseg Dataroom for your well data management!**")

elif st.session_state.page == "Shape Cleaning":
    st.markdown("### Shape Cleaning")
    st.write("This is the Shape Cleaning page content.")
    # Insert the content of 1_Shape_Cleaning.py here

elif st.session_state.page == "Generate Wells":
    st.markdown("### Generate Wells")
    st.write("This is the Generate Wells page content.")
    # Insert the content of 2_Generate_Wells.py here

elif st.session_state.page == "Clean Wells":
    st.markdown("### Clean Wells")
    st.write("This is the Clean Wells page content.")
    # Insert the content of 3_Clean_Wells.py here

elif st.session_state.page == "Download":
    st.markdown("### Download")
    st.write("This is the Download page content.")
    # Insert the content of 4_Download.py here
