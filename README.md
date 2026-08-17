# ✈️ Flight Operations Data Analysis – Day 10

## 📌 Description

This project is a **Complete Flight Operations Data Analysis** performed using Python and Pandas. The analysis explores flight operations data to understand flight performance, passenger activity, delays, ticket prices, airlines, destinations, weather conditions, booking channels, and passenger satisfaction.

The notebook follows a complete data analysis workflow including data loading, inspection, selection, filtering, sorting, grouping, aggregation, data transformation, and meaningful observations.

## ✨ Analysis Performed

* Loaded the Flight Operations dataset using Pandas
* Inspected the first and last records
* Viewed random samples
* Checked dataset shape and column names
* Checked data types using `dtypes`
* Generated dataset information using `info()`
* Generated descriptive statistics using `describe()`
* Checked missing values
* Converted flight dates using DateTime
* Extracted year, month, and day of the week
* Selected relevant flight data
* Filtered delayed and high-satisfaction flights
* Sorted flights by ticket price and delay
* Performed airline-wise analysis
* Performed weather-wise analysis
* Analyzed travel classes
* Analyzed aircraft performance
* Analyzed origin and destination airports
* Analyzed booking channels
* Analyzed meal preferences
* Calculated total passengers and flights
* Calculated average ticket price
* Calculated average and maximum delays
* Calculated passenger satisfaction
* Calculated on-time and delayed flight percentages
* Identified top airlines, destinations, and booking channels
* Generated 8 meaningful observations

## 🛠️ Technologies Used

* Python 3
* Pandas
* Google Colab
* CSV
* DateTime

## 📂 Project Structure

```text
Flight-Operations-Data-Analysis/
│
├── Day10_Flight_Operations_Dataset.csv
├── Flight_Operations_Analysis_Day10.ipynb
└── README.md
```

## ▶️ How to Run

### 1. Upload the Dataset

Upload the following CSV file to Google Colab:

```text
Day10_Flight_Operations_Dataset.csv
```

### 2. Load the Dataset

```python
import pandas as pd

df = pd.read_csv("Day10_Flight_Operations_Dataset.csv")
```

### 3. Run the Notebook

Run the notebook cells in Google Colab to perform the complete flight operations analysis.

## 📊 Analysis Areas

| Analysis               | Description                                 |
| ---------------------- | ------------------------------------------- |
| Airline                | Flight and passenger performance by airline |
| Flight Status          | On-time and delayed flight analysis         |
| Weather                | Impact of weather on delays                 |
| Travel Class           | Passenger and ticket price analysis         |
| Aircraft               | Flight and delay performance                |
| Origin                 | Passenger traffic by origin                 |
| Destination            | Passenger traffic by destination            |
| Booking Channel        | Flight bookings by channel                  |
| Ticket Price           | Average, highest and lowest prices          |
| Passenger Satisfaction | Satisfaction across airlines and classes    |
| Delay                  | Average, maximum and delayed flights        |

## 🔧 Pandas Operations Used

```python
df.head()
df.tail()
df.sample()
df.shape
df.columns
df.dtypes
df.info()
df.describe()
df.isnull().sum()
df.sort_values()
df.groupby()
df.agg()
df.value_counts()
pd.to_datetime()
```

## 📅 DateTime Operations

Flight dates are converted into DateTime format and additional information is extracted:

```python
df["Flight_Date"] = pd.to_datetime(df["Flight_Date"])

df["Flight_Year"] = df["Flight_Date"].dt.year
df["Flight_Month"] = df["Flight_Date"].dt.month
df["Day_of_Week"] = df["Flight_Date"].dt.day_name()
```

## 🔍 Meaningful Observations

The notebook generates **8 observations** based on the analysis, including:

1. Total number of flights analyzed.
2. Total number of passengers.
3. Percentage of on-time flights.
4. Percentage of delayed flights.
5. Airline with the highest average delay.
6. Most popular destination.
7. Most used booking channel.
8. Airline with the highest passenger satisfaction.

## 🎯 Learning Outcome

This project demonstrates a complete **Pandas data analysis workflow**. It provides practical experience in exploring datasets, filtering and sorting records, performing group-based analysis, calculating statistics, transforming data, and extracting meaningful business insights from flight operations data.
