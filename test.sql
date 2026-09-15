CREATE TABLE dbo.Products
(
    ProductID INT,
    ProductName VARCHAR(100)
    ProductDescription VARCHAR(255)
)
WITH
(
    DISTRIBUTION = ROUND_ROBIN
);