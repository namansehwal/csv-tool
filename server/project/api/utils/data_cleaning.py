from fuzzywuzzy import process
from .school_data import data
import pandas as pd


def clean(file_path):
    # Read the CSV into a pandas DataFrame
    df = pd.read_csv(file_path)
    
    # Merge 'First Name' and 'Last Name' into a single 'Name' column
    df['Name'] = df['First Name'].fillna('') + ' ' + df['Last Name'].fillna('')
    
    # Extract the state using the provided extract function based on 'School' and 'Location'
    df['State'] = df.apply(lambda row: extract(row['School'], row['Location']), axis=1)
    
    # Melt the DataFrame to unpivot the Class columns into rows
    class_cols = [col for col in df.columns if 'Class' in col]  # Find all columns with 'Class' in their name
    df_melted = df.melt(id_vars=['Name', 'School', 'State'], value_vars=class_cols, var_name='Class Type', value_name='Class')
    
    # Drop rows where Class is NaN or empty
    df_melted = df_melted.dropna(subset=['Class'])
    
    # Sort the data by Name 
    df_melted = df_melted.sort_values('Name')
    
    # Select only the relevant columns for the final output
    final_df = df_melted[['Name', 'Class', 'School', 'State']]

    return final_df
    

def extract(school_name, Location):
    # Extract school names from the dictionary
    schools = list(data.keys())
    
    # Perform fuzzy matching
    closest_match = process.extractOne(school_name, schools)
    
    if closest_match:
        matched_school = closest_match[0]
        state_code = data[matched_school]
        return state_code
    else:
        return Location
