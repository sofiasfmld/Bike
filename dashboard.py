import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load data
main_data = pd.read_csv("main_data.csv")

# Convert date columns correctly
main_data['dteday'] = pd.to_datetime(main_data['dteday'], errors='coerce')

# Set title of the dashboard
st.title("Bike Sharing Dashboard")

# Section 1: Total Rentals per Hour
st.header("Total Rentals per Hour")
total_rentals_per_hour = main_data.groupby('hr')['cnt'].sum()
st.bar_chart(total_rentals_per_hour)

# Section 2: Average Rentals by Weather Situation
st.header("Average Rentals by Weather Situation")
avg_rentals_weather_hour = main_data.groupby(['weathersit', 'hr'])['cnt'].mean().unstack()
st.line_chart(avg_rentals_weather_hour)

# Section 3: Monthly Rentals
st.header("Total Rentals per Month")
monthly_rentals = main_data.groupby(main_data['dteday'].dt.month)['cnt'].sum()
st.line_chart(monthly_rentals)

# Section 4: Rentals by Weekday
st.header("Average Rentals by Weekday")
weekday_rentals = main_data.groupby(main_data['dteday'].dt.weekday)['cnt'].mean()
st.bar_chart(weekday_rentals)

# Section 5: Rentals by Weather Situation
st.header("Average Rentals by Weather Situation")
weather_rentals = main_data.groupby('weathersit')['cnt'].mean()
st.bar_chart(weather_rentals)

# Section 6: Rentals by Holiday
st.header("Rentals on Holidays vs Normal Days")
holiday_counts = main_data.groupby('holiday')['cnt'].sum()
st.bar_chart(holiday_counts)

# Section 7: User Type Distribution
st.header("User Type Distribution")
user_counts = main_data[['casual', 'registered']].sum()
st.write(user_counts)

# Section 8: RFM Analysis
st.header("RFM Analysis")

# Calculate RFM values
rfm_df = main_data.groupby(by="registered", as_index=False).agg({
    "dteday": "max",
    "cnt": "sum"
})

rfm_df.columns = ["customer_id", "max_rental_date", "monetary"]
recent_date = main_data['dteday'].max()
rfm_df['max_rental_date'] = pd.to_datetime(rfm_df['max_rental_date'], errors='coerce')
rfm_df["recency"] = rfm_df["max_rental_date"].apply(lambda x: (recent_date - x).days)
rfm_df['frequency'] = main_data.groupby('registered')['cnt'].count().values
rfm_df.drop("max_rental_date", axis=1, inplace=True)

# Display RFM DataFrame
st.write(rfm_df)

# Visualize RFM
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(20, 6))
colors = ["#72BCD4"] * 5

# Bar plot for Recency
sns.barplot(y="recency", x="customer_id", data=rfm_df.sort_values(by="recency", ascending=True).head(5), palette=colors, ax=ax[0])
ax[0].set_title("By Recency (days)", loc="center", fontsize=18)

# Bar plot for Frequency
sns.barplot(y="frequency", x="customer_id", data=rfm_df.sort_values(by="frequency", ascending=False).head(5), palette=colors, ax=ax[1])
ax[1].set_title("By Frequency", loc="center", fontsize=18)

# Bar plot for Monetary
sns.barplot(y="monetary", x="customer_id", data=rfm_df.sort_values(by="monetary", ascending=False).head(5), palette=colors, ax=ax[2])
ax[2].set_title("By Monetary", loc="center", fontsize=18)

plt.suptitle("Best Customer Based on RFM Parameters (customer_id)", fontsize=20)

# Display RFM plot
st.pyplot(fig)
