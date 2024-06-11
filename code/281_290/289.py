# 289 - Viết chương trình để phân tích dữ liệu sử dụng Pandas

import pandas as pd

def load_data(file_path):
    """Load data from a CSV file into a Pandas DataFrame."""
    df = pd.read_csv(file_path)
    return df

def display_basic_info(df):
    """Display basic information and descriptive statistics of the DataFrame."""
    print("DataFrame Information:")
    print(df.info())
    print("\nDescriptive Statistics:")
    print(df.describe())

def handle_missing_data(df):
    """Handle missing data by filling them with the mean of each column."""
    # Select only numeric columns
    numeric_df = df.select_dtypes(include=['number'])
    # Calculate mean only for numeric columns
    mean_values = numeric_df.mean()
    # Fill missing values in numeric columns with their mean
    df_filled = df.fillna(mean_values)
    return df_filled

def group_and_aggregate(df, group_by_column, agg_column, agg_func):
    """Group the DataFrame by a column and aggregate using a specified function."""
    grouped_df = df.groupby(group_by_column)[agg_column].agg(agg_func)
    return grouped_df

# Load data
file_path = 'data.csv'  # Đường dẫn tới tệp CSV của bạn
df = load_data(file_path)

# Display basic info and statistics
display_basic_info(df)

# Handle missing data
df_filled = handle_missing_data(df)

# Group and aggregate data
group_by_column = 'Category'  # Cột để nhóm
agg_column = 'Value'         # Cột để tổng hợp
agg_func = 'mean'            # Hàm tổng hợp
grouped_df = group_and_aggregate(df_filled, group_by_column, agg_column, agg_func)

print("\nGrouped and Aggregated Data:")
print(grouped_df)
