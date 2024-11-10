# src/1_Clean_SHP.py
import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt
import os

def shape_cleaning_page(_):
    st.title(_("shape_cleaning_title"))

    # Define paths
    shapefile_path = 'input/irrigated/Irrigated fields.shp'
    output_directory = 'input/irrigated_cleaned'
    output_shapefile_path = os.path.join(output_directory, 'Irrigated_fields_cleaned.shp')

    # Description of the script
    st.markdown(_("shape_cleaning_description"))

    # Buffer distance input
    buffer_distance = st.slider(_("buffer_distance_label"), min_value=0, max_value=100, value=50, step=5)
    st.write(_("buffer_distance_set").format(buffer_distance))

    # Run the clean and merge process
    if st.button(_("run_clean_button")):
        with st.spinner(_("processing_message")):
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
                st.success(_("success_message").format(output_shapefile_path))

                # Plotting the before and after side by side
                fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 10))
                
                # Before plot
                fields_gdf.plot(ax=ax1, color='lightgrey', edgecolor='black')
                ax1.set_title(_("original_fields"))
                ax1.set_xlabel(_("longitude_label"))
                ax1.set_ylabel(_("latitude_label"))
                
                # After plot
                merged_gdf.plot(ax=ax2, color='lightblue', edgecolor='black')
                ax2.set_title(_("merged_fields").format(buffer_distance))
                ax2.set_xlabel(_("longitude_label"))
                ax2.set_ylabel(_("latitude_label"))
                
                # Show the plots in Streamlit
                st.pyplot(fig)
            
            except Exception as e:
                st.error(_("error_message").format(e))
