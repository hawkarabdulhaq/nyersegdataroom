# src/4_Final_Map.py
import streamlit as st
import geopandas as gpd
import pandas as pd
import folium
from folium.plugins import MarkerCluster
import os

def final_map_page():
    st.title("Final Map of Real and Generated Wells")

    # Define input paths
    filtered_wells_path = 'output/filtered_generated_wells_eov.txt'
    real_wells_path = 'input/real_wells/realwellss.txt'
    output_html_map_path = 'output/final_wells_map.html'

    # Description
    st.markdown("""
    This page displays the final positions of generated wells, filtered to ensure appropriate distances from real wells, 
    alongside the real well locations on an interactive map. The map can also be downloaded as an HTML file.
    Additionally, you can download the generated EOV X and Y coordinates for the filtered generated wells.
    """)

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
                popup=f"Real Well {idx + 1}"
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
                popup=f"Generated Well {idx + 1}"
            ).add_to(m)

        # Save map as HTML file
        m.save(output_html_map_path)
        st.success(f"Interactive map saved as HTML at {output_html_map_path}")

        # Display the map in Streamlit
        st.components.v1.html(m._repr_html_(), height=600)

        # Download link for the HTML map
        with open(output_html_map_path, "rb") as file:
            st.download_button("Download Map as HTML", data=file, file_name="final_wells_map.html", mime="text/html")

        # Download link for the generated wells EOV file
        with open(filtered_wells_path, "rb") as file:
            st.download_button("Download Generated Wells EOV Coordinates", data=file, file_name="filtered_generated_wells_eov.txt", mime="text/plain")

    except Exception as e:
        st.error(f"An error occurred: {e}")
