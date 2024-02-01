import pyarrow.parquet as pq

def display_dataframe(df, start_row, end_row):
    print(df.iloc[start_row:end_row])

print("Starting Execution")
# Download /copy your parquet file in the same folder. Specify the path/name of your Parquet file
parquet_file_path = '<your parquet file name with .parquet extension>'

# Read the Parquet file into a PyArrow Table
table = pq.read_table(parquet_file_path)

# Convert the Table to a Pandas DataFrame
df = table.to_pandas()

# Set the number of rows to display at a time
rows_per_page = 50

# Display the DataFrame with pagination
start_row = 0
while start_row < len(df):
    end_row = start_row + rows_per_page
    display_dataframe(df, start_row, end_row)
    
    user_input = input("Press Enter to view the next set of rows, or type 'exit' to stop: ")
    if user_input.lower() == 'exit':
        break
    
    start_row = end_row
