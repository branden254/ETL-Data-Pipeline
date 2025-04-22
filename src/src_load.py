def save_to_excel(df, output_path):
    """Save a DataFrame to an Excel file."""
    print(f"✅ Saving data to Excel at {output_path}...")
    df.to_excel(output_path, index=False)
    print(f"✅ Data successfully saved to: {output_path}")