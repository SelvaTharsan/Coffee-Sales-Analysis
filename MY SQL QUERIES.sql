-- Coffee Sales Analysis using SQL

SELECT * 
FROM coffee_sales_dataset;

DESCRIBE coffee_sales_dataset;


-- TOTAL TRANSACTIONS

SELECT COUNT(*) AS total_transactions
FROM coffee_sales_dataset;


-- CHECK MISSING CUSTOMER CARD VALUES

SELECT COUNT(*) AS missing_card_values
FROM coffee_sales_dataset
WHERE card IS NULL;


-- TOTAL REVENUE

SELECT ROUND(SUM(money),2) AS total_revenue
FROM coffee_sales_dataset;


-- MONTHLY SALES KPI - MOM DIFFERENCE AND MOM GROWTH

SELECT 
    DATE_FORMAT(date, '%Y-%m') AS month,
    ROUND(SUM(money),2) AS total_sales,
    ROUND(
        (
            SUM(money) - LAG(SUM(money),1) 
            OVER (ORDER BY DATE_FORMAT(date, '%Y-%m'))
        ) /
        LAG(SUM(money),1)
        OVER (ORDER BY DATE_FORMAT(date, '%Y-%m')) * 100
    ,2) AS mom_growth_percentage
FROM coffee_sales_dataset
GROUP BY DATE_FORMAT(date, '%Y-%m')
ORDER BY month;


-- TOTAL ORDERS

SELECT COUNT(*) AS total_orders
FROM coffee_sales_dataset;


-- MONTHLY ORDERS KPI - MOM DIFFERENCE AND MOM GROWTH

SELECT 
    DATE_FORMAT(date, '%Y-%m') AS month,
    COUNT(*) AS total_orders,
    ROUND(
        (
            COUNT(*) - LAG(COUNT(*),1)
            OVER (ORDER BY DATE_FORMAT(date, '%Y-%m'))
        ) /
        LAG(COUNT(*),1)
        OVER (ORDER BY DATE_FORMAT(date, '%Y-%m')) * 100
    ,2) AS mom_growth_percentage
FROM coffee_sales_dataset
GROUP BY DATE_FORMAT(date, '%Y-%m')
ORDER BY month;


-- DAILY SALES TREND

SELECT 
    date,
    ROUND(SUM(money),2) AS daily_sales
FROM coffee_sales_dataset
GROUP BY date
ORDER BY date;


-- WEEKLY SALES TREND

SELECT 
    WEEK(date) AS week_number,
    ROUND(SUM(money),2) AS weekly_sales
FROM coffee_sales_dataset
GROUP BY WEEK(date)
ORDER BY week_number;


-- SALES BY WEEKDAY / WEEKEND

SELECT 
    CASE
        WHEN DAYOFWEEK(date) IN (1,7) THEN 'Weekend'
        ELSE 'Weekday'
    END AS day_type,
    ROUND(SUM(money),2) AS total_sales
FROM coffee_sales_dataset
GROUP BY 
    CASE
        WHEN DAYOFWEEK(date) IN (1,7) THEN 'Weekend'
        ELSE 'Weekday'
    END;


-- SALES BY WEEKDAY

SELECT 
    DAYNAME(date) AS weekday,
    ROUND(SUM(money),2) AS total_sales
FROM coffee_sales_dataset
GROUP BY weekday
ORDER BY FIELD(
    weekday,
    'Monday','Tuesday','Wednesday',
    'Thursday','Friday','Saturday','Sunday'
);


-- SALES BY HOUR

SELECT 
    HOUR(datetime) AS sales_hour,
    ROUND(SUM(money),2) AS total_sales
FROM coffee_sales_dataset
GROUP BY HOUR(datetime)
ORDER BY sales_hour;


-- NUMBER OF TRANSACTIONS BY DAY

SELECT 
    date,
    COUNT(*) AS transaction_count
FROM coffee_sales_dataset
GROUP BY date
ORDER BY date;


-- COFFEE PRODUCT ANALYSIS

SELECT 
    coffee_name,
    COUNT(*) AS total_orders,
    ROUND(SUM(money),2) AS total_revenue
FROM coffee_sales_dataset
GROUP BY coffee_name
ORDER BY total_revenue DESC;


-- TOP 10 PRODUCTS BY SALES

SELECT 
    coffee_name,
    ROUND(SUM(money),2) AS total_sales
FROM coffee_sales_dataset
GROUP BY coffee_name
ORDER BY total_sales DESC
LIMIT 10;


-- AVERAGE SELLING AMOUNT BY COFFEE TYPE

SELECT 
    coffee_name,
    ROUND(AVG(money),2) AS avg_sales_amount
FROM coffee_sales_dataset
GROUP BY coffee_name
ORDER BY avg_sales_amount DESC;


-- PAYMENT TYPE DISTRIBUTION

SELECT 
    cash_type,
    COUNT(*) AS total_transactions,
    ROUND(SUM(money),2) AS total_revenue
FROM coffee_sales_dataset
GROUP BY cash_type;


-- TOTAL UNIQUE CUSTOMERS

SELECT COUNT(DISTINCT card) AS unique_customers
FROM coffee_sales_dataset
WHERE card IS NOT NULL;


-- TOP 10 CUSTOMERS BY NUMBER OF PURCHASES

SELECT 
    card,
    COUNT(*) AS purchase_count
FROM coffee_sales_dataset
WHERE card IS NOT NULL
GROUP BY card
ORDER BY purchase_count DESC
LIMIT 10;


-- TOP 10 CUSTOMERS BY TOTAL SPENDING

SELECT 
    card,
    ROUND(SUM(money),2) AS total_spent
FROM coffee_sales_dataset
WHERE card IS NOT NULL
GROUP BY card
ORDER BY total_spent DESC
LIMIT 10;


-- PURCHASE HISTORY OF A SPECIFIC CUSTOMER

SELECT 
    card,
    date,
    datetime,
    coffee_name,
    money,
    cash_type
FROM coffee_sales_dataset
WHERE card = 'ANON-0000-0000-0012'
ORDER BY datetime;


-- FAVORITE COFFEE OF EACH CUSTOMER

SELECT 
    card,
    coffee_name,
    COUNT(*) AS purchase_count
FROM coffee_sales_dataset
WHERE card IS NOT NULL
GROUP BY card, coffee_name
ORDER BY card, purchase_count DESC;


-- MONTHLY SPENDING OF A SPECIFIC CUSTOMER

SELECT 
    card,
    DATE_FORMAT(date, '%Y-%m') AS month,
    ROUND(SUM(money),2) AS monthly_spending
FROM coffee_sales_dataset
WHERE card = 'ANON-0000-0000-0012'
GROUP BY card, DATE_FORMAT(date, '%Y-%m')
ORDER BY month;


-- HIGHEST SALES DAY

SELECT 
    date,
    ROUND(SUM(money),2) AS total_sales
FROM coffee_sales_dataset
GROUP BY date
ORDER BY total_sales DESC
LIMIT 1;


-- LOWEST SALES DAY

SELECT 
    date,
    ROUND(SUM(money),2) AS total_sales
FROM coffee_sales_dataset
GROUP BY date
ORDER BY total_sales ASC
LIMIT 1;


-- AVERAGE DAILY SALES

SELECT ROUND(AVG(daily_total),2) AS avg_daily_sales
FROM
(
    SELECT 
        date,
        SUM(money) AS daily_total
    FROM coffee_sales_dataset
    GROUP BY date
) AS daily_summary;


-- REPEAT CUSTOMERS ONLY

SELECT 
    card,
    COUNT(*) AS total_purchases
FROM coffee_sales_dataset
WHERE card IS NOT NULL
GROUP BY card
HAVING COUNT(*) > 1
ORDER BY total_purchases DESC;


-- CUSTOMERS WHO SPENT MORE THAN AVERAGE

SELECT 
    card,
    ROUND(SUM(money),2) AS total_spent
FROM coffee_sales_dataset
WHERE card IS NOT NULL
GROUP BY card
HAVING SUM(money) >
(
    SELECT AVG(customer_total)
    FROM
    (
        SELECT SUM(money) AS customer_total
        FROM coffee_sales_dataset
        WHERE card IS NOT NULL
        GROUP BY card
    ) AS subquery
)
ORDER BY total_spent DESC;
