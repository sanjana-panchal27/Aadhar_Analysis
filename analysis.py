import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# 1. Load Dataset
# -------------------------------
df = pd.read_csv("data/aadhaar_statewise.csv")


# -------------------------------
# 2. Basic Inspection
# -------------------------------
print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nColumn Names:")
print(df.columns)

# -------------------------------
# 3. Data Cleaning & Processing
# -------------------------------

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'], dayfirst=True)

# Create total enrolment column
df['total_enrolment'] = (
    df['age_0_5'] +
    df['age_5_17'] +
    df['age_18_greater']
)

# -------------------------------
# 4. State-wise Analysis
# -------------------------------
state_wise = (
    df.groupby('state')['total_enrolment']
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))
state_wise.plot(kind='bar')
plt.title("State-wise Aadhaar Enrolment")
plt.xlabel("State")
plt.ylabel("Total Enrolments")
plt.tight_layout()
plt.savefig("state_wise_enrolment.png")
plt.close()

# -------------------------------
# 5. Age-wise Analysis
# -------------------------------
age_wise = df[['age_0_5', 'age_5_17', 'age_18_greater']].sum()

plt.figure(figsize=(6,6))
age_wise.plot(kind='pie', autopct='%1.1f%%')
plt.title("Age-wise Aadhaar Enrolment Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("age_wise_enrolment.png")
plt.close()

# -------------------------------
# 6. District-wise Analysis (Top 10)
# -------------------------------
district_wise = (
    df.groupby('district')['total_enrolment']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(8,5))
district_wise.plot(kind='bar')
plt.title("Top 10 Districts by Aadhaar Enrolment")
plt.xlabel("District")
plt.ylabel("Total Enrolments")
plt.tight_layout()
plt.savefig("top_districts_enrolment.png")
plt.close()

# -------------------------------
# 7. Time Trend Analysis
# -------------------------------
date_wise = df.groupby('date')['total_enrolment'].sum()

plt.figure(figsize=(8,5))
date_wise.plot()
plt.title("Aadhaar Enrolment Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Total Enrolments")
plt.tight_layout()
plt.savefig("time_trend_enrolment.png")
plt.close()

print("\nAnalysis completed successfully.")
