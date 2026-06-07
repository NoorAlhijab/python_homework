# Task 1

import sqlite3
conn = sqlite3.connect("../db/lesson.db")
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()


# Execute the query
query = """
SELECT 
orders.order_id,
SUM(products.price * line_items.quantity) AS total_price
FROM orders 
JOIN line_items ON orders.order_id = line_items.order_id
JOIN products ON line_items.product_id = products.product_id
GROUP BY orders.order_id
ORDER BY orders.order_id
LIMIT 5;

"""
cursor.execute(query)
records = cursor.fetchall()
for record in records:
    print(record)



# Task 2

query = """
SELECT 
customers.customer_name,
AVG(total_price) AS avg_total_price
FROM (
SELECT 
orders.order_id,
orders.customer_id AS customer_id_b,
SUM(products.price * line_items.quantity) AS total_price
FROM orders
JOIN line_items ON orders.order_id = line_items.order_id
JOIN products ON line_items.product_id = products.product_id
GROUP BY orders.order_id, orders.customer_id
) AS total_orders
LEFT JOIN customers ON customers.customer_id = total_orders.customer_id_b
GROUP BY customers.customer_id;
"""
cursor.execute(query)
records = cursor.fetchall()
for record in records:
    print(record)

# Task 3
# Retrieve the customer_id
cursor.execute("""
SELECT 
customer_id
FROM customers
WHERE customer_name = 'Perez and Sons' 
""")
customer_id = cursor.fetchone()[0]

# Retrieve the employee_id
cursor.execute("""
SELECT 
employee_id
FROM employees
WHERE first_name = 'Miranda' AND last_name = 'Harris'
""")
employee_id = cursor.fetchone()[0]
# Retrieve the product_id with the 5 least expensive products
cursor.execute(""" 
SELECT 
product_id
FROM products
ORDER BY price ASC
LIMIT 5;
""")
product_ids = cursor.fetchall()

# Transaction
try:
    cursor.execute("""
    INSERT INTO orders (customer_id, employee_id) 
    VALUES (?, ?) RETURNING order_id; 
    """, (customer_id, employee_id))
    order_id = cursor.fetchone()[0]

    # Create the 5 line_item records comprising the order
    for (product_id,) in (product_ids):
        cursor.execute("""
    INSERT INTO line_items (order_id, product_id, quantity)
    VALUES (?, ?, ?);
    """, (order_id, product_id, 10))

    conn.commit()  
except Exception as e:
    conn.rollback()  
    print("Error:", e)

# Using a SELECT with a JOIN, print out the list of line_item_ids 
# for the order along with the quantity and product name for each
cursor.execute("""
SELECT                
line_items.line_item_id,
line_items.quantity,
products.product_name
FROM line_items
JOIN products ON line_items.product_id = products.product_id
WHERE line_items.order_id = ?;
""", (order_id,))
records = cursor.fetchall()
for record in records:
    print(record)

# Task 4
query = """
SELECT
employees.employee_id,
employees.first_name,
employees.last_name,
COUNT(orders.order_id) AS order_count
FROM employees
JOIN orders ON employees.employee_id = orders.employee_id
GROUP BY employees.employee_id, employees.first_name, employees.last_name
HAVING COUNT(orders.order_id) > 5; 
"""
cursor.execute(query)
records = cursor.fetchall()
for record in records:
    print(record)
conn.close()