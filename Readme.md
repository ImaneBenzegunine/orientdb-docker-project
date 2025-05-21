# Job Recommendation Engine with OrientDB — 🚧 Work in Progress

## 🎯 Project Goal
**Build a graph-based job recommendation system** that:
- Matches candidates to jobs based on skill compatibility
- Recommends career paths using employment history graphs
- Identifies skill gaps for career advancement
- Visualizes professional networks and opportunities

## 🌟 Key Features
| Feature | Description | Technology Used |
|---------|-------------|-----------------|
| Skill Matching | Recommends jobs based on skill overlap between candidates and positions | OrientDB Graph Queries |
| Career Pathing | Suggests progression paths using historical employment patterns | NetworkX + GDS Algorithms |
| Gap Analysis | Identifies missing skills for target positions | Spark ML |
| Real-time Dashboard | Interactive visualization of recommendations | Streamlit |



## 🛠️ Tech Stack

| Component          | Technology               |
|--------------------|--------------------------|
| Database           | OrientDB 3.1.10          |
| Data Generation    | Python Faker, NetworkX   |
| ETL                | Apache Spark, PyOrient   |
| Orchestration      | Airflow                  |
| Visualization      | Streamlit, Metabase      |
| Containerization   | Docker                   |

## 🚀 Quick Start

### Prerequisites
- Docker 20.10+
- Docker Compose 2.0+
- Python 3.8+

### Installation
```bash
## Prerequisites
- Docker Desktop ([Download](https://www.docker.com/products/docker-desktop))


## Setup
```bash
# 1. Clone this repository
git clone https://github.com/ImaneBenzegunine/GraphNest.git
cd GraphNest

# 2. Start OrientDB
docker-compose up -d

## Create a virtual environment:
✅ 1. Create the virtual environment : In your project directory (where your Python files are), run:

python -m venv venv

This creates a virtual environment named venv.

✅ 2. Activate the virtual environment

venv\Scripts\activate

✅ 3. Install the requirements
Run the following command:


pip install -r requirements.txt


✅ 4. Run your  project
Once all dependencies are installed, you can start your app (assuming it's in a file like app.py) using:

python Script.py
