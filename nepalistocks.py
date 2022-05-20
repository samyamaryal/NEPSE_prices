# This program makes use of the 'find_all' module within BS4 and 'for' loops to fetch data.
from bs4 import BeautifulSoup
import requests

url = 'http://www.nepalstock.com/todaysprice'
# Get the webpage using requests
webpage = requests.get(url)
# Parse the webpage
parsed = BeautifulSoup(webpage.text, "html.parser")

# find all elements within the 'table' tag
body = parsed.find_all('table')

# iterate through every element with 'tr' tag within the 'table' tag
for b in body:
    rows = b.find_all('tr')

    # The last 4 elements in the 'rows' list are irrelevant & generate a traceback while indexing.
    # So, I've sliced them out and added the other elements to a new list.
    all_rows = rows[2:-4]

    # Iterate through every element in the new row, which is stored in all_rows
    for row in all_rows:
        # Find all elements with the 'td' tag
        cols = row.find_all('td')
        # Index 1 is the name of scrip & 5 is the closing price of the scrip.
        stock_name = cols[1]
        stock_price = cols[5]
        print(stock_name.string, '\t', stock_price.string)
