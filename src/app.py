# app.py
import streamlit as st

st.set_page_config(page_title="Home", layout="wide")

st.title("Nyerseg Dataroom")
st.markdown("""
**Welcome to the Nyerseg Dataroom by Hawkar Ali Abdulhaq, Szeged University**  
**Contact**: [hawkar.ali.abdulhaq@szte.hu](mailto:hawkar.ali.abdulhaq@szte.hu)

This app provides a streamlined process for managing and visualizing well data across multiple stages of analysis.

### How This App Works

1. **Shape Cleaning**:  
   - Consolidate nearby fields by applying a buffer to each shapefile boundary.
   - Adjust the buffer distance as needed and review the before and after visuals.

2. **Generate Wells**:  
   - Place virtual wells within each field based on field size and specified offset distance.
   - Customize the well density based on field size thresholds.

3. **Clean Wells**:  
   - Apply distance filters to remove wells that are too close to each other or to real wells.
   - Adjust the distance parameters and visualize the filtered results.

4. **Download**:  
   - View the final interactive map showing real and generated wells.
   - Download the map as an HTML file for external sharing or offline viewing.

**Enjoy using the Nyerseg Dataroom for your well data management!**
""")
