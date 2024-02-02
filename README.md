# helper
Helper code includes random short codes that helps in testing / building other codes

# Read Parquet File

## Overview

This Python script (`read-parquet.py`) demonstrates how to read and display the contents of a Parquet file using the PyArrow and Pandas libraries. It provides an option to display the DataFrame in paginated form for better readability.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Kaify/helper

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
## Run the Script

3. **Place your Parquet file:**
   - Ensure your Parquet file is in the same folder as `read-parquet.py`.

4. **Update the script:**
   - Open `read-parquet.py` in a text editor/IDE of your choice.
   - Locate the `parquet_file_path` variable.
   - Update its value with your Parquet file's name.

5. **Execute the script:**
   ```bash
   python read-parquet.py

## Pagination
   - The script will display rows in a paginated manner.
   - Press Enter to view the next set of rows.
   - Type 'exit' and press Enter to stop the pagination.

