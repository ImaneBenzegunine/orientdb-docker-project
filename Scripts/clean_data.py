import pandas as pd
import ast
from pathlib import Path
from path import BASE_DIR, CLEAN_DATA_DIR,OUTPUT_DIR
import os

def clean_skills(skills_str):
    """Convert string representation of dict/list to actual Python objects"""
    try:
        if pd.isna(skills_str):
            return {}
        return ast.literal_eval(skills_str.replace("'", "\""))
    except:
        print(f"Failed to parse: {skills_str}")
        return {}

def clean_data(input_dir, output_dir):
    """Clean all CSV files in input directory"""
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)
    
    # Clean companies data
    companies = pd.read_csv(f"{input_dir}/companies.csv")
    #print the type of the skills after cleaning
    print(type(companies['required_skills'][0]))
    companies['required_skills'] = companies['required_skills'].apply(clean_skills)
    #print the type of the skills after cleaning 
    print(type(companies['required_skills'][0]))
    companies.to_csv(output_dir/"companies_clean.csv", index=False)
    
    # Clean employment data
    employment = pd.read_csv(f"{input_dir}/employment.csv")
    employment['skills_used'] = employment['skills_used'].apply(clean_skills)
    employment.to_csv(output_dir/"employment_clean.csv", index=False)
    
    # Clean jobs data
    jobs = pd.read_csv(f"{input_dir}/jobs.csv")
    jobs['required_skills'] = jobs['required_skills'].apply(clean_skills)
    jobs.to_csv(output_dir/"jobs_clean.csv", index=False)
    
    # Clean users data
    users = pd.read_csv(f"{input_dir}/users.csv")
    users['skills'] = users['skills'].apply(clean_skills)
    users['skills_used'] = users['skills_used'].apply(clean_skills)
    users.to_csv(output_dir/"users_clean.csv", index=False)

if __name__ == "__main__":
    clean_data(OUTPUT_DIR, CLEAN_DATA_DIR)