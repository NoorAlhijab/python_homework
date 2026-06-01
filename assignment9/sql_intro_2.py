# Task 5
# Read Data into a DataFrame
import pandas as pd
import sqlite3

with sqlite3.connect("../db/lesson.db") as conn:
# Create summary from database 
# to find out how many times each product has been ordered, 
# and what was the total price paid by product.

    sql_statement = ("""
    SELECT 
    line_items.line_item_id,
    line_items.quantity,
    line_items.product_id,
    products.product_name,
    products.price
    FROM line_items
    JOIN products
    ON line_items.product_id = products.product_id                        
    """)
    df = pd.read_sql_query(sql_statement, conn)
#print(df.shape)

print(df.head())
#Add a total column to the DataFrame 
df['total'] = df['quantity'] * df['price']
print(df.head())

# Group data by product_id and calculate summary statistics
grouped_product_id =df.groupby('product_id').agg({'line_item_id': 'count', 'total': 'sum', 'product_name': 'first'})
print(grouped_product_id.head())
# Sort dataframe by product name
grouped_product_id = grouped_product_id.sort_values(by='product_name')
print(grouped_product_id.head())

# Export DataFrame to csv file
grouped_product_id.to_csv('order_summary.csv')
