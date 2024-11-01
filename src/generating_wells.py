import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import numpy as np
import pandas as pd
import os

# Define input and output paths
shapefile_path = r'D:\Nyrseg\Clearning\input\irrigated_cleaned\Irrigated_fields_cleaned.shp'
real_wells_path = r'D:\Nyrseg\Clearning\input\real_wells\realwellss.txt'
output_directory = r'D:\Nyrseg\Clearning\output'

# Load the shapefile
fields = gpd.read_file(shapefile_path)

# Convert CRS to a projected system that allows for metric distance measurement
fields = fields.to_crs(epsg=32633)  # UTM Zone 33N, suitable for metric distances in this region

# Function to place wells
def place_wells(geometry, num_wells):
    points = []
    for _ in range(num_wells):
        # Generate points near the center of the polygon
        x_offset, y_offset = np.random.uniform(-50, 50, 2)  # Random offset in meters, within 50 meters from the center
        point = Point(geometry.centroid.x + x_offset, geometry.centroid.y + y_offset)
        points.append(point)
    return points

# Determine number of wells for each field and place them with tracing
def assign_wells(geometry):
    area = geometry.area
    num_wells = 0 if area < 5000 else (1 if area < 10000 else (2 if area < 50000 else 3))
    print(f"Field area: {area:.2f} m², Assigned wells: {num_wells}")
    return place_wells(geometry, num_wells)

# Apply the well assignment with tracing
fields['wells'] = fields['geometry'].apply(assign_wells)

# Flatten the list of well points for easy plotting
well_points = [pt for sublist in fields['wells'] for pt in sublist if sublist]
well_gdf = gpd.GeoDataFrame(geometry=well_points, crs=fields.crs)

# Save generated wells to text file with EOV coordinates
well_gdf_eov = well_gdf.to_crs(epsg=23700)
well_gdf_eov['X'] = well_gdf_eov.geometry.x
well_gdf_eov['Y'] = well_gdf_eov.geometry.y
output_wells_path = os.path.join(output_directory, 'generated_wells_eov.txt')
well_gdf_eov[['X', 'Y']].to_csv(output_wells_path, sep=' ', index=False, header=False)
print(f"Generated wells saved to {output_wells_path} in EOV coordinates.")

# Load real well locations
real_wells = pd.read_csv(real_wells_path, delim_whitespace=True, header=None, names=['X', 'Y'])
real_wells_gdf = gpd.GeoDataFrame(real_wells, geometry=gpd.points_from_xy(real_wells.X, real_wells.Y))
real_wells_gdf.crs = 'EPSG:23700'  # Set original CRS for the real wells
real_wells_gdf = real_wells_gdf.to_crs(epsg=32633)  # Transform CRS to match fields

# Plotting
fig, ax = plt.subplots(figsize=(10, 10))
fields.plot(ax=ax, color='lightgreen', edgecolor='black')  # Plot fields
well_gdf.plot(ax=ax, color='blue', marker='o', markersize=30, label='Generated Wells')  # Plot generated wells
real_wells_gdf.plot(ax=ax, color='red', marker='x', markersize=50, label='Real Wells')  # Plot real wells
plt.title('Well Locations within Fields')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()

# Save the plot to the output directory
output_path = os.path.join(output_directory, 'wells_map.png')
plt.savefig(output_path, dpi=300)
print(f"Map has been created and saved as {output_path}")

plt.show()
