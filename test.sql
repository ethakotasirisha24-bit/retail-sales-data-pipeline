CREATE TABLE dbo.Products
(
    ProductID INT,
    ProductName VARCHAR(100)
)
WITH
(
    DISTRIBUTION = ROUND_ROBIN
);