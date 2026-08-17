import pandas as pd
df = pd.read_csv("Day10_Flight_Operations_Dataset.csv")
print("===== FLIGHT OPERATIONS DATA ANALYSIS =====")

# 2. Basic Dataset Information
print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== LAST 5 ROWS =====")
print(df.tail())

print("\n===== RANDOM SAMPLE =====")
print(df.sample(5))

print("\n===== DATASET SHAPE =====")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

print("\n===== DATA TYPES =====")
print(df.dtypes)

# 3. Dataset Information
print("\n===== DATASET INFO =====")
df.info()

# 4. Descriptive Statistics
print("\n===== DESCRIPTIVE STATISTICS =====")
print(df.describe())

# 5. Missing Values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# 6. Date Transformation
df["Flight_Date"] = pd.to_datetime(df["Flight_Date"])

df["Flight_Year"] = df["Flight_Date"].dt.year
df["Flight_Month"] = df["Flight_Date"].dt.month
df["Day_of_Week"] = df["Flight_Date"].dt.day_name()

print("\n===== DATE TRANSFORMATION =====")
print(df[[
    "Flight_Date",
    "Flight_Year",
    "Flight_Month",
    "Day_of_Week"
]].head())

# 7. Data Selection
print("\n===== SELECTED FLIGHT DATA =====")
print(df[[
    "Flight_ID",
    "Airline",
    "Origin",
    "Destination",
    "Passengers",
    "Flight_Status"
]].head(10))

# 8. Filtering
print("\n===== DELAYED FLIGHTS =====")
delayed_flights = df[df["Flight_Status"] == "Delayed"]
print(delayed_flights[[
    "Flight_ID",
    "Airline",
    "Origin",
    "Destination",
    "Delay_Minutes"
]].head(10))

print("\n===== FLIGHTS WITH DELAY MORE THAN 30 MINUTES =====")
long_delay = df[df["Delay_Minutes"] > 30]
print(long_delay[[
    "Flight_ID",
    "Airline",
    "Delay_Minutes",
    "Weather"
]].head(10))

print("\n===== HIGH SATISFACTION FLIGHTS =====")
high_satisfaction = df[df["Passenger_Satisfaction"] >= 4]
print(high_satisfaction[[
    "Flight_ID",
    "Airline",
    "Passenger_Satisfaction"
]].head(10))

# 9. Sorting
print("\n===== TOP FLIGHTS BY TICKET PRICE =====")
top_price = df.sort_values(
    by="Average_Ticket_Price",
    ascending=False
)
print(top_price[[
    "Flight_ID",
    "Airline",
    "Travel_Class",
    "Average_Ticket_Price"
]].head(10))

print("\n===== LONGEST DELAYS =====")
top_delays = df.sort_values(
    by="Delay_Minutes",
    ascending=False
)
print(top_delays[[
    "Flight_ID",
    "Airline",
    "Delay_Minutes",
    "Weather"
]].head(10))

# 10. Airline-wise Analysis
print("\n===== AIRLINE-WISE ANALYSIS =====")
airline_summary = df.groupby("Airline").agg(
    Total_Passengers=("Passengers", "sum"),
    Average_Passengers=("Passengers", "mean"),
    Average_Delay=("Delay_Minutes", "mean"),
    Average_Satisfaction=("Passenger_Satisfaction", "mean"),
    Average_Ticket_Price=("Average_Ticket_Price", "mean")
)
print(airline_summary)

# 11. Flight Status Analysis
print("\n===== FLIGHT STATUS =====")
print(df["Flight_Status"].value_counts())

# 12. Weather Analysis
print("\n===== WEATHER-WISE FLIGHT COUNT =====")
print(df["Weather"].value_counts())

print("\n===== WEATHER-WISE AVERAGE DELAY =====")
weather_delay = df.groupby("Weather")["Delay_Minutes"].mean()
print(weather_delay.sort_values(ascending=False))

# 13. Travel Class Analysis
print("\n===== TRAVEL CLASS ANALYSIS =====")
class_summary = df.groupby("Travel_Class").agg(
    Total_Passengers=("Passengers", "sum"),
    Average_Ticket_Price=("Average_Ticket_Price", "mean"),
    Average_Satisfaction=("Passenger_Satisfaction", "mean")
)
print(class_summary)

# 14. Aircraft Analysis
print("\n===== AIRCRAFT ANALYSIS =====")
aircraft_summary = df.groupby("Aircraft").agg(
    Number_of_Flights=("Flight_ID", "count"),
    Total_Passengers=("Passengers", "sum"),
    Average_Delay=("Delay_Minutes", "mean")
)
print(aircraft_summary)

# 15. Origin-wise Analysis
print("\n===== ORIGIN-WISE PASSENGERS =====")
origin_summary = df.groupby("Origin")["Passengers"].sum()
print(origin_summary.sort_values(ascending=False))

# 16. Destination-wise Analysis
print("\n===== DESTINATION-WISE PASSENGERS =====")
destination_summary = df.groupby("Destination")["Passengers"].sum()
print(destination_summary.sort_values(ascending=False))

# 17. Booking Channel Analysis
print("\n===== BOOKING CHANNEL ANALYSIS =====")
booking_summary = df.groupby("Booking_Channel").agg(
    Number_of_Flights=("Flight_ID", "count"),
    Average_Ticket_Price=("Average_Ticket_Price", "mean"),
    Average_Satisfaction=("Passenger_Satisfaction", "mean")
)
print(booking_summary)

# 18. Meal Preference Analysis
print("\n===== MEAL PREFERENCE =====")
print(df["Meal_Preference"].value_counts())

# 19. Overall Statistics
print("\n===== OVERALL STATISTICS =====")

print("Total Flights:", df["Flight_ID"].nunique())
print("Total Passengers:", df["Passengers"].sum())
print("Average Passengers per Flight:",
      round(df["Passengers"].mean(), 2))

print("Average Ticket Price:",
      round(df["Average_Ticket_Price"].mean(), 2))

print("Highest Ticket Price:",
      df["Average_Ticket_Price"].max())

print("Lowest Ticket Price:",
      df["Average_Ticket_Price"].min())

print("Average Delay:",
      round(df["Delay_Minutes"].mean(), 2))

print("Maximum Delay:",
      df["Delay_Minutes"].max())

print("Average Satisfaction:",
      round(df["Passenger_Satisfaction"].mean(), 2))

# 20. On-Time Percentage
print("\n===== ON-TIME PERFORMANCE =====")
on_time_percentage = (
    (df["Flight_Status"] == "On Time").sum()
    / len(df)
) * 100
print("On-Time Flight Percentage:",
      round(on_time_percentage, 2), "%")

# 21. Delayed Flight Percentage
delayed_percentage = (
    (df["Flight_Status"] == "Delayed").sum()
    / len(df)
) * 100
print("Delayed Flight Percentage:",
      round(delayed_percentage, 2), "%")

# 22. Most Delayed Airline
airline_delay = df.groupby("Airline")["Delay_Minutes"].mean()
most_delayed_airline = airline_delay.idxmax()
print("\nMost Delayed Airline:",
      most_delayed_airline)

# 23. Most Popular Destination
popular_destination = df.groupby(
    "Destination"
)["Passengers"].sum().idxmax()

print("Most Popular Destination:",
      popular_destination)

# 24. Most Used Booking Channel
most_used_booking = df["Booking_Channel"].value_counts().idxmax()
print("Most Used Booking Channel:",
      most_used_booking)

# 25. Best Satisfaction Airline
best_airline = df.groupby(
    "Airline"
)["Passenger_Satisfaction"].mean().idxmax()
print("Highest Satisfaction Airline:",
      best_airline)

# 26. Meaningful Observations
print("\n===== 8 MEANINGFUL OBSERVATIONS =====")

print("1. Total flights analyzed:", df["Flight_ID"].nunique())

print("2. Total passengers:",
      df["Passengers"].sum())

print("3. On-time flight percentage:",
      round(on_time_percentage, 2), "%")

print("4. Delayed flight percentage:",
      round(delayed_percentage, 2), "%")

print("5. Most delayed airline:",
      most_delayed_airline)

print("6. Most popular destination:",
      popular_destination)

print("7. Most used booking channel:",
      most_used_booking)

print("8. Airline with highest passenger satisfaction:",
      best_airline)

print("\n===== ANALYSIS COMPLETED SUCCESSFULLY =====")