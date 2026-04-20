# Coffee-Sales-Analysis
## Project Overview  
The Coffee Sales Analysis project was developed using Machine Learning, SQL, and Excel Dashboard to analyze coffee vending machine sales data. It provides insights into sales performance, customer purchasing behavior, product trends, and payment methods. SQL was used for data analysis, Excel for dashboard visualization, and Machine Learning for future sales forecasting.

## Problem Statement
The coffee vending machine business needs to better understand its sales performance and customer behavior. The key areas of concern include:
-	Total sales analysis
-	Daily / weekly / monthly sales trends
-	Product performance analysis
-	Customer purchase behavior
-	Payment method analysis (Card vs Cash)
-	Peak sales hours and weekdays
-	Top customers by spending
-	Future sales forecasting (next day / week / month)
The goal is to use data-driven techniques to improve decision-making, optimize inventory, and increase profitability.

## Tools Used
-	Python (Machine Learning) – Sales forecasting and data preprocessing
-	MySQL – Data storage and querying insights
-	Microsoft Excel – Dashboard creation and data visualization
-	Pandas / NumPy – Data cleaning and transformation
-	Matplotlib / Seaborn – Exploratory data analysis (EDA) charts
-	Scikit-learn – Machine learning models


### Dataset used
-	<a href="https://github.com/SelvaTharsan/Coffee-Sales-Analysis/blob/main/coffee%20sales_Dataset.csv"> Dataset </a>
## Dataset Information
The dataset contains detailed coffee vending machine transaction records with the following columns:
-	date – Transaction date
-	datetime – Exact transaction timestamp
-	cash_type – Payment type (Card / Cash)
-	card – Customer card ID (for card users)
-	money – Transaction amount
-	coffee_name – Purchased coffee product

## Data Cleaning & Preparation
### Excel
- Imported CSV dataset-
- Checked missing values
- Replaced null card values with CASH_CUSTOMER
- Created helper columns:
  - Month
  - Weekday
  - Hour
- Designed dashboard using Pivot Tables & Charts
### Python
- Converted `date` and `datetime` columns to proper datetime format
- Cleaned and handled missing values
- Performed feature engineering to create:
  - Month
  - Day
  - Weekday
  - Hour
- Prepared the dataset for machine learning model training
# SQL
-	Queried revenue, customer spending, sales trends, and product performance
-	Used aggregate functions, grouping, filtering, subqueries, and ordering

## Exploratory Data Analysis (EDA)
The following analyses were performed:
### Sales Trends
-	Daily sales trend
-	Monthly revenue trend
-	Weekly sales pattern
-	Sales by hour
### Product Analysis
-	Top-selling coffee types
-	Revenue by coffee product
-	Popular products based on frequency
### Customer Analysis
-	Unique customers
-	Repeat customers
-	Top customers by spending
-	Favorite products of customers
### Payment Analysis
-	Card vs Cash transaction comparison

## Machine Learning – Sales Forecasting
Built a predictive model to estimate future sales using historical transaction data.
### Predictions Performed:
-	Next day sales
-	Next 7 days sales
-	Next 30 days sales
### Model Used:
-	Linear Regression
### Evaluation Metrics:
-	Mean Squared Error (MSE)
-	R² Score

## Excel Dashboard
An interactive dashboard was created in Excel containing:
### KPI Cards
-	Total Revenue
-	Total Orders
-	Top Coffee Product
-	Top Sales Day
### Charts
-	Monthly Sales Trend
-	Sales by Coffee Type
-	Payment Method Distribution
-	Sales by Weekday
-	Sales by Hour

## SQL Analysis Performed
-	Total revenue
-	Monthly sales summary
-	Daily sales trends
-	Top-selling products
-	Customer purchase history
-	Top customers by spending
-	Sales by weekday and hour

## Key Insights
-	Latte and Americano products generate strong revenue
-	Card payments dominate transactions
-	Certain weekdays show higher sales activity
-	Peak hours indicate customer rush times
-	Repeat customers contribute significantly to revenue
-	Sales forecasting helps in inventory planning

## Recommendations
-	Increase stock for top-selling coffee products
-	Run promotions during low-sales hours
-	Introduce loyalty rewards for repeat customers
-	Optimize staffing during peak hours
-	Use sales forecasting for inventory planning

## Conclusion
The Coffee Sales Analysis Project demonstrates how Excel, SQL, and Machine Learning can be integrated to transform raw transaction data into valuable business insights. The project helps identify trends, improve operations, understand customer behavior, and forecast future revenue effectively.

## Project Output
<h2>Dashboard Preview</h2>
<img width="1366" height="618" alt="Dashboard" src="https://github.com/SelvaTharsan/Coffee-Sales-Analysis/blob/main/Dashboard.jpg" />

<h2>SQL Results</h2>
















