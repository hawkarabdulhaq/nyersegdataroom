# src/generate_wells.py
import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import numpy as np
import pandas as pd
import os
from translations.generate_wells import translations as generate_wells_translations

def generate_wells_page(_):
    # Page title
    st.title(_("generate_wells_title"))

    # Description
    st.markdown(_("generate_wells_description"))

    # User inputs for essential parameters
    offset_range = st.slider(_("offset_range_label"), min_value=0, max_value=100, value=50, step=5)

    # Parameters for determining the number of wells based on field area
    area_to_wells = {
        _("small_fields_label"): 0,
        _("medium_fields_label"): 1,
        _("large_fields_label"): 2,
        _("very_large_fields_label"): 3
    }

    st.markdown(_("field_area_section"))
    area_to_wells[_("small_fields_label")] = st.number_input(_("small_fields_label"), min_value=0, max_value=10, value=0)
    area_to_wells[_("medium_fields_label")] = st.number_input(_("medium_fields_label"), min_value=0, max_value=10, value=1)
    area_to_wells[_("large_fields_label")] = st.number_input(_("large_fields_label"), min_value=0, max_value=10, value=2)
    area_to_wells[_("very_large_fields_label")] = st.number_input(_("very_large_fields_label"), min_value=0, max_value=10, value=3)

    # Run the well generation script when button is clicked
    if st.button(_("generate_wells_button"), key="generate_wells_button"):
        try:
            # Define paths
            shapefile_path = 'input/irrigated_cleaned/Irrigated_fields_cleaned.shp'
            real_wells_path = 'input/real_wells/realwellss.txt'
            output_directory = 'output'
            output_wells_path = os.path.join(output_directory, 'generated_wells_eov.txt')
            output_map_path = os.path.join(output_directory, 'wells_map.png')

            # Load the cleaned shapefile
            fields = gpd.read_file(shapefile_path)
            fields = fields.to_crs(epsg=32633)  # Set CRS directly without user input

            # Define function to place wells
            def place_wells(geometry, num_wells):
                points = []
                for _ in range(num_wells):
                    x_offset, y_offset = np.random.uniform(-offset_range, offset_range, 2)
                    point = Point(geometry.centroid.x + x_offset, geometry.centroid.y + y_offset)
                    points.append(point)
                return points

            # Define function to determine the number of wells based on field area
            def assign_wells(geometry):
                area = geometry.area
                if area < 5000:
                    num_wells = area_to_wells[_("small_fields_label")]
                elif area < 10000:
                    num_wells = area_to_wells[_("medium_fields_label")]
                elif area < 50000:
                    num_wells = area_to_wells[_("large_fields_label")]
                else:
                    num_wells = area_to_wells[_("very_large_fields_label")]
                return place_wells(geometry, num_wells)

            # Apply well assignment
            fields['wells'] = fields['geometry'].apply(assign_wells)

            # Flatten the list of well points for easy plotting
            well_points = [pt for sublist in fields['wells'] for pt in sublist if sublist]
            well_gdf = gpd.GeoDataFrame(geometry=well_points, crs=fields.crs)

            # Save generated wells to text file with EOV coordinates
            well_gdf_eov = well_gdf.to_crs(epsg=23700)
            well_gdf_eov['X'] = well_gdf_eov.geometry.x
            well_gdf_eov['Y'] = well_gdf_eov.geometry.y
            well_gdf_eov[['X', 'Y']].to_csv(output_wells_path, sep=' ', index=False, header=False)
            st.success(_("generated_wells_saved").format(output_wells_path))

            # Load real well locations and plot the results
            real_wells = pd.read_csv(real_wells_path, delim_whitespace=True, header=None, names=['X', 'Y'])
            real_wells_gdf = gpd.GeoDataFrame(real_wells, geometry=gpd.points_from_xy(real_wells.X, real_wells.Y), crs='EPSG:23700')
            real_wells_gdf = real_wells_gdf.to_crs(epsg=32633)  # Set CRS directly

            # Plotting the generated and real wells
            fig, ax = plt.subplots(figsize=(10, 10))
            fields.plot(ax=ax, color='lightgreen', edgecolor='black')
            well_gdf.plot(ax=ax, color='blue', marker='o', markersize=30, label=_("generated_wells_label"))
            real_wells_gdf.plot(ax=ax, color='red', marker='x', markersize=50, label=_("real_wells_label"))
            plt.title(_("well_locations_title"))
            plt.xlabel(_("longitude_label"))
            plt.ylabel(_("latitude_label"))
            plt.legend()

            # Show the plot in Streamlit
            st.pyplot(fig)

            # Save the plot
            plt.savefig(output_map_path, dpi=300)
            st.success(_("map_saved").format(output_map_path))

        except Exception as e:
            st.error(_("error_message").format(e))

# Helper function for page translation
def _(text_key):
    return generate_wells_translations[st.session_state.language].get(text_key, text_key)
