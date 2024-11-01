# src/1_Clean_SHP.py
import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt
import os

def shape_cleaning_page():
    st.title("Shape Cleaning - Clean and Merge Shapefiles")

    # Define paths
    shapefile_path = 'input/irrigated/Irrigated fields.shp'
    output_directory = 'input/irrigated_cleaned'
    output_shapefile_path = os.path.join(output_directory, 'Irrigated_fields_cleaned.shp')

    # Description of the script
    st.markdown("""
    **Objective**: This page runs the `cleanshp.py` script, which cleans and merges shapefile data by buffering and merging close polygons. 
    The process is useful for consolidating fields that are near each other, simplifying visualization and analysis.
    """)

    # Buffer distance input
    buffer_distance = st.slider("Select Buffer Distance (meters)", min_value=0, max_value=100, value=50, step=5)
    st.write(f"Buffer distance set to: {buffer_distance} meters")

    # Run the clean and merge process
    if st.button("Run CleanSHP"):
        try:
            # Load the shapefile
            fields_gdf = gpd.read_file(shapefile_path)

            # Set the CRS to a projected CRS for accurate distance calculations
            fields_gdf = fields_gdf.to_crs(epsg=32633)

            # Buffer each field by the user-defined distance, merge overlapping buffers, then remove the buffer
            buffered_fields = fields_gdf.buffer(buffer_distance)
            merged_fields = buffered_fields.unary_union
            merged_gdf = gpd.GeoDataFrame(geometry=[merged_fields]).explode(index_parts=False).reset_index(drop=True)

            # Set CRS to match the original fields CRS
            merged_gdf.crs = fields_gdf.crs

            # Save the merged fields as a new shapefile
            os.makedirs(output_directory, exist_ok=True)
            merged_gdf.to_file(output_shapefile_path)
            st.success(f"Merged shapefile saved to {output_shapefile_path}")

            # Plotting the before and after side by side
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 10))
            
            # Before plot
            fields_gdf.plot(ax=ax1, color='lightgrey', edgecolor='black')
            ax1.set_title("Original Fields")
            ax1.set_xlabel("Longitude")
            ax1.set_ylabel("Latitude")
            
            # After plot
            merged_gdf.plot(ax=ax2, color='lightblue', edgecolor='black')
            ax2.set_title(f"Merged Fields with {buffer_distance} m Buffer")
            ax2.set_xlabel("Longitude")
            ax2.set_ylabel("Latitude")
            
            # Show the plots in Streamlit
            st.pyplot(fig)
        
        except Exception as e:
            st.error(f"An error occurred: {e}")
