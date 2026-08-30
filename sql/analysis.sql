-- E-Commerce Sales Analysis

-- 1. View all orders
SELECT *
FROM orders;

-- 2. Total revenue
SELECT SUM(quantity * price) AS total_revenue
FROM orders;

-- 3. Total number of orders
SELECT COUNT(order_id) AS total_orders
FROM orders;

-- 4. Best-selling products
SELECT product,
       SUM(quantity) AS total_quantity
FROM orders
GROUP BY product
ORDER BY total_quantity DESC;
