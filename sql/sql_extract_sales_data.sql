WITH Base AS (
    SELECT 
        [Name], 
        [Code], 
        [Description_1], 
        [CATEGORY], 
        [New_Category], 
        [Super_Category], 
        [ACCOUNT_TYPE], 
        FORMAT([TxDate], 'yyyy-MM') AS Sales_Month
    FROM [TH_Primary_Sales_Data].[dbo].[Sales_Data]
    WHERE [TxDate] BETWEEN '2025-01-01' AND '2025-03-31'
)

SELECT 
    b.[Name], 
    b.[Code], 
    b.[Description_1], 
    b.[CATEGORY], 
    b.[New_Category], 
    b.[Super_Category], 
    b.[ACCOUNT_TYPE], 
    COUNT(*) OVER (PARTITION BY b.[Name], b.[Code]) AS Code_Count,
    (SELECT COUNT(DISTINCT FORMAT([TxDate], 'yyyy-MM')) 
     FROM [TH_Primary_Sales_Data].[dbo].[Sales_Data] s 
     WHERE s.[Name] = b.[Name] AND s.[Code] = b.[Code] 
       AND s.[TxDate] BETWEEN '2025-01-01' AND '2025-03-31') AS Unique_Month_Count
FROM Base b
GROUP BY 
    b.[Name], 
    b.[Code], 
    b.[Description_1], 
    b.[CATEGORY], 
    b.[New_Category], 
    b.[Super_Category], 
    b.[ACCOUNT_TYPE]
ORDER BY 
    b.[Name], 
    b.[Code];