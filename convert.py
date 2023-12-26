from bs4 import BeautifulSoup
import csv

# Specify the path to your HTML file
html_file_path = 'filename.html'

# Read HTML content from the file
with open(html_file_path, 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the header row
header_row = soup.find('div', class_='flexTableHeader')

# Extract column names from the header row
columns = [column.get_text(strip=True) for column in header_row.find_all('div', class_='flexHead')]

# Create a CSV file and write the header
csv_filename = 'output.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(columns)

    # Find and process each content row
    content_rows = soup.find_all('div', class_='flexRow network list')
    for row in content_rows:
        # Extract data from each cell in the row
        row_data = [cell.get_text(strip=True) for cell in row.find_all('div', class_='flexCell')]

        # Write the row data to the CSV file
        csv_writer.writerow(row_data)

print(f'CSV file "{csv_filename}" created successfully.')
