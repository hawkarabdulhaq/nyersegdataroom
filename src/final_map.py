# src/4_Final_Map.py
import streamlit as st
import geopandas as gpd
import pandas as pd
import folium
import os
from translations.final_map import translations as final_map_translations

def final_map_page(_):
    # Page title
    st.title(_("final_map_title"))

    # Define input paths
    filtered_wells_path = 'output/filtered_generated_wells_eov.txt'
    real_wells_path = 'input/real_wells/realwellss.txt'
    output_html_map_path = 'output/final_wells_map.html'

    # Description
    st.markdown(_("final_map_description"))

    # Load the filtered generated wells and real wells
    try:
        # Load generated wells in EOV (EPSG:23700)
        generated_wells = pd.read_csv(filtered_wells_path, sep='\s+', header=None, names=['X', 'Y'])
        generated_wells_gdf = gpd.GeoDataFrame(generated_wells, geometry=gpd.points_from_xy(generated_wells.X, generated_wells.Y), crs='EPSG:23700')
        generated_wells_gdf = generated_wells_gdf.to_crs(epsg=4326)  # Convert to WGS84 for folium

        # Load real wells in EOV (EPSG:23700)
        real_wells = pd.read_csv(real_wells_path, sep='\s+', header=None, names=['X', 'Y'])
        real_wells_gdf = gpd.GeoDataFrame(real_wells, geometry=gpd.points_from_xy(real_wells.X, real_wells.Y), crs='EPSG:23700')
        real_wells_gdf = real_wells_gdf.to_crs(epsg=4326)  # Convert to WGS84 for folium

        # Create an interactive map centered on the average location of generated wells
        m = folium.Map(location=[generated_wells_gdf.geometry.y.mean(), generated_wells_gdf.geometry.x.mean()], zoom_start=12)
        
        # Add real wells to the map with red markers
        for idx, row in real_wells_gdf.iterrows():
            folium.CircleMarker(
                location=[row.geometry.y, row.geometry.x],
                color='red',
                radius=3,
                fill=True,
                fill_color='red',
                fill_opacity=0.6,
                popup=_("real_well_popup").format(idx + 1)
            ).add_to(m)
        
        # Add generated wells to the map with blue markers
        for idx, row in generated_wells_gdf.iterrows():
            folium.CircleMarker(
                location=[row.geometry.y, row.geometry.x],
                color='blue',
                radius=3,
                fill=True,
                fill_color='blue',
                fill_opacity=0.6,
                popup=_("generated_well_popup").format(idx + 1)
            ).add_to(m)

        # Save map as HTML file
        m.save(output_html_map_path)
        st.success(_("map_saved_message").format(output_html_map_path))

        # Display the map in Streamlit
        st.components.v1.html(m._repr_html_(), height=600)

        # Download link for the HTML map
        with open(output_html_map_path, "rb") as file:
            st.download_button(_("download_map_button"), data=file, file_name="final_wells_map.html", mime="text/html")

        # Download link for the generated wells EOV file
        with open(filtered_wells_path, "rb") as file:
            st.download_button(_("download_generated_wells_button"), data=file, file_name="filtered_generated_wells_eov.txt", mime="text/plain")

    except Exception as e:
        st.error(_("error_message").format(e))

# Helper function for page translation
def _(text_key):
    return final_map_translations[st.session_state.language].get(text_key, text_key)
