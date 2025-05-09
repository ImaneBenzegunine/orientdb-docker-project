from faker import Faker
from faker.providers import DynamicProvider
import random

# Custom providers
professional_skills = DynamicProvider(
    provider_name="professional_skills",
    elements=["Python", "Spark", "OrientDB", "SQL","Data Engineering", "Machine Learning"]
)

job_titles = DynamicProvider(
    provider_name="job_titles",
    elements=["Data Engineer", "Graph Analyst", "ETL Developer"]
)
company = DynamicProvider(
    provider_name="company",
    elements=["IBM", "Oracle", "AWS","Meta","Accenture"]
)
fake = Faker('en_IN')
fake.add_provider(professional_skills)
fake.add_provider(job_titles)

def generate_user():
    return {
        "id_user":fake.unique.random_number(digits=8),
        "name": fake.name(),
        "email": fake.email(),
        "headline": f"{fake.job_title()} at {fake.company()}",
        "skills": [fake.professional_skill() for _ in range(random.randint(3,8))],
        "experience": [
            {
                "company": fake.company(),
                "position": fake.job_title(),
                "duration": f"{random.randint(1,5)} years"
            } for _ in range(random.randint(1,4))
        ]
    }
def generate_company():
    return {
        "id_company":fake.unique.random_number(digits=6),
        "name": [fake.company() for _ in range(random.randint(3,8))],
        "post": [fake.job_titles() for _ in range(random.randint(3,8))],
        "people": [
            {
                "id_user":id_user.generate_user(),
                "position": fake.job_title(),
                "duration": f"{random.randint(1,5)} years"
                "skills":,
                
            } for _ in range(random.randint(1,4))
        ]
    }
def save_blinkit_data(data_dict, prefix='blinkit_'):
    """Save all generated DataFrames to CSV files"""
    for name, df in data_dict.items():
        df.to_csv(f'{prefix}{name}.csv', index=False)
# Generate and save the data with custom date range
data = generate_complete_blinkit_data(start_date='2023-01-01', end_date='2025-12-31')
save_blinkit_data(data)