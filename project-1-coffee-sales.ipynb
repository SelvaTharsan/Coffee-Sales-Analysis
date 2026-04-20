# COFFEE SALES ANALYSIS PROJECT

# IMPORT LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

import warnings
warnings.filterwarnings('ignore')


# LOAD DATA
data = pd.read_csv("/kaggle/input/datasets/tharsthanu/coffee-sales/index.csv")

print("First 5 rows:")
print(data.head())


# CONVERT DATE COLUMNS
data['date'] = pd.to_datetime(data['date'])
data['datetime'] = pd.to_datetime(data['datetime'])


# CHECK MISSING VALUES
print("\nMissing values before handling:")
print(data.isnull().sum())


# HANDLE MISSING VALUES
# Missing card values are treated as cash transactions
data['card'] = data['card'].fillna('cash')

print("\nMissing values after handling:")
print(data.isnull().sum())


# FEATURE ENGINEERING
data['month'] = data['date'].dt.to_period('M').astype(str)
data['day_of_month'] = data['date'].dt.day
data['weekday'] = data['date'].dt.day_name()
data['weekday_num'] = data['date'].dt.dayofweek   # Monday = 0
data['hour'] = data['datetime'].dt.hour
data['week'] = data['date'].dt.isocalendar().week.astype(int)
data['is_weekend'] = (data['weekday_num'] >= 5).astype(int)

print("\nData after feature engineering:")
print(data.head())


# DATA OVERVIEW
print(f"\nShape of dataset: {data.shape}")
print(f"Date range: {data['date'].min()} to {data['date'].max()}")

print("\nCoffee types count:")
print(data['coffee_name'].value_counts())

print("\nPayment type count:")
print(data['cash_type'].value_counts())

print("\nSummary statistics:")
print(data[['money', 'day_of_month', 'hour', 'week']].describe())


# DAILY TOTAL SALES
daily_sales = data.groupby('date')['money'].sum().reset_index()

plt.figure(figsize=(12, 5))
plt.plot(daily_sales['date'], daily_sales['money'], linewidth=1)
plt.title("Daily Sales Trend (March - July 2024)")
plt.xlabel("Date")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# MONTHLY TOTAL SALES
monthly_sales = data.groupby('month')['money'].sum().reset_index()

plt.figure(figsize=(10, 5))
sns.barplot(x='month', y='money', data=monthly_sales, color='steelblue')
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# SALES BY WEEKDAY
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekly_sales = data.groupby('weekday')['money'].sum().reindex(weekday_order).reset_index()

plt.figure(figsize=(10, 5))
sns.barplot(x='weekday', y='money', data=weekly_sales, palette='viridis')
plt.title("Sales by Weekday")
plt.xlabel("Weekday")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# SALES BY HOUR
hourly_sales = data.groupby('hour')['money'].sum().reset_index()

plt.figure(figsize=(12, 5))
sns.barplot(x='hour', y='money', data=hourly_sales, palette='coolwarm')
plt.title("Sales by Hour of Day")
plt.xlabel("Hour (24h)")
plt.ylabel("Total Sales ($)")
plt.tight_layout()
plt.show()


# PRODUCT POPULARITY
plt.figure(figsize=(10, 6))
product_counts = data['coffee_name'].value_counts()
sns.barplot(y=product_counts.index, x=product_counts.values, palette='Set2')
plt.title("Number of Sales by Coffee Type")
plt.xlabel("Number of Transactions")
plt.ylabel("Coffee Name")
plt.tight_layout()
plt.show()


# REVENUE BY PRODUCT
coffee_revenue = data.groupby('coffee_name')['money'].sum().sort_values(ascending=False).reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='money', y='coffee_name', data=coffee_revenue, palette='Set3')
plt.title("Revenue by Coffee Type")
plt.xlabel("Revenue ($)")
plt.ylabel("Coffee Name")
plt.tight_layout()
plt.show()


# PAYMENT METHOD DISTRIBUTION
payment_counts = data['cash_type'].value_counts(normalize=True) * 100
print("\nPayment method percentage:")
print(payment_counts)

# SALES PREDICTION PART

# AGGREGATE DAILY SALES
daily_sales = data.groupby('date').agg({
    'money': 'sum',
    'datetime': 'count'
}).rename(columns={'datetime': 'transaction_count'}).reset_index()


# CREATE TIME-BASED FEATURES
daily_sales['day_of_week'] = daily_sales['date'].dt.dayofweek
daily_sales['month'] = daily_sales['date'].dt.month
daily_sales['day_of_month'] = daily_sales['date'].dt.day
daily_sales['week_of_year'] = daily_sales['date'].dt.isocalendar().week.astype(int)


# CREATE LAG FEATURES
daily_sales['prev_day_sales'] = daily_sales['money'].shift(1)
daily_sales['prev_2day_sales'] = daily_sales['money'].shift(2)
daily_sales['prev_3day_sales'] = daily_sales['money'].shift(3)
daily_sales['prev_week_sales'] = daily_sales['money'].shift(7)


# CREATE ROLLING AVERAGES
daily_sales['rolling_3day_avg'] = daily_sales['money'].rolling(window=3, min_periods=1).mean()
daily_sales['rolling_7day_avg'] = daily_sales['money'].rolling(window=7, min_periods=1).mean()


# DROP NaN VALUES
daily_sales_clean = daily_sales.dropna().reset_index(drop=True)

print(f"\nDaily sales data shape: {daily_sales_clean.shape}")
print(f"Date range for modeling: {daily_sales_clean['date'].min()} to {daily_sales_clean['date'].max()}")


# SELECT FEATURES
feature_columns = [
    'day_of_week', 'month', 'day_of_month', 'week_of_year',
    'prev_day_sales', 'prev_2day_sales', 'prev_3day_sales', 'prev_week_sales',
    'rolling_3day_avg', 'rolling_7day_avg', 'transaction_count'
]

X = daily_sales_clean[feature_columns]
y = daily_sales_clean['money']


# CHRONOLOGICAL TRAIN-TEST SPLIT
split_idx = int(len(daily_sales_clean) * 0.8)

X_train, X_test = X[:split_idx], X[split_idx:]
y_train, y_test = y[:split_idx], y[split_idx:]

print(f"\nTraining set: {X_train.shape[0]} days ({daily_sales_clean['date'].iloc[split_idx-1]})")
print(f"Test set: {X_test.shape[0]} days ({daily_sales_clean['date'].iloc[split_idx]} to {daily_sales_clean['date'].iloc[-1]})")


# LINEAR REGRESSION MODEL
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
y_pred_lr = lr_model.predict(X_test)

mse_lr = mean_squared_error(y_test, y_pred_lr)
rmse_lr = np.sqrt(mse_lr)
mae_lr = mean_absolute_error(y_test, y_pred_lr)
r2_lr = r2_score(y_test, y_pred_lr)

print("\nLinear Regression Performance:")
print(f"Mean Squared Error: {mse_lr:.2f}")
print(f"Root Mean Squared Error: {rmse_lr:.2f}")
print(f"Mean Absolute Error: {mae_lr:.2f}")
print(f"R² Score: {r2_lr:.4f}")


# RANDOM FOREST MODEL
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)

mse_rf = mean_squared_error(y_test, y_pred_rf)
rmse_rf = np.sqrt(mse_rf)
mae_rf = mean_absolute_error(y_test, y_pred_rf)
r2_rf = r2_score(y_test, y_pred_rf)

print("\nRandom Forest Performance:")
print(f"Mean Squared Error: {mse_rf:.2f}")
print(f"Root Mean Squared Error: {rmse_rf:.2f}")
print(f"Mean Absolute Error: {mae_rf:.2f}")
print(f"R² Score: {r2_rf:.4f}")


# FEATURE IMPORTANCE
feature_importance = pd.DataFrame({
    'feature': feature_columns,
    'importance': rf_model.feature_importances_
}).sort_values('importance', ascending=False)

print("\nFeature Importance (Random Forest):")
print(feature_importance)


# ACTUAL VS PREDICTED SALES
plt.figure(figsize=(14, 6))
test_dates = daily_sales_clean['date'].iloc[split_idx:]

plt.plot(test_dates, y_test.values, label='Actual Sales', marker='o', linewidth=2, markersize=4)
plt.plot(test_dates, y_pred_rf, label='Random Forest Predictions', marker='s', linewidth=2, markersize=4, alpha=0.7)
plt.plot(test_dates, y_pred_lr, label='Linear Regression Predictions', marker='^', linewidth=2, markersize=4, alpha=0.7)

plt.title('Actual vs Predicted Sales (Test Set)')
plt.xlabel('Date')
plt.ylabel('Sales ($)')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# FUTURE PREDICTIONS

# PREPARE LAST ROW
last_row = daily_sales_clean.iloc[-1:].copy()
last_date = daily_sales_clean['date'].max()


# FUNCTION FOR FUTURE PREDICTION
def predict_future_days(model, last_data, feature_cols, last_date, n_days=7):
    predictions = []
    current_data = last_data.copy()
    current_date = last_date

    for i in range(n_days):
        current_date += pd.Timedelta(days=1)

        current_data['day_of_week'] = current_date.dayofweek
        current_data['month'] = current_date.month
        current_data['day_of_month'] = current_date.day
        current_data['week_of_year'] = int(current_date.isocalendar().week)

        pred = model.predict(current_data[feature_cols])[0]
        predictions.append(pred)

        if i < n_days - 1:
            current_data['prev_day_sales'] = pred
            current_data['prev_2day_sales'] = pred
            current_data['prev_3day_sales'] = pred
            current_data['prev_week_sales'] = pred
            current_data['rolling_3day_avg'] = pred
            current_data['rolling_7day_avg'] = pred

    return predictions


# NEXT 7 DAYS PREDICTION
next_7_days = predict_future_days(rf_model, last_row, feature_columns, last_date, 7)

future_dates = [last_date + pd.Timedelta(days=i+1) for i in range(7)]
future_df = pd.DataFrame({
    'date': future_dates,
    'predicted_sales': next_7_days
})

print("\nNext 7 Days Sales Prediction (Random Forest):")
print(future_df.to_string(index=False))
print(f"\nTotal predicted sales for next week: ${sum(next_7_days):.2f}")


# NEXT 30 DAYS PREDICTION
next_30_days = predict_future_days(rf_model, last_row, feature_columns, last_date, 30)
future_30_dates = [last_date + pd.Timedelta(days=i+1) for i in range(30)]

plt.figure(figsize=(14, 6))
plt.plot(future_30_dates, next_30_days, marker='o', linewidth=2, markersize=4)
plt.title('Next 30 Days Sales Prediction (Random Forest)')
plt.xlabel('Date')
plt.ylabel('Predicted Sales ($)')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# CUSTOMER PURCHASE ANALYSIS

# CUSTOMER DATA
customer_data = data[data['card'] != 'cash'].copy()

print(f"\nNumber of unique customers: {customer_data['card'].nunique()}")


# TOP CUSTOMERS BY PURCHASE COUNT
top_customers_count = customer_data['card'].value_counts().head(10).reset_index()
top_customers_count.columns = ['customer_id', 'purchase_count']

print("\nTop 10 customers by purchase count:")
print(top_customers_count.to_string(index=False))

plt.figure(figsize=(10, 6))
sns.barplot(x='purchase_count', y='customer_id', data=top_customers_count, palette='Blues_d')
plt.title("Top 10 Customers by Number of Purchases")
plt.xlabel("Purchase Count")
plt.ylabel("Customer ID")
plt.tight_layout()
plt.show()


# TOP CUSTOMERS BY TOTAL SPENDING
top_customers_spending = customer_data.groupby('card')['money'].sum().sort_values(ascending=False).head(10).reset_index()
top_customers_spending.columns = ['customer_id', 'total_spending']

print("\nTop 10 customers by total spending:")
print(top_customers_spending.to_string(index=False))

plt.figure(figsize=(10, 6))
sns.barplot(x='total_spending', y='customer_id', data=top_customers_spending, palette='Greens_d')
plt.title("Top 10 Customers by Total Spending")
plt.xlabel("Total Spending ($)")
plt.ylabel("Customer ID")
plt.tight_layout()
plt.show()


# SPECIFIC CUSTOMER ANALYSIS
specific_customer = top_customers_count['customer_id'].iloc[0]
specific_customer_data = customer_data[customer_data['card'] == specific_customer]

print(f"\nCUSTOMER DETAILS: {specific_customer}")
print(f"\nTotal purchases: {len(specific_customer_data)}")
print(f"Total spending: ${specific_customer_data['money'].sum():.2f}")
print(f"Average spending per purchase: ${specific_customer_data['money'].mean():.2f}")
print(f"Favorite payment method: {specific_customer_data['cash_type'].mode().iloc[0]}")

print("\nPurchase history (last 10 transactions):")
print(specific_customer_data[['date', 'datetime', 'coffee_name', 'money']].tail(10).to_string(index=False))


# FAVORITE PRODUCTS OF SPECIFIC CUSTOMER
customer_favorites = specific_customer_data['coffee_name'].value_counts().reset_index()
customer_favorites.columns = ['coffee_name', 'count']

print("\nFavorite products:")
print(customer_favorites.to_string(index=False))

plt.figure(figsize=(10, 6))
sns.barplot(x='count', y='coffee_name', data=customer_favorites, palette='Oranges_d')
plt.title(f"Favorite Products of Customer {specific_customer}")
plt.xlabel("Purchase Count")
plt.ylabel("Coffee Name")
plt.tight_layout()
plt.show()


# FINAL INSIGHTS & RECOMMENDATIONS
print("\nFINAL INSIGHTS & RECOMMENDATIONS")

print(f"\nOVERALL METRICS:")
print(f"   • Total Revenue: ${data['money'].sum():.2f}")
print(f"   • Total Transactions: {len(data)}")
print(f"   • Average Transaction Value: ${data['money'].mean():.2f}")
print(f"   • Date Range: {data['date'].min().date()} to {data['date'].max().date()}")

print(f"\nTOP PERFORMING PRODUCTS:")
top_products = data['coffee_name'].value_counts().head(3)
for product, count in top_products.items():
    revenue = data[data['coffee_name'] == product]['money'].sum()
    print(f"   • {product}: {count} sales, ${revenue:.2f} revenue")

print(f"\nSALES PATTERNS:")
print(f"   • Best Day: {weekly_sales.loc[weekly_sales['money'].idxmax(), 'weekday']}")
print(f"   • Best Hour: {hourly_sales.loc[hourly_sales['money'].idxmax(), 'hour']}:00")
print(f"   • Weekend vs Weekday: Weekend sales represent {(data[data['is_weekend'] == 1]['money'].sum() / data['money'].sum() * 100):.1f}% of total")

print(f"\nCUSTOMER INSIGHTS:")
print(f"   • Unique Customers: {customer_data['card'].nunique()}")
print(f"   • Top Customer: {specific_customer} with {len(specific_customer_data)} purchases")
repeat_customers = customer_data.groupby('card').size()
print(f"   • Repeat Customers: {(repeat_customers > 1).sum()}")

print(f"\nPAYMENT PREFERENCES:")
if 'card' in payment_counts.index:
    print(f"   • Card: {payment_counts['card']:.1f}%")
if 'cash' in payment_counts.index:
    print(f"   • Cash: {payment_counts['cash']:.1f}%")
