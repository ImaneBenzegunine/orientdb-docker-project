import pandas as pd
import networkx as nx
import json
from pathlib import Path
from typing import Dict, List
from path import CLEAN_DATA_DIR,GRAPH_DATA_DIR
# Configuration
INPUT_DIR = CLEAN_DATA_DIR # Docker volume path for input CSVs
OUTPUT_DIR = GRAPH_DATA_DIR # Docker volume path for graph outputs
GRAPH_FILE = "professional_network.graphml"

def load_clean_data() -> Dict[str, pd.DataFrame]:
    """Load cleaned CSV files from the volume"""
    return {
        "users": pd.read_csv(f"{INPUT_DIR}/users_clean.csv"),
        "companies": pd.read_csv(f"{INPUT_DIR}/companies_clean.csv"),
        "jobs": pd.read_csv(f"{INPUT_DIR}/jobs_clean.csv"),
        "employment": pd.read_csv(f"{INPUT_DIR}/employment_clean.csv")
    }

def convert_skills(skill_str: str) -> Dict:
    """Convert string representation of skills to dict"""
    try:
        return json.loads(skill_str.replace("'", "\""))
    except:
        return {}

def create_professional_network(data: Dict[str, pd.DataFrame]) -> nx.Graph:
    """Create a directed graph of professional relationships"""
    G = nx.DiGraph()
    
    # Add users as nodes
    for _, user in data["users"].iterrows():
        G.add_node(
            user["user_id"],
            type="user",
            name=user["name"],
            email=user["email"],
            skills=convert_skills(user["skills"]),
            **user[["position", "duration_years"]].to_dict()
        )
    
    # Add companies as nodes
    for _, company in data["companies"].iterrows():
        G.add_node(
            company["company_id"],
            type="company",
            name=company["name"],
            required_skills=convert_skills(company["required_skills"])
        )
    
    # Add employment relationships as edges
    for _, employment in data["employment"].iterrows():
        G.add_edge(
            employment["user_id"],
            employment["company_id"],
            relationship="employment",
            position=employment["position"],
            start_date=employment["start_date"],
            end_date=employment["end_date"],
            skills_used=convert_skills(employment["skills_used"])
        )
    
    # Add skill similarity edges between users
    user_skills = {
        row["user_id"]: set(convert_skills(row["skills"]).keys()) 
        for _, row in data["users"].iterrows()
    }
    
    user_ids = list(user_skills.keys())
    for i in range(len(user_ids)):
        for j in range(i+1, len(user_ids)):
            u1, u2 = user_ids[i], user_ids[j]
            common_skills = user_skills[u1] & user_skills[u2]
            if common_skills:
                G.add_edge(
                    u1, u2,
                    relationship="skill_similarity",
                    weight=len(common_skills)/min(len(user_skills[u1]), len(user_skills[u2])),
                    common_skills=list(common_skills)
                )
    
    return G

def save_graph(G: nx.Graph, output_dir: str):
    """Save graph in multiple formats"""
    Path(output_dir).mkdir(exist_ok=True, parents=True)
    
    # Save as GraphML for OrientDB import
    nx.write_graphml(G, f"{output_dir}/{GRAPH_FILE}")
    
    # Save edge list for simple analysis
    nx.write_edgelist(G, f"{output_dir}/professional_network.edgelist")
    
    print(f"Graph saved with {len(G.nodes())} nodes and {len(G.edges())} edges")

if __name__ == "__main__":
    print("Loading cleaned data...")
    data = load_clean_data()
    
    print("Creating professional network graph...")
    G = create_professional_network(data)
    
    print("Saving graph files...")
    save_graph(G, OUTPUT_DIR)
    print("Graph generation complete!")