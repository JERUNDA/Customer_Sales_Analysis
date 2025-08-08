-- last order of each customer (date and amount)
select distinct on (CUSTOMER_NAME)
CUSTOMER_NAME,  -- customer name
ORDER_DATE,   -- order date
SALES   -- sales amount for the order
from sales_data_sample
order by CUSTOMER_NAME, ORDER_DATE desc;   -- sort by customer and order date (last on top)


-- number of orders for each customer for the period (e.g. for 2024)
select 
CUSTOMER_NAME,  --client name
count(*) as orders_count_2024  -- number of orders in 2024
from sales_data_sample 
where YEAR_ID = 2024 -- filter by 2024
group by CUSTOMER_NAME  -- grouping by clients
order by orders_count_2024 desc;  -- sort by descending number of orders


-- average purchase frequency (average number of days between orders) by customer
with ordered_dates as(
select 
CUSTOMER_NAME, -- client name
ORDER_DATE,  -- current order date
lead(ORDER_DATE) over (partition by CUSTOMER_NAME order by ORDER_DATE) as next_order_date -- next order date for the customer
from sales_data_sample
)
select 
CUSTOMER_NAME, -- client name
avg(next_order_date - ORDER_DATE) as avg_days_between_orders -- average number of days between orders
from ordered_dates
where next_order_date is not null  -- exclude the last order without the next one
group by CUSTOMER_NAME
order by avg_days_between_orders;  -- sort by increasing average frequency


-- customers with missed orders - example logic (requires business rules)
-- for example, customers with a gap between orders greater than 90 days
with ordered_dates as(
select 
CUSTOMER_NAME, -- client name
ORDER_DATE, -- current order date
lead(ORDER_DATE) over (partition by CUSTOMER_NAME order by ORDER_DATE) as next_order_date  -- next order date
from sales_data_sample
)
select CUSTOMER_NAME,  -- client name
ORDER_DATE,  -- current order date
next_order_date,  --next order date
(next_order_date - ORDER_DATE) AS days_diff  -- difference in days between orders
from ordered_dates
where next_order_date is not null
and (next_order_date - ORDER_DATE) > 90  -- filter to make the gap more than 90 days
order by CUSTOMER_NAME;

