-- ranking of clients by total income (entire period)
select CUSTOMER_NAME,   -- client name
sum(SALES) as total_sales,  -- total sales amount for the entire period
rank () over(order by sum(SALES) desc) as sales_rank  -- rank by total sales, highest first
from sales_data_sample
group by CUSTOMER_NAME
order by sales_rank;

-- ranking of customers by revenue in each year
select 
CUSTOMER_NAME,   -- client name
YEAR_ID,   -- year of the sales
sum(SALES) as total_sales,    -- total sales amount per year
rank () over (partition by YEAR_ID order by sum(SALES) desc) as sales_rank  -- rank within each year
from sales_data_sample
group by CUSTOMER_NAME, YEAR_ID
order by YEAR_ID, sales_rank;

-- ranking of customers based on the number of orders (frequency)
select CUSTOMER_NAME,    -- client name
count(*) as orders_count,  -- total number of orders
rank() over (order by count(*) desc) as order_rank   -- rank by number of orders, highest first
from sales_data_sample
group by CUSTOMER_NAME
order by order_rank;