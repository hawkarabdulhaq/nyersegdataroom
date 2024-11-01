import geopandas as gpd
import matplotlib.pyplot as plt
import os

# Define paths
shapefile_path = r'D:\Nyrseg\Clearning\input\irrigated\Irrigated fields.shp'
output_directory = r'D:\Nyrseg\Clearning\input\irrigated_cleaned'
output_shapefile_path = os.path.join(output_directory, 'Irrigated_fields_cleaned.shp')

# Load the shapefile
fields_gdf = gpd.read_file(shapefile_path)

# Set the CRS to a projected CRS for accurate distance calculations
fields_gdf = fields_gdf.to_crs(epsg=32633)  # UTM Zone 33N as an example, adjust to your region

# Buffer each field by 50 meters, merge overlapping buffers, then remove the buffer
buffered_fields = fields_gdf.buffer(50)  # Apply a 50-meter buffer
merged_fields = buffered_fields.unary_union  # Merge overlapping buffered areas
merged_gdf = gpd.GeoDataFrame(geometry=[merged_fields]).explode(index_parts=False).reset_index(drop=True)

# Set CRS to match the original fields CRS
merged_gdf.crs = fields_gdf.crs

# Save the merged fields as a new shapefile
os.makedirs(output_directory, exist_ok=True)  # Ensure the output directory exists
merged_gdf.to_file(output_shapefile_path)
print(f"Merged shapefile saved to {output_shapefile_path}")

# Plotting the merged fields
fig, ax = plt.subplots(figsize=(10, 10))
merged_gdf.plot(ax=ax, color='lightblue', edgecolor='black')
plt.title('Merged Irrigated Fields (Fields within 50 meters merged)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
