SELECT region, SUM(total_value) as total_sales
FROM cleaned
GROUP BY region
ORDER BY total_sales DESC;

SELECT product, SUM(quantity) as total_quantity
FROM cleaned
GROUP BY product
ORDER BY total_quantity DESC;

SELECT DATE_TRUNC('month', order_date) as month, COUNT(*) as order_count
FROM cleaned
GROUP BY 1
ORDER BY 1;

SELECT product, ROUND(AVG(total_value), 2) as avg_order_value
FROM cleaned
GROUP BY product
ORDER BY avg_order_value DESC;
