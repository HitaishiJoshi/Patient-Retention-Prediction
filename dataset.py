import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import matplotlib.pyplot as plt
import json

# Setting the number of records to generate
num_records = 100000
np.random.seed(42)


with open("address.json", "r") as f:
    clinic_locations = json.load(f).get("Clinic Location")

with open("FMS_Data.json", "r") as f:
    Illness_type = json.load(f).get("Illness type?")

with open("FMS_Data.json", "r") as f:
    transport = json.load(f).get("Mode of transport")

with open("FMS_Data.json", "r") as f:
    health_insurance = json.load(f).get("Health Ins. Type")

with open("FMS_Data.json", "r") as f:
    reason_for_missing = json.load(f).get("Reason for missing")

with open("FMS_Data.json", "r") as f:
    Comorbidities = json.load(f).get("Comorbidities")

with open("FMS_Data.json", "r") as f:
    access_type = json.load(f).get("Access Type")

with open("FMS_Data.json", "r") as f:
    blood_presure = json.load(f).get("Frequency of Blood Pressure Fluctuations")

# Helper functions to generate specific fields
def generate_random_date(start_date, end_date):
    # Generate random dates within the specified range with no more than 6 patients per day
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date.strftime("%Y-%m-%d")

def generate_case_assigned():
    case_assigned = np.random.choice(["True", "False"], p=[0.7, 0.3])
    return case_assigned == "True"

def generate_action_taken(case_assigned):
    return np.random.choice(["Call", "Email", "SMS"]) if case_assigned else "None"

def generate_case_duration_v4(case_assigned, days_enrolled, age):
    if not case_assigned:
        return 0
    base_duration = np.random.randint(1, min(days_enrolled, 90))
    return base_duration if age <= 60 else min(base_duration + 30, days_enrolled)

def generate_street_address():
    street_number = random.randint(20, 9999)
    street_name = random.choice(["Main St", "Highland Ave", "Maple St", "Broadway", "Sunset Blvd", "Park Ave", "Queens Blvd", "Hollywood Blvd", "Wall St", "Elm St", "Cambridge St", "Pine St", "Cedar St", "Oak St", "Washington St", "Market St", "Chestnut St", "River Rd", "Lake St", "Spring St", "Knox Rd", "Church St", "College Ave", "Grove St", "Hill St", "Forest Ave", "Meadow St", "Valley Rd", "Jefferson St", "Madison Ave", "Monroe St", "Adams St", "Lincoln St", "Grant St", "Jackson St", "Franklin St", "Wilson St", "Taylor St", "Tyler St", "Hamilton St", "Johnson St", "Harrison St", "Buchanan St", "Truman St", "Eisenhower St", "Kennedy St", "Reagan St", "Clinton St", "Bush St", "Obama St", "Trump St", "Biden St"])
    return f"{street_number} {street_name}"

# Start and end dates for enrollment
start_date = datetime.strptime("2022-01-01", "%Y-%m-%d")
end_date = datetime.strptime("2024-10-30", "%Y-%m-%d")

# Main data dictionary
data_v4 = {
    "Date of enrollment": [generate_random_date(start_date, end_date) for _ in range(num_records)],
    "Patient ID": [f"P{str(i).zfill(6)}" for i in range(1, num_records + 1)],
    "COC ID": [f"C{str(random.randint(1, 12)).zfill(2)}" for _ in range(num_records)],
    "Case Assigned": [],
    "Action Taken": [],
    "Days Enrolled": [],
    "Case duration in days": [],
    "Illness type?": [random.choice(Illness_type) for _ in range(num_records)],
    "At home?": [random.choice(["True", "False"]) for _ in range(num_records)],
    "Patient Age": [np.random.choice([random.randint(18, 44), random.randint(45, 65), random.randint(66, 90)], p=[0.1, 0.6, 0.3]) for _ in range(num_records)],
    "Patient Gender": np.random.choice(["Male", "Female", "Other"], num_records),
    "Preferred Language": [random.choice(["English", "Spanish"]) for _ in range(num_records)],
    "Patient Ethnic Background": [random.choice(["Caucasian", "African American", "Hispanic", "Asian", "Native American", "Others"]) for _ in range(num_records)],
    # "Patient Address": [],
    # "Patient City": [],
    # "Patient State": [],
    "Lives Alone?": [random.choice(["True", "False"]) for _ in range(num_records)],
    "Mode of transport": [random.choice(transport) for _ in range(num_records)],
    "Number of treatments till date": [],
    "Mortality in 52 weeks": [],
    "# consecutive missed treatments ": [],
    "# treatments in 3 Months": np.random.randint(0, 36, num_records),
    "# of grievances?": [],
    "Hospitalization Days": [],
    "Hospitalization Status": np.random.choice(["True", "False"], num_records),
    "Distance from clinic": [random.randint(1, 50) for _ in range(num_records)],
    "Clinic NPS": [],
    "Health Ins. Type": [random.choice(health_insurance) for _ in range(num_records)],
    "Reason for missing": [random.choice(reason_for_missing) for _ in range(num_records)],
    "Support Programs Participation": [random.choice(["True", "False"]) for _ in range(num_records)],
    "Medications Compliance Score": [],
    "Financial Challenges": [random.choice(["True", "False"]) for _ in range(num_records)],
    "Number of Different Care Settings": [],
    "Comorbidities": [random.choice(Comorbidities) for _ in range(num_records)],
    "Physical Activity and Well-being": ["True" if random.random() > 0.5 else "False" for _ in range(num_records)],
    "Patient Engagement via PatientHub": ["True" if random.random() > 0.5 else "False" for _ in range(num_records)],
    "Care Team Relationship Score": [],
    "Dialysis-Related Complications": [],
    # "Clinic Location": random.choice(clinic_locations),
    # "Clinic Location": [],
    "Clinic Size": [random.choice(["Small", "Medium", "Large"]) for _ in range(num_records)],
    "Clinic Hygiene": [random.choice(["Excellent", "Good", "Average", "Poor"]) for _ in range(num_records)],
    "Patient Satisfaction Score": [],
    "Social Support Availability": [random.choice(["True", "False"]) for _ in range(num_records)],
    "Frequency of Emotional Health Support": [],
    "Dialysis Shift Timing": [random.choice(["Morning", "Afternoon", "Evening", "Night"]) for _ in range(num_records)],
    "Access Type": [random.choice(access_type) for _ in range(num_records)],
    "Number of Care Team Changes": [],
    "Nutritional Counseling Attendance": [random.choice(["True", "False"]) for _ in range(num_records)],
    "Time in Current Dialysis Modality": np.random.randint(1, 60, num_records),
    "Appointment Reminder Type": [random.choice(["Call", "Email", "SMS"]) for _ in range(num_records)],
    "Frequency of Access Complications": [],
    "Involvement in Peer Support Groups": [random.choice(["True", "False"]) for _ in range(num_records)],
    "Patient Activation Measure (PAM) Score": [],
    "Blood Pressure Fluctuations": [random.choice(blood_presure) for _ in range(num_records)],
    "Accessibility to Emergency Care": [random.choice(["True", "False"]) for _ in range(num_records)],
    "Retention": [random.choice(["True", "False"]) for _ in range(num_records)],
}

# Populate dependent fields
for i in range(num_records):
    age = data_v4["Patient Age"][i]
    clinic_hygiene = data_v4["Clinic Hygiene"][i]
    # clinic = data_v4["Clinic Location"][i]
    days_enrolled = np.random.randint(365, 730) if age > 60 else np.random.randint(30, 730)
    case_assigned = generate_case_assigned()
    treatments = int(days_enrolled * np.random.uniform(0.4, 1))
    clinic_nps = random.randint(8, 10) if clinic_hygiene in ["Excellent", "Good"] else random.randint(0, 7)
    care_team_score = [random.choice(["Excellent", "Good"]) if clinic_nps > 8 else random.choice(["Average", "Poor"])]
    # city, state = clinic.split(", ")
    # address = generate_street_address()

    data_v4["Days Enrolled"].append(days_enrolled)
    data_v4["Case Assigned"].append(case_assigned)
    data_v4["Action Taken"].append(generate_action_taken(case_assigned))
    data_v4["Case duration in days"].append(generate_case_duration_v4(case_assigned, days_enrolled, age))
    data_v4["Mortality in 52 weeks"].append(round(np.random.uniform(0.6 if age > 60 else 0.2, 0.8), 2))
    data_v4["Number of treatments till date"].append(treatments)
    # data_v4["Patient Address"].append(address)
    # data_v4["Patient City"].append(city)
    # data_v4["Patient State"].append(state)
    data_v4["# consecutive missed treatments "].append(int(treatments * np.random.uniform(0.01, 0.3)))
    data_v4["# of grievances?"].append(np.random.randint(0, 5) if age <= 60 else np.random.randint(5, 10))
    data_v4["Hospitalization Days"].append(min(np.random.randint(0, 90), days_enrolled))
    data_v4["Dialysis-Related Complications"].append(np.random.randint(0, 5 if age > 60 else 3))
    data_v4["Patient Satisfaction Score"].append(np.random.randint(5, 10) if age < 45 else np.random.randint(1, 10))
    data_v4["Clinic NPS"].append(clinic_nps)
    data_v4["Care Team Relationship Score"].append(care_team_score)
    data_v4["Patient Activation Measure (PAM) Score"].append(np.random.randint(6, 10) if age < 45 else np.random.randint(1, 5))
    data_v4["Frequency of Access Complications"].append(np.random.randint(1, 10) if age > 60 else np.random.randint(1, 5))
    data_v4["Number of Care Team Changes"].append(np.random.randint(5, 10) if 50 <= age <= 70 else np.random.randint(1, 5))
    data_v4["Frequency of Emotional Health Support"].append(min(np.random.randint(5, 20), days_enrolled) if 30 <= age <= 60 else np.random.randint(1, 10))
    data_v4["Number of Different Care Settings"].append(np.random.randint(5, 10) if age > 50 else np.random.randint(1, 5))
    data_v4["Medications Compliance Score"].append(np.random.randint(5, 10) if age > 50 else np.random.randint(1, 10))

# Convert data to DataFrame and save to CSV
df_v4 = pd.DataFrame(data_v4)
output_file_path_v4 = 'FMS_Dataset.csv'
df_v4.to_csv(output_file_path_v4, index=False)
print(f"Data saved to {output_file_path_v4}")