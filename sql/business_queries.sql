-- Top 5 Products by Revenue

SELECT
    [Product Name],
    SUM(Sales) AS Revenue
FROM sales
GROUP BY [Product Name]
ORDER BY Revenue DESC
LIMIT 5;

-- Monthly Sales Trend

SELECT
    strftime('%m',[Order Date]) AS Month,
    SUM(Sales) AS TotalSales
FROM sales
GROUP BY Month
ORDER BY Month;

-- Most Profitable Category

SELECT
    Category,
    SUM(Profit) AS TotalProfit
FROM sales
GROUP BY Category
ORDER BY TotalProfit DESC;

-- Average Order Value

SELECT AVG(Sales)
FROM sales;

-- Top Customers

SELECT
    [Customer Name],
    SUM(Sales) AS Revenue
FROM sales
GROUP BY [Customer Name]
ORDER BY Revenue DESC
LIMIT 10;

-- Region Performance

SELECT
    Region,
    SUM(Sales),
    SUM(Profit)
FROM sales
GROUP BY Region;