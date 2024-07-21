import pandas as pd
import csv

# Load the Excel file
excel_file_path = 'eqlist.xlsx'
xls = pd.ExcelFile(excel_file_path)

# Initialize an empty list to store DataFrames
dfs = []

# Iterate through each sheet
for sheet_name in xls.sheet_names:
    # Parse each sheet into a DataFrame
    df = xls.parse(sheet_name)
    # Insert the sheet name as the second column
    df.insert(1, 'SheetName', sheet_name)
    # Append the DataFrame to the list
    dfs.append(df)

# Concatenate all the DataFrames into a single DataFrame
all_sheets_df = pd.concat(dfs, ignore_index=True)

# Save the combined DataFrame to a CSV file with custom quoting
csv_file_path = 'combined_output.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL, escapechar='\\', quotechar='"', delimiter=',')
    # Write header
    writer.writerow(all_sheets_df.columns)
    # Write rows
    for index, row in all_sheets_df.iterrows():
        writer.writerow(row)

print(f"All sheets have been combined and saved to {csv_file_path}")

# Read the CSV file back into a DataFrame
df = pd.read_csv(csv_file_path)

# Function to add quotes around each field as needed
def add_quotes_to_fields(row):
    quoted_row = []
    for value in row:
        if isinstance(value, str):
            if '"' in value:
                value = value.replace('"', '""')  # Double any existing quotes
            quoted_row.append(f'"{value}"')
        else:
            quoted_row.append(str(value))
    return pd.Series(quoted_row)

# Apply the function to each row
df = df.apply(add_quotes_to_fields, axis=1)

# Save the modified DataFrame back to a CSV file
quoted_csv_file_path = 'eqlist.csv'
df.to_csv(quoted_csv_file_path, index=False, header=False, quoting=csv.QUOTE_NONE, escapechar='\\')

print(f"Quotes added to fields as needed and saved to {quoted_csv_file_path}")

