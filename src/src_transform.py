import pandas as pd

def preprocess_data(df):
    """Preprocess the data to add a 'Buying Status' column."""
    df['Buying Status'] = 'Listed'
    return df

def create_cross_join(df):
    """Create a cross join of unique products and customers."""
    product_cols = ['CODE', 'Description_1', 'CATEGORY', 'New_Category', 'Super_Category']
    customer_cols = ['Name', 'ACCOUNT_TYPE']
    unique_products = df[product_cols].drop_duplicates()
    unique_customers = df[customer_cols].drop_duplicates()

    print("✅ Creating cross join of products and customers...")
    full_combos = pd.merge(
        unique_customers.assign(key=1),
        unique_products.assign(key=1),
        on='key'
    ).drop('key', axis=1)
    return full_combos

def find_not_listed(df, full_combos):
    """Identify the 'Not Listed' items."""
    listed_subset = df[['Name', 'CODE']].drop_duplicates()
    merged_check = pd.merge(full_combos, listed_subset, on=['Name', 'CODE'], how='left', indicator=True)
    not_listed = merged_check[merged_check['_merge'] == 'left_only'].drop(columns=['_merge'])
    not_listed['Buying Status'] = 'Not Listed'
    not_listed['CODE_Count'] = 0
    not_listed['Unique_Month_Count'] = 0

    # Match columns
    for col in df.columns:
        if col not in not_listed.columns:
            not_listed[col] = None
    return not_listed

def merge_with_relevance(final_df, master_df):
    """Merge the final DataFrame with relevance data."""
    final_df.columns = final_df.columns.str.strip()
    master_df.columns = master_df.columns.str.strip()

    final_df['CODE'] = final_df['CODE'].astype(str).str.strip().str.upper()
    final_df['ACCOUNT_TYPE'] = final_df['ACCOUNT_TYPE'].astype(str).str.strip().str.upper()
    master_df['CODE'] = master_df['CODE'].astype(str).str.strip().str.upper()
    master_df['ACCOUNT_TYPE'] = master_df['ACCOUNT_TYPE'].astype(str).str.strip().str.upper()

    if 'RELEVANCE' in master_df.columns:
        master_df['RELEVANCE'] = master_df['RELEVANCE'].astype(str).str.strip()

    master_df_deduped = master_df.drop_duplicates(subset=['CODE', 'ACCOUNT_TYPE'])
    final_df = final_df.merge(
        master_df_deduped[['CODE', 'ACCOUNT_TYPE', 'RELEVANCE']],
        on=['CODE', 'ACCOUNT_TYPE'],
        how='left'
    )
    return final_df