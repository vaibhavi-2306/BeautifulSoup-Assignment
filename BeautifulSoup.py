import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.geeksforgeeks.org/python/python-regex-cheat-sheet/"
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, "html.parser")

tables = soup.find_all("table")
print("Total tables found:", len(tables))

table_number = 1
for table in tables:
    all_rows = []    
    for tr in table.find_all("tr"):
        row_data = [] 
        
        for cell in tr.find_all(["td", "th"]):
            text = cell.get_text(strip=True)  
            row_data.append(text)           
        
        if row_data:
            all_rows.append(row_data)
    
    df = pd.DataFrame(all_rows)
    file_name = "table_" + str(table_number) + ".csv"
    df.to_csv(file_name)
    print("Saved:", file_name)
    
    table_number = table_number + 1
