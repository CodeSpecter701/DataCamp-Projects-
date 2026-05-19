import pandas as pd
import numpy as np
import os

# ==================================================
# CREATE DUMMY DATA IF FILE DOES NOT EXIST
# ==================================================

file_path = r"D:\Cleaning Bank Marketing Campaign Data\bank_marketing.csv"

if not os.path.exists(file_path):

    data = {
        "client_id": list(range(1, 11)),

        "age": [25, 32, 45, 29, 41, 38, 50, 27, 36, 44],

        "job": [
            "admin.",
            "technician",
            "blue-collar",
            "services",
            "management",
            "admin.",
            "technician",
            "blue-collar",
            "services",
            "management"
        ],

        "marital": [
            "single", "married", "married", "single", "divorced",
            "married", "single", "married", "single", "divorced"
        ],

        "education": [
            "university.degree",
            "high.school",
            "basic.9y",
            "unknown",
            "professional.course",
            "high.school",
            "basic.6y",
            "university.degree",
            "unknown",
            "professional.course"
        ],

        "credit_default": [
            "no", "yes", "no", "no", "yes",
            "no", "no", "yes", "no", "yes"
        ],

        "mortgage": [
            "yes", "no", "yes", "no", "yes",
            "yes", "no", "yes", "no", "yes"
        ],

        "number_contacts": [1, 2, 3, 1, 2, 4, 2, 1, 3, 2],

        "contact_duration": [120, 300, 150, 200, 180, 250, 90, 400, 160, 220],

        "previous_campaign_contacts": [0, 1, 2, 0, 1, 3, 0, 2, 1, 0],

        "previous_outcome": [
            "nonexistent", "success", "failure", "success", "failure",
            "success", "nonexistent", "failure", "success", "failure"
        ],

        "campaign_outcome": [
            "yes", "no", "yes", "no", "yes",
            "no", "yes", "no", "yes", "no"
        ],

        "day": [5, 12, 20, 7, 15, 10, 18, 25, 3, 30],

        "month": [
            "may", "jun", "jul", "aug", "sep",
            "may", "jun", "jul", "aug", "sep"
        ],

        "cons_price_idx": [93.2, 92.8, 93.5, 92.1, 94.0, 93.1, 92.9, 93.6, 92.2, 94.1],

        "euribor_three_months": [1.25, 1.10, 1.50, 1.75, 1.30, 1.40, 1.20, 1.60, 1.80, 1.35]
    }

    df_init = pd.DataFrame(data)

    # ==================================================
    # FIX: CREATE DIRECTORY IF IT DOES NOT EXIST
    # ==================================================

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    df_init.to_csv(file_path, index=False)

    print("✅ Dummy bank_marketing.csv created successfully!")

# ==================================================
# LOAD DATASET
# ==================================================

df = pd.read_csv(file_path)

# ==================================================
# CLIENT DATAFRAME
# ==================================================

client = df[
    [
        "client_id",
        "age",
        "job",
        "marital",
        "education",
        "credit_default",
        "mortgage"
    ]
].copy()

client["job"] = client["job"].str.replace(".", "_", regex=False)

client["education"] = (
    client["education"]
    .str.replace(".", "_", regex=False)
    .replace("unknown", np.nan)
)

client["credit_default"] = client["credit_default"].eq("yes")
client["mortgage"] = client["mortgage"].eq("yes")

# ==================================================
# CAMPAIGN DATAFRAME
# ==================================================

campaign = df[
    [
        "client_id",
        "number_contacts",
        "contact_duration",
        "previous_campaign_contacts",
        "previous_outcome",
        "campaign_outcome",
        "day",
        "month"
    ]
].copy()

campaign["previous_outcome"] = campaign["previous_outcome"].eq("success")
campaign["campaign_outcome"] = campaign["campaign_outcome"].eq("yes")

campaign["year"] = 2022

# Fix month parsing safely
campaign["month"] = campaign["month"].str.title()

campaign["last_contact_date"] = pd.to_datetime(
    campaign["day"].astype(str) + "-" +
    campaign["month"] + "-" +
    campaign["year"].astype(str),
    format="%d-%b-%Y"
)

campaign = campaign[
    [
        "client_id",
        "number_contacts",
        "contact_duration",
        "previous_campaign_contacts",
        "previous_outcome",
        "campaign_outcome",
        "last_contact_date"
    ]
]

# ==================================================
# ECONOMICS DATAFRAME
# ==================================================

economics = df[
    [
        "client_id",
        "cons_price_idx",
        "euribor_three_months"
    ]
].copy()

# ==================================================
# SAVE OUTPUT FILES
# ==================================================

client.to_csv("client.csv", index=False)
campaign.to_csv("campaign.csv", index=False)
economics.to_csv("economics.csv", index=False)

print("🚀 All CSV files created successfully!")