# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reading CSV with code encoding
df = pd.read_csv(r'C:\temp\sales_data_sample.csv', sep=',', encoding='cp1251')

# View first lines
print(df.head())
   ORDER_NUMBER  QUANTITY_ORDERED  PRICE_EACH  ...  CONTACT_LAST_NAME  CONTACT_FIRST_NAME DEAL_SIZE
0         10107                30       95.70  ...                 Yu                Kwai     Small
1         10121                34       81.35  ...            Henriot                Paul     Small
2         10134                41       94.74  ...           Da Cunha              Daniel    Medium
3         10145                45       83.26  ...              Young               Julie    Medium
4         10159                49      100.00  ...              Brown               Julie    Medium

[5 rows x 25 columns]

# Check the number of gaps in each column
df.isnull().sum()
ORDER_NUMBER             0
QUANTITY_ORDERED         0
PRICE_EACH               0
ORDER_LINE_NUMBER        0
SALES                    0
ORDER_DATE               0
STATUS                   0
QTR_ID                   0
MONTH_ID                 0
YEAR_ID                  0
PRODUCT_LINE             0
MSRP                     0
PRODUCT_CODE             0
CUSTOMER_NAME            0
PHONE                    0
ADDRESS_LINE1            0
ADDRESS_LINE2         2521
CITY                     0
STATE                 1486
POSTAL_CODE             76
COUNTRY                  0
TERRITORY             1074
CONTACT_LAST_NAME        0
CONTACT_FIRST_NAME       0
DEAL_SIZE                0
dtype: int64

# Fill in the blanks: text fields - 'Unknown', numeric - 0
obj_col = df.select_dtypes(include = 'object').columns
df[obj_col] = df[obj_col].fillna('Unknown')

num_col = df.select_dtypes(include = 'number').columns
df[num_col] = df[num_col].fillna(0)

# Control of absence of passes
>>> df.isnull().sum()
ORDER_NUMBER          0
QUANTITY_ORDERED      0
PRICE_EACH            0
ORDER_LINE_NUMBER     0
SALES                 0
ORDER_DATE            0
STATUS                0
QTR_ID                0
MONTH_ID              0
YEAR_ID               0
PRODUCT_LINE          0
MSRP                  0
PRODUCT_CODE          0
CUSTOMER_NAME         0
PHONE                 0
ADDRESS_LINE1         0
ADDRESS_LINE2         0
CITY                  0
STATE                 0
POSTAL_CODE           0
COUNTRY               0
TERRITORY             0
CONTACT_LAST_NAME     0
CONTACT_FIRST_NAME    0
DEAL_SIZE             0
dtype: int64

# Information about data types
df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 2823 entries, 0 to 2822
Data columns (total 25 columns):
 #   Column              Non-Null Count  Dtype
---  ------              --------------  -----
 0   ORDER_NUMBER        2823 non-null   int64
 1   QUANTITY_ORDERED    2823 non-null   int64
 2   PRICE_EACH          2823 non-null   float64
 3   ORDER_LINE_NUMBER   2823 non-null   int64
 4   SALES               2823 non-null   float64
 5   ORDER_DATE          2823 non-null   object
 6   STATUS              2823 non-null   object
 7   QTR_ID              2823 non-null   int64
 8   MONTH_ID            2823 non-null   int64
 9   YEAR_ID             2823 non-null   int64
 10  PRODUCT_LINE        2823 non-null   object
 11  MSRP                2823 non-null   int64
 12  PRODUCT_CODE        2823 non-null   object
 13  CUSTOMER_NAME       2823 non-null   object
 14  PHONE               2823 non-null   object
 15  ADDRESS_LINE1       2823 non-null   object
 16  ADDRESS_LINE2       2823 non-null   object
 17  CITY                2823 non-null   object
 18  STATE               2823 non-null   object
 19  POSTAL_CODE         2823 non-null   object
 20  COUNTRY             2823 non-null   object
 21  TERRITORY           2823 non-null   object
 22  CONTACT_LAST_NAME   2823 non-null   object
 23  CONTACT_FIRST_NAME  2823 non-null   object
 24  DEAL_SIZE           2823 non-null   object
dtypes: float64(2), int64(7), object(16)
memory usage: 551.5+ KB

# Convert ORDER_DATE to datetime format
df['ORDER_DATE'] = pd.to_datetime(df['ORDER_DATE'], errors='coerce', dayfirst=False)

# Create a column with the total amount of sales by item
df['Total_Sales'] = df['QUANTITY_ORDERED'] * df['PRICE_EACH']
print(df['Total_Sales'].head())
0    2871.00
1    2765.90
2    3884.34
3    3746.70
4    4900.00
Name: Total_Sales, dtype: float64

# Add a column with the order month for analysis by month
df['ORDER_MONTH'] = df['ORDER_DATE'].dt.to_period('M')

# Total sales for each order
total_orders = df.groupby('ORDER_NUMBER')['Total_Sales'].sum()

# Average Order Value (AOV)
AOV = total_orders.mean()
print(AOV)
27006.145895765476

# Average sales by product category
category_avg_sales = df.groupby('PRODUCT_LINE')['Total_Sales'].mean()
print(category_avg_sales)
PRODUCT_LINE
Classic Cars        3069.851499
Motorcycles         2933.795438
Planes              2869.092190
Ships               2897.181197
Trains              2646.808571
Trucks and Buses    3147.359402
Vintage Cars        2708.751318
Name: Total_Sales, dtype: float64

# Number of unique orders per customer
orders_per_customer = df.groupby('CUSTOMER_NAME')['ORDER_NUMBER'].nunique()
print(orders_per_customer)
CUSTOMER_NAME
AV Stores, Co.                 3
Alpha Cognac                   3
Amica Models & Co.             2
Anna's Decorations, Ltd        4
Atelier graphique              3
                              ..
Vida Sport, Ltd                2
Vitachrome Inc.                3
Volvo Model Replicas, Co       4
West Coast Collectables Co.    2
giftsbymail.co.uk              2
Name: ORDER_NUMBER, Length: 92, dtype: int64

# Determine the top 5 clients by total revenue
top5_customers = df.groupby('CUSTOMER_NAME')['Total_Sales'].sum().sort_values(ascending = False).head(5)
print(top5_customers)
CUSTOMER_NAME
Euro Shopping Channel           766195.05
Mini Gifts Distributors Ltd.    530587.19
Australian Collectors, Co.      164575.87
La Rochelle Gifts               153909.82
Muscle Machine Inc              151782.04
Name: Total_Sales, dtype: float64

# Revenue by month
monthly_revenue = df.groupby('ORDER_MONTH')['Total_Sales'].sum()
print(monthly_revenue)
ORDER_MONTH
2003-01     82971.01
2003-02     73422.63
2003-03     77680.11
2003-04    117377.82
2003-05    105078.03
2003-06     48221.02
2003-07     57046.22
2003-08     49300.25
2003-09    110452.07
2003-10    272146.66
2003-11    452146.64
2004-01    155528.74
2004-02    195544.22
2004-03     70569.14
2004-04     76881.82
2004-05     44464.20
2004-06    197495.12
2004-07    197593.06
2004-08    291858.94
2004-09     87897.44
2004-10    400510.28
2004-11    501967.46
2004-12     58878.58
2005-01    170430.89
2005-02    157148.51
2005-03    121234.67
2005-04     97073.48
2005-05    191579.66
Freq: M, Name: Total_Sales, dtype: float64

# Recency (time since last order)
last_order_date = df.groupby('CUSTOMER_NAME')['ORDER_DATE'].max()
today = pd.Timestamp('today')
recency = (today - last_order_date).dt.days
print(recency.head())
CUSTOMER_NAME
AV Stores, Co.             7569.0
Alpha Cognac               7438.0
Amica Models & Co.         7661.0
Anna's Decorations, Ltd    7505.0
Atelier graphique          7561.0
Name: ORDER_DATE, dtype: float64

# Summarize sales by product category
category_sales = df.groupby('PRODUCT_LINE')['Total_Sales'].sum().reset_index()

# Create a 12x6 inch chart shape
plt.figure(figsize=(12, 6))

# Build a bar chart of income by product category
sns.barplot(data = category_sales, x = 'PRODUCT_LINE', y = 'Total_Sales', palette = 'viridis')

# Add title and axis labels
plt.title('Revenue by product category')
plt.xlabel('Product category')
plt.ylabel('Revenue amount')

# Rotate category labels on the X axis for better readability
plt.xticks(rotation = 45)

# Make indents so that the elements of the graph do not overlap each other
plt.tight_layout()

# Display the graph
plt.show()

# Analyze sales by clients (sum up for each client)
customers_sales = df.groupby('CUSTOMER_NAME')['Total_Sales'].sum().reset_index()

# Create a figure for the boxplot with a larger size for readability
plt.figure(figsize=(20,8))

# Build a boxplot to distribute revenue across customers
sns.boxplot(data=customers_sales, x='CUSTOMER_NAME', y='Total_Sales', palette='Set3')

# Rotate the client signatures on the X axis by 90 degrees and reduce the font size so that they all fit
plt.xticks(rotation=90, fontsize=8)

# Make indents for a dense and neat display
plt.tight_layout()

# Display the graph
plt.show()

# Create a pivot table with the sales amount by year and month
pivot = df.pivot_table(index = 'YEAR_ID', values = 'SALES', columns = 'MONTH_ID', aggfunc = 'sum', fill_value = 0)

# Convert values to thousands for ease of display
pivot_thousands = pivot / 1000

# Visualization of sales seasonality in the form of a heat map
plt.figure(figsize=(12, 6))
sns.heatmap(pivot_thousands, annot=True, fmt='.1f', cmap='YlGnBu')
plt.title('Revenue seasonality (thousands of $)')
plt.xlabel('Month')
plt.ylabel('Year')
plt.show()

# Create a column with the month from the order date (only year and month, date from the beginning of the month)
df['ORDER_MONTH'] = df['ORDER_DATE'].dt.to_period('M').dt.to_timestamp()

# Group sales by month
monthly_sales = df.groupby('ORDER_MONTH')['SALES'].sum().reset_index()

# Visualize sales trend by month using line chart
plt.figure(figsize=(12, 6))
sns.lineplot(data = monthly_sales, x = 'ORDER_MONTH', y = 'SALES', marker = 'o')
plt.title('Sales trend by month')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.grid(True)
plt.show()

# Total sales by country
country_sales = df.groupby('COUNTRY')['SALES'].sum()

# Visualization of sales shares by country in the form of a pie chart
plt.figure(figsize=(10, 8))
plt.pie(country_sales, labels=country_sales.index, autopct='%.1f%%')
plt.title('Sales share by country')
plt.show()
