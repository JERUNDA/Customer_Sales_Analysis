-- revenue per client for the entire period
select 
CUSTOMER_NAME,             -- client name
count(*) as total_orders,  -- total number of orders
sum(SALES) as total_sales  -- total sales amount
from sales_data_sample
group by CUSTOMER_NAME
order by total_sales desc;

-- revenue per client for each year / quarter / month
select
CUSTOMER_NAME,             -- client name
YEAR_ID,                   -- year
QTR_ID,                    -- quarter
MONTH_ID,                  -- month
count(*) as orders_count,  -- number of orders
sum(SALES) as total_sales  -- sales amount
from sales_data_sample
group by CUSTOMER_NAME, YEAR_ID, QTR_ID, MONTH_ID
order by CUSTOMER_NAME, YEAR_ID, QTR_ID, MONTH_ID;

-- revenue by year/quarter/month (aggregated, excluding clients)
select 
YEAR_ID,                   -- year
QTR_ID,                    -- quarter
MONTH_ID,                  -- month
count(*) as orders_count,  -- number of orders
sum(SALES) as total_sales  -- total sales amount
from sales_data_sample
group by YEAR_ID, QTR_ID, MONTH_ID
order by YEAR_ID, QTR_ID, MONTH_ID;