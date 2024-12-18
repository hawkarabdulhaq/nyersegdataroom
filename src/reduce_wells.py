# src/3_Reduce_Wells.py
import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from shapely.geometry import Point
import os
from scipy.spatial import cKDTree
from scipy.spatial.distance import pdist
import numpy as np
from translations.reduce_wells import translations as reduce_wells_translations

def reduce_wells_page(_):
    # Page title
    st.title(_("reduce_wells_title"))

    # Define input and output paths
    generated_wells_path = 'output/generated_wells_eov.txt'
    real_wells_path = 'input/real_wells/realwellss.txt'
    boundary_path = 'input/boundary/boundary.shp'
    output_filtered_wells_path = 'output/filtered_generated_wells_eov.txt'
    output_map_path = 'output/filtered_generated_wells_map.png'
    output_histogram_path = 'output/filtered_well_distances_histogram.png'

    # Description
    st.markdown(_("reduce_wells_description"))

    # User inputs for distance cutoffs
    min_distance_generated = st.slider(_("min_distance_generated_label"), min_value=0, max_value=1000, value=500, step=10)
    min_distance_real = st.slider(_("min_distance_real_label"), min_value=0, max_value=1000, value=500, step=10)
    min_distance_boundary = st.slider(_("Border Threshold"), min_value=0, max_value=5000, value=3000, step=100)

    # Run the well reduction script when button is clicked
    if st.button(_("run_well_reduction_button")):
        try:
            # Load the generated wells
            generated_wells = pd.read_csv(generated_wells_path, sep='\s+', header=None, names=['X', 'Y'])
            generated_wells_gdf = gpd.GeoDataFrame(generated_wells, geometry=gpd.points_from_xy(generated_wells.X, generated_wells.Y))
            generated_wells_gdf.crs = 'EPSG:23700'

            # Load real wells
            real_wells = pd.read_csv(real_wells_path, sep='\s+', header=None, names=['X', 'Y'])
            real_wells_gdf = gpd.GeoDataFrame(real_wells, geometry=gpd.points_from_xy(real_wells.X, real_wells.Y))
            real_wells_gdf.crs = 'EPSG:23700'

            # Load boundary
            boundary_gdf = gpd.read_file(boundary_path)
            boundary_gdf.crs = 'EPSG:23700'

            # Convert CRS for distance measurement
            generated_wells_gdf = generated_wells_gdf.to_crs(epsg=32633)
            real_wells_gdf = real_wells_gdf.to_crs(epsg=32633)
            boundary_gdf = boundary_gdf.to_crs(epsg=32633)

            # Convert coordinates to NumPy arrays
            generated_coordinates = np.array(list(zip(generated_wells_gdf.geometry.x, generated_wells_gdf.geometry.y)))
            real_coordinates = np.array(list(zip(real_wells_gdf.geometry.x, real_wells_gdf.geometry.y)))

            # Create KDTree for generated wells and real wells
            generated_tree = cKDTree(generated_coordinates)
            real_tree = cKDTree(real_coordinates)

            # Identify generated wells to remove based on distance to other generated wells
            to_remove = set()
            for i, point in enumerate(generated_coordinates):
                if i in to_remove:
                    continue  # Skip wells already marked for removal
                # Check for generated wells within min_distance_generated
                indices = generated_tree.query_ball_point(point, min_distance_generated)
                for j in indices:
                    if i != j:
                        to_remove.add(j)  # Mark well for removal

            # Further filter out generated wells that are within min_distance_real of any real well
            for i, point in enumerate(generated_coordinates):
                if i in to_remove:
                    continue  # Skip wells already marked for removal
                # Check if the well is within min_distance_real of any real well
                if real_tree.query_ball_point(point, min_distance_real):
                    to_remove.add(i)

            # Create a GeoSeries for the boundary geometry
            boundary_geometry = boundary_gdf.unary_union

            # Further filter out generated wells that are within min_distance_boundary of the boundary line
            remaining_indices = [i for i in range(len(generated_wells_gdf)) if i not in to_remove]
            for i in remaining_indices:
                point = generated_wells_gdf.geometry.iloc[i]
                distance_to_boundary = point.distance(boundary_geometry)
                if distance_to_boundary <= min_distance_boundary:
                    to_remove.add(i)

            # Filter wells based on the to_remove set
            remaining_wells_gdf = generated_wells_gdf.drop(index=to_remove).reset_index(drop=True)
            removed_wells_gdf = generated_wells_gdf.loc[list(to_remove)].reset_index(drop=True)

            # Save the filtered wells to a new text file
            remaining_wells_gdf[['X', 'Y']].to_csv(output_filtered_wells_path, sep=' ', index=False, header=False)
            st.success(_("filtered_wells_saved").format(output_filtered_wells_path))

            # Plot the remaining and removed wells on a map
            fig, ax = plt.subplots(figsize=(10, 10))
            remaining_wells_gdf.plot(ax=ax, color='green', marker='o', markersize=30, label=_("remaining_wells_label"))
            removed_wells_gdf.plot(ax=ax, color='red', marker='x', markersize=30, label=_("removed_wells_label"))
            real_wells_gdf.plot(ax=ax, color='blue', marker='^', markersize=50, label=_("real_wells_label"))
            boundary_gdf.plot(ax=ax, color='black', linewidth=2, label=_("boundary_label"))
            plt.title(_("well_locations_with_filters"))
            plt.xlabel(_("easting_label"))
            plt.ylabel(_("northing_label"))
            plt.legend()
            st.pyplot(fig)

            # Save the map
            plt.savefig(output_map_path, dpi=300)
            st.success(_("filtered_wells_map_saved").format(output_map_path))

            # Calculate pairwise distances for remaining wells
            remaining_coordinates = np.array(list(zip(remaining_wells_gdf.geometry.x, remaining_wells_gdf.geometry.y)))
            remaining_distances = pdist(remaining_coordinates)

            # Plot histogram of the distances after filtering
            plt.figure(figsize=(10, 6))
            plt.hist(remaining_distances, bins=30, edgecolor='black')
            plt.title(_("histogram_title"))
            plt.xlabel(_("histogram_x_label"))
            plt.ylabel(_("histogram_y_label"))
            st.pyplot(plt)

            # Save the histogram
            plt.savefig(output_histogram_path, dpi=300)
            st.success(_("histogram_saved").format(output_histogram_path))

        except Exception as e:
            st.error(_("error_message").format(e))

# Helper function for page translation
def _(text_key):
    return reduce_wells_translations[st.session_state.language].get(text_key, text_key)
