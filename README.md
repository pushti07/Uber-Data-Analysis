# Uber Data Analysis

## Overview
This project analyzes Uber ride data to uncover trends and insights, including trip purposes, time-based distributions, and distance variations. Using Python, pandas, NumPy, Matplotlib, and Seaborn, the dataset is cleaned, preprocessed, and visualized for better understanding.

## Dataset
The dataset used is `UberDataset.csv`, containing information about Uber rides, including:
- Start and end timestamps
- Trip purpose
- Distance traveled
- Ride category (Business or Personal)

## Technologies Used
- **Python**: Core language for data analysis
- **pandas**: Data manipulation and cleaning
- **NumPy**: Numerical operations
- **Matplotlib** & **Seaborn**: Data visualization

## Steps in Analysis
### 1. Data Preprocessing
- Handle missing values in the `PURPOSE` column by replacing them with "NOT".
- Convert `START_DATE` and `END_DATE` columns to datetime format.
- Extract date, time, and categorize time into Morning, Afternoon, Evening, and Night.
- Remove missing values after processing.

### 2. Data Visualization
- **Category Distribution:** Count of Business vs. Personal rides.
- **Trip Purpose Analysis:** Distribution of trip purposes.
- **Time-Based Analysis:**
  - Count of rides across different times of the day.
  - Monthly trend of rides.
  - Weekday ride distribution.
- **Distance Analysis:** Box plots and distribution plots to visualize ride distances.

## Key Insights
- The most frequent trip purpose.
- Peak hours for Uber usage.
- How ride frequency varies by day and month.
- Patterns in travel distances.

## How to Run the Project
1. Install dependencies using:
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```
2. Place `UberDataset.csv` in the working directory.
3. Run the script to generate insights and visualizations.
