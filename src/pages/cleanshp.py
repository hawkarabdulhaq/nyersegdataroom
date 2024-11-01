import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt
import os

# Define paths
shapefile_path = 'input/irrigated/Irrigated fields.shp'
output_directory = 'input/irrigated_cleaned'
output_shapefile_path = os.path.join(output_directory, 'Irrigated_fields_cleaned.shp')

st.title("Clean and Merge Shapefiles")

# Run the clean and merge process
if st.button("Run CleanSHP"):
    try:
        # Load the shapefile
        fields_gdf = gpd.read_file(shapefile_path)

        # Set the CRS to a projected CRS for accurate distance calculations
        fields_gdf = fields_gdf.to_crs(epsg=32633)

        # Buffer each field by 50 meters, merge overlapping buffers, then remove the buffer
        buffered_fields = fields_gdf.buffer(50)
        merged_fields = buffered_fields.unary_union
        merged_gdf = gpd.GeoDataFrame(geometry=[merged_fields]).explode(index_parts=False).reset_index(drop=True)

        # Set CRS to match the original fields CRS
        merged_gdf.crs = fields_gdf.crs

        # Save the merged fields as a new shapefile
        os.makedirs(output_directory, exist_ok=True)
        merged_gdf.to_file(output_shapefile_path)
        st.success(f"Merged shapefile saved to {output_shapefile_path}")

        # Plot the merged fields
        fig, ax = plt.subplots(figsize=(10, 10))
        merged_gdf.plot(ax=ax, color='lightblue', edgecolor='black')
        plt.title('Merged Irrigated Fields (Fields within 50 meters merged)')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        st.pyplot(fig)
    
    except Exception as e:
        st.error(f"An error occurred: {e}")
