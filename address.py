import pandas as pd
import random
import faker
import json

fake = faker.Faker()

num_records = 100000

def random_choice(choices):
    return random.choice(choices)

def extract_left_cell_data(df, target_col):
    '''Function to extract the data from the left cell of the target column'''
    return df[target_col].shift(1)


with open("data_example.json", "r") as f:
    clinic_locations = json.load(f).get("Clinic Location")

# Helper function to generate random street addresses
def generate_street_address():
    street_number = random.randint(20, 9999)
    street_name = random.choice(["Main St", "Highland Ave", "Maple St", "Broadway", "Sunset Blvd", "Park Ave", "Queens Blvd", "Hollywood Blvd", "Wall St", "Elm St", "Cambridge St", "Pine St", "Cedar St", "Oak St", "Washington St", "Market St", "Chestnut St", "River Rd", "Lake St", "Spring St", "Knox Rd", "Church St", "College Ave", "Grove St", "Hill St", "Forest Ave", "Meadow St", "Valley Rd", "Jefferson St", "Madison Ave", "Monroe St", "Adams St", "Lincoln St", "Grant St", "Jackson St", "Franklin St", "Wilson St", "Taylor St", "Tyler St", "Hamilton St", "Johnson St", "Harrison St", "Buchanan St", "Truman St", "Eisenhower St", "Kennedy St", "Reagan St", "Clinton St", "Bush St", "Obama St", "Trump St", "Biden St"])
    return f"{street_number} {street_name}"

# Generating data with diversified city names by iterating over all available locations
data = []
for _ in range(100000):
    clinic = random.choice(clinic_locations)
    city, state = clinic.split(", ")
    address = generate_street_address()
    data.append({
        "Patient Address": address,
        "Patient City": city,
        "Patient State": state,
        "Clinic Location": clinic
    })

# Creating the DataFrame
df = pd.DataFrame(data)

# Saving the DataFrame to a CSV file
output_path = 'generated_patient_addresses_diverse.csv'
df.to_csv(output_path, index=False)

print(f"Data saved to {output_path}")
