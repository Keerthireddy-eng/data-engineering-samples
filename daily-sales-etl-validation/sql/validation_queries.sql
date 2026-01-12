-- Check for missing customer IDs
SELECT *
FROM sales
WHERE customer_id IS NULL;

-- Detect negative sales amounts
SELECT *
FROM sales
WHERE amount < 0;

-- Detect duplicate transactions
SELECT transaction_id, COUNT(*)
FROM sales
GROUP BY transaction_id
HAVING COUNT(*) > 1;
