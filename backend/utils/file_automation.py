import requests
from zipfile import ZipFile
import os
import pandas as pd

# Define the base URL for the OpenFDA endpoint for Animal & Veterinary Adverse Events
base_url = 'https://api.fda.gov/download/animalandveterinary/event/'

# Function to download and unzip files
def download_and_unzip_files(base_url, number_of_files):
    for i in range(number_of_files):
        # Construct the file URL
        file_url = f"{base_url}Q{i+1}_data.zip"
        
        # Download the file
        resp = requests.get(file_url)
        file_name = f"Q{i+1}_data.zip"
        
        # Save the file
        with open(file_name, 'wb') as f:
            f.write(resp.content)
        
        # Unzip the file
        with ZipFile(file_name, 'r') as zip_ref:
            zip_ref.extractall("data")

# Call the function to download and unzip all files
download_and_unzip_files(base_url, 147)

# Assuming all unzipped JSON files are in the "data" directory, load them into Pandas DataFrames
data_frames = []
for json_file in os.listdir('data'):
    if json_file.endswith('.json'):
        data_frame = pd.read_json(os.path.join('data', json_file))
        data_frames.append(data_frame)

# Concatenate the dataframes
combined_df = pd.concat(data_frames, ignore_index=True)

# Perform further data cleaning and transformation here...

# Save the combined DataFrame to a CSV or database for use with Tableau
combined_df.to_csv('combined_data.csv', index=False)
# Or load into a database...
