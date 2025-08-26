# US Accidents Analysis - Task 04

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap

# Load dataset
df = pd.read_csv("US_Accidents_March23.csv")

# Basic cleaning
df.drop(columns=['Number', 'Zipcode', 'Airport_Code', 'Turning_Loop'], inplace=True, errors='ignore')
df.dropna(subset=['Start_Time', 'End_Time', 'Weather_Condition', 'Street'], inplace=True)

# Extract hour from Start_Time
df['Hour'] = pd.to_datetime(df['Start_Time']).dt.hour

# -------------------------------
# 1. Accidents by Hour of Day
plt.figure(figsize=(12,6))
sns.countplot(x='Hour', data=df, palette='viridis')
plt.title("Accidents by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Number of Accidents")
plt.tight_layout()
plt.show()

# -------------------------------
# 2. Top Weather Conditions
plt.figure(figsize=(14,6))
top_weather = df['Weather_Condition'].value_counts().nlargest(10)
sns.barplot(x=top_weather.index, y=top_weather.values, palette='coolwarm')
plt.title("Top 10 Weather Conditions During Accidents")
plt.xticks(rotation=45)
plt.ylabel("Accident Count")
plt.tight_layout()
plt.show()

# -------------------------------
# 3. Road Side Distribution
plt.figure(figsize=(6,4))
sns.countplot(x='Side', data=df, palette='Set2')
plt.title("Accidents by Road Side")
plt.tight_layout()
plt.show()

# -------------------------------
# 4. Traffic Signal Presence
plt.figure(figsize=(6,4))
sns.countplot(x='Traffic_Signal', data=df, palette='Set1')
plt.title("Accidents Near Traffic Signals")
plt.tight_layout()
plt.show()

# -------------------------------
# 5. Accident Hotspots (Heatmap)
sample_df = df[['Start_Lat', 'Start_Lng']].dropna().sample(10000)
map = folium.Map(location=[39.5, -98.35], zoom_start=5)
HeatMap(data=sample_df.values.tolist()).add_to(map)
map.save("accident_hotspots.html")  # Opens in browser

# -------------------------------
# 6. Correlation with Severity
plt.figure(figsize=(8,6))
corr = df[['Severity', 'Visibility(mi)', 'Temperature(F)', 'Humidity(%)']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation with Severity")
plt.tight_layout()
plt.show()
