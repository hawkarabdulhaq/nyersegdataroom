# Create the main repository directory
mkdir -p Nyersegdataroom
cd Nyersegdataroom

# Initialize a new git repository
git init

# Create the main folders for data and scripts
mkdir -p input/irrigated
mkdir -p input/irrigated_cleaned
mkdir -p input/real_wells
mkdir -p output
mkdir -p src

# Navigate back to the root of the repository
cd ..

# Print confirmation message
echo "Repository structure for Nyersegdataroom has been created."

# Optional: Create a .gitignore file to exclude certain files from version control
cat <<EOL > Nyersegdataroom/.gitignore
# Ignore output files and other generated data
output/
*.txt
*.png

# Ignore environment or temporary files
__pycache__/
*.py[cod]
*.DS_Store

# Ignore Streamlit cache files if using Streamlit
.streamlit/
EOL

echo ".gitignore has been created."

# Print final message
echo "Repository setup is complete. You can now add your files to the directory."
