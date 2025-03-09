from textwrap import indent

import pandas as pd
from faker import Faker
import random
import json


def generate_employee_data(num_records, seed=None):
    fake = Faker()
    if seed:
        Faker.seed(seed)  # Set seed for reproducibility

    data = {
        "Employee_ID": [fake.unique.random_int(min=1000, max=9999) for _ in range(num_records)],
        "Employee_Name": [fake.name() for _ in range(num_records)],
        "Email_ID": [fake.email() for _ in range(num_records)],
        "DOB": [fake.date_of_birth(minimum_age=22, maximum_age=60).strftime("%Y-%m-%d") for _ in range(num_records)],
        "Salary": [random.randint(30000, 120000) for _ in range(num_records)]
    }

    return pd.DataFrame(data)

# Generate first set of employee data
df1 = generate_employee_data(10, seed=12)

df1.to_csv("EmpTestdata2.csv", index=False)
# df1.to_json("emptestdata2.json", orient="records", indent=4)