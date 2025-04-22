from extract import connect_to_sql_server, extract_sales_data
from load import save_to_excel

def main():
    try:
        # Step 1: Connect to SQL Server
        print("✅ Step 1: Connecting to SQL Server...")
        engine = connect_to_sql_server()

        # Step 2: Extract data using SQL query
        print("✅ Step 2: Extracting sales data from SQL Server...")
        sales_data_df = extract_sales_data(engine)

        # Step 3: Save the extracted data to Excel
        print("✅ Step 3: Saving extracted data to Excel...")
        output_path = r"C:\Users\Data Analyst\Downloads\Sales_Data_Extracted.xlsx"
        save_to_excel(sales_data_df, output_path)

        print("✅ ETL Pipeline for SQL to Excel completed successfully!")

    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()