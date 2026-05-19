📊 Bank Marketing Campaign Data Pipeline
🧠 Project Overview

This project demonstrates a data cleaning, transformation, and structuring pipeline built using Python.
It simulates a real-world bank marketing campaign dataset, where raw customer data is processed into clean, analytics-ready tables.

The goal is to transform a single messy dataset into a normalized multi-table structure, similar to what is used in data warehouses and production ETL pipelines.

🏦 Business Context

Banks run marketing campaigns to promote term deposits and financial products.
Understanding customer behavior helps optimize:

Campaign targeting 🎯
Conversion rates 📈
Customer segmentation 👥
Financial decision-making 💰

This pipeline prepares data for such analysis by structuring it into clean relational datasets.

⚙️ Tech Stack
🐍 Python 3.x
📦 Pandas
🔢 NumPy
💾 OS Module (file handling)
🏗️ Project Architecture

The dataset is transformed into three structured tables:

1. 👤 Client Table

Contains demographic and personal banking information.

Column	Description
client_id	Unique customer ID
age	Age of client
job	Occupation type
marital	Marital status
education	Education level
credit_default	Has credit default (True/False)
mortgage	Has housing loan (True/False)
2. 📞 Campaign Table

Contains marketing interaction details.

Column	Description
client_id	Unique customer ID
number_contacts	Number of campaign contacts
contact_duration	Last contact duration (seconds)
previous_campaign_contacts	Previous contacts count
previous_outcome	Previous campaign success (True/False)
campaign_outcome	Current campaign success (True/False)
last_contact_date	Final structured contact date
3. 📊 Economics Table

Contains macroeconomic indicators affecting campaign outcomes.

Column	Description
client_id	Unique customer ID
cons_price_idx	Consumer Price Index
euribor_three_months	Euribor 3-month rate
🔄 Data Pipeline Workflow
📥 Load dataset (or generate dummy data if file missing)
🧹 Clean and standardize categorical values
🔁 Convert string features into boolean indicators
📅 Construct proper datetime fields
🧩 Normalize dataset into multiple relational tables
💾 Export cleaned CSV files
📂 Output Files

After execution, the pipeline generates:

client.csv
campaign.csv
economics.csv

These files are analytics-ready and can be used for:

SQL analysis
Power BI dashboards
Machine learning models
Data warehouse ingestion
🚀 Key Features

✔ Automatic dataset creation if file is missing
✔ Clean feature engineering pipeline
✔ Boolean conversion for ML readiness
✔ Date parsing & transformation
✔ Modular dataframe separation (normalized design)
✔ Production-style ETL structure

📌 Example Use Cases
Customer segmentation analysis
Campaign success prediction
Financial behavior modeling
BI dashboard reporting
ETL pipeline simulation
🧪 How to Run
# Step 1: Clone repo
git clone https://github.com/CodeSpecter701/DataCamp-Projects-.git

# Step 2: Navigate into project
cd DataCamp-Projects-

# Step 3: Install dependencies
pip install pandas numpy

# Step 4: Run script
python your_script_name.py
📈 Future Improvements
Add SQL database integration (PostgreSQL / MySQL)
Build Power BI dashboard on output tables
Deploy pipeline using Airflow or Prefect
Add logging & error handling system
Containerize using Docker 🐳
👨‍💻 Author

Qaiser Anoosh Mughal
Aspiring Data Engineer | AWS | Data Pipelines | Cloud Analytics

📜 License

This project is open-source and available under the MIT License.
