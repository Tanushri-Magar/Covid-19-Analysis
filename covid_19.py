# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load COVID-19 dataset
url = "https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv"
df = pd.read_csv(url)

df['Date'] = pd.to_datetime(df['Date'])

# Display the first few rows
print("🔹 First 5 rows of the dataset:")
df.head()

print("\n🔹 Dataset Info:")
print(df.info())

print("\n🔹 Summary Statistics:")
print(df.describe())

print("\n🔹 Missing Values in the Dataset:")
print(df.isnull().sum())

top_cases = df.groupby("Country")["Confirmed"].max().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
top_cases.plot(kind='bar', color='red')
plt.xlabel("Country")
plt.ylabel("Total Cases")
plt.title("Top 10 Countries with Highest COVID-19 Cases")
plt.xticks(rotation=45)
plt.show()

top_deaths = df.groupby("Country")["Deaths"].max().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
top_deaths.plot(kind='bar', color='black')
plt.xlabel("Country")
plt.ylabel("Total Deaths")
plt.title("Top 10 Countries with Highest COVID-19 Deaths")
plt.xticks(rotation=45)
plt.show()

df['Month'] = df['Date'].dt.to_period('M')
monthly_cases = df.groupby("Month")["Confirmed"].sum()

plt.figure(figsize=(12, 6))
monthly_cases.plot(color='blue', marker='o', linestyle='dashed')
plt.xlabel("Month")
plt.ylabel("Total Cases")
plt.title("Monthly Trend of COVID-19 Cases Globally")
plt.xticks(rotation=45)
plt.show()

monthly_deaths = df.groupby("Month")["Deaths"].sum()

plt.figure(figsize=(12, 6))
monthly_deaths.plot(color='brown', marker='o', linestyle='dashed')
plt.xlabel("Month")
plt.ylabel("Total Deaths")
plt.title("Monthly Trend of COVID-19 Deaths Globally")
plt.xticks(rotation=45)
plt.show()

correlation = df[['Confirmed', 'Deaths']].corr()
print("\n🔹 Correlation between Cases and Deaths:")
print(correlation)

df["Recovery Rate"] = np.where(df["Confirmed"] > 0, (df["Recovered"] / df["Confirmed"]) * 100, 0)
avg_recovery_rate = df.groupby("Country")["Recovery Rate"].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
avg_recovery_rate.plot(kind='bar', color='green')
plt.xlabel("Country")
plt.ylabel("Average Recovery Rate (%)")
plt.title("Top 10 Countries with Highest Recovery Rate")
plt.xticks(rotation=45)
plt.show()

top_countries = df.groupby("Country")["Confirmed"].max().sort_values(ascending=False).head(10)

plt.figure(figsize=(8, 8))
plt.pie(top_countries, labels=top_countries.index, autopct='%1.1f%%',
        colors=['red', 'blue', 'green', 'yellow', 'purple', 'pink', 'orange', 'cyan', 'gray', 'brown'])
plt.title("Global COVID-19 Cases Distribution (Top 10 Countries)")
plt.show()

print("COVID-19 Data Analysis Completed Successfully!")

