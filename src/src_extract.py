import pandas as pd
from sqlalchemy import create_engine, text
import urllib

def connect_to_sql_server():
    """Connect to the SQL Server database."""
    params = urllib.parse.quote_plus(
        "DRIVER={SQL Server};SERVER=HR-ASSISTANT\\SQLEXPRESS;DATABASE=TH_Primary_Sales_Data;UID=sa;PWD=Tropical@50;"
    )
    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")
    return engine

def execute_sql_query(engine, query):
    """Execute a SQL query and return the results as a DataFrame."""
    with engine.connect() as conn:
        result = pd.read_sql_query(text(query), conn)
    return result

def extract_sales_data(engine):
    """Run the SQL query to extract sales data."""
    query = """
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
        (
            SELECT COUNT(DISTINCT FORMAT([TxDate], 'yyyy-MM')) 
            FROM [TH_Primary_Sales_Data].[dbo].[Sales_Data] s 
            WHERE s.[Name] = b.[Name] AND s.[Code] = b.[Code] 
              AND s.[TxDate] BETWEEN '2025-01-01' AND '2025-03-31'
        ) AS Unique_Month_Count
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
    """
    print("✅ Executing SQL query to extract sales data...")
    return execute_sql_query(engine, query)