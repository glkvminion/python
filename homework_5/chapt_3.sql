SELECT supplier_id, MAX(unit_price) AS max_price 
FROM products 
WHERE supplier_id IN (1, 3, 5) 
GROUP BY supplier_id 
ORDER BY supplier_id;