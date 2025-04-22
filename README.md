<<<<<<< HEAD
# ETL Data Pipeline for Power BI Dashboard

This project implements an ETL (Extract, Transform, Load) pipeline designed to pull data from a SQL Server database, process and transform the data, and load it into either Excel files or back into the SQL Server for use in a Power BI dashboard.

## Features
- **Data Extraction:**
  - Reads data from an Excel file.
  - Extracts data from a SQL Server database using SQL queries.
  
- **Data Transformation:**
  - Processes and transforms data (e.g., adds columns, cross joins).
  - Merges data with additional relevance metrics.
  
- **Data Loading:**
  - Outputs the transformed data to an Excel file.
  - Inserts the processed data into a SQL Server table.

## Project Structure
```
etl-pipeline/
│
├── src/
│   ├── extract.py           # Handles data extraction (SQL Server and Excel file reading)
│   ├── transform.py         # Handles data transformation and processing
│   ├── load.py              # Handles data loading into the SQL Server database and Excel
│   ├── main.py              # Entry point for the ETL pipeline
│   └── utils.py             # Utility functions used across the project
│
├── config/
│   ├── database_config.py   # Stores database connection configurations
│   └── settings.py          # General settings (file paths, batch size, etc.)
│
├── tests/
│   ├── test_extract.py      # Unit tests for extract module
│   ├── test_transform.py    # Unit tests for transform module
│   ├── test_load.py         # Unit tests for load module
│
├── data/
│   ├── input/               # Input files (e.g., Excel files)
│   └── output/              # Output files (e.g., processed Excel files)
│
├── logs/                    # Logs generated during ETL runs
│
├── requirements.txt         # List of Python dependencies
├── README.md                # Documentation for the project
├── .gitignore               # Files and folders to ignore in version control
└── LICENSE                  # License for the project
```

## How to Run
### Prerequisites
1. **Python Environment:**
   - Requires Python 3.8 or later.
   - Install dependencies from `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

2. **SQL Server Database:**
   - Ensure the database server is accessible.
   - Update `config/database_config.py` with your database credentials.

3. **Excel Files:**
   - Place the required input Excel files in the `data/input` folder.

### Steps to Run
1. Run the ETL pipeline:
   ```bash
   python src/main.py
   ```

2. The processed data will be:
   - Saved into an Excel file in the `data/output` folder.
   - Uploaded to the SQL Server database.

## SQL Query for Extraction
The SQL query used for extracting data from the SQL Server is as follows:
```sql
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
```

## Contributing
Feel free to open issues or submit pull requests for enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
=======
# ETL-Data-Pipeline
This project implements an ETL (Extract, Transform, Load) pipeline designed to pull data from a SQL Server database, process and transform the data, and load it into either Excel files or back into the SQL Server for use in a Power BI dashboard.
>>>>>>> b29330dbaf6385bfecfb9aab648fc223dc82283d
