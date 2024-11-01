# src/2_Generate_Wells.py
import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import numpy as np
import pandas as pd
import os

def generate_wells_page():
    st.title("Generate Wells")

    # Define input and output paths
    shapefile_path = 'input/irrigated_cleaned/Irrigated_fields_cleaned.shp'
    real_wells_path = 'input/real_wells/realwellss.txt'
    output_directory = 'output'
    output_wells_path = os.path.join(output_directory, 'generated_wells_eov.txt')
    output_map_path = os.path.join(output_directory, 'wells_map.png')

    # Description
    st.markdown("""
    **Objective**: This script generates wells within each field based on field area and user-defined parameters. 
    The wells are placed randomly around the center of each field, with the number determined by the field's size.
    """)

    # User inputs for essential parameters
    offset_range = st.slider("Offset Range from Centroid (meters)", min_value=0, max_value=100, value=50, step=5)

    # Parameters for determining the number of wells based on field area
    area_to_wells = {
        "Small fields (< 5,000 m²)": 0,
        "Medium fields (5,000 - 10,000 m²)": 1,
        "Large fields (10,000 - 50,000 m²)": 2,
        "Very large fields (> 50,000 m²)": 3
    }

    st.markdown("### Set Number of Wells Based on Field Area")
    area_to_wells["Small fields (< 5,000 m²)"] = st.number_input("Number of wells for Small fields (< 5,000 m²)", min_value=0, max_value=10, value=0)
    area_to_wells["Medium fields (5,000 - 10,000 m²)"] = st.number_input("Number of wells for Medium fields (5,000 - 10,000 m²)", min_value=0, max_value=10, value=1)
    area_to_wells["Large fields (10,000 - 50,000 m²)"] = st.number_input("Number of wells for Large fields (10,000 - 50,000 m²)", min_value=0, max_value=10, value=2)
    area_to_wells["Very large fields (> 50,000 m²)"] = st.number_input("Number of wells for Very large fields (> 50,000 m²)", min_value=0, max_value=10, value=3)

    # Run the well generation script when button is clicked
    if st.button("Generate Wells"):
        try:
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
                    num_wells = area_to_wells["Small fields (< 5,000 m²)"]
                elif area < 10000:
                    num_wells = area_to_wells["Medium fields (5,000 - 10,000 m²)"]
                elif area < 50000:
                    num_wells = area_to_wells["Large fields (10,000 - 50,000 m²)"]
                else:
                    num_wells = area_to_wells["Very large fields (> 50,000 m²)"]
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
            st.success(f"Generated wells saved to {output_wells_path}")

            # Load real well locations and plot the results
            real_wells = pd.read_csv(real_wells_path, delim_whitespace=True, header=None, names=['X', 'Y'])
            real_wells_gdf = gpd.GeoDataFrame(real_wells, geometry=gpd.points_from_xy(real_wells.X, real_wells.Y), crs='EPSG:23700')
            real_wells_gdf = real_wells_gdf.to_crs(epsg=32633)  # Set CRS directly

            # Plotting the generated and real wells
            fig, ax = plt.subplots(figsize=(10, 10))
            fields.plot(ax=ax, color='lightgreen', edgecolor='black')
            well_gdf.plot(ax=ax, color='blue', marker='o', markersize=30, label='Generated Wells')
            real_wells_gdf.plot(ax=ax, color='red', marker='x', markersize=50, label='Real Wells')
            plt.title('Well Locations within Fields')
            plt.xlabel('Longitude')
            plt.ylabel('Latitude')
            plt.legend()

            # Show the plot in Streamlit
            st.pyplot(fig)

            # Save the plot
            plt.savefig(output_map_path, dpi=300)
            st.success(f"Map has been created and saved as {output_map_path}")

        except Exception as e:
            st.error(f"An error occurred: {e}")
