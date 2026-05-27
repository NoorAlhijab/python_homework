import pandas as pd
import json 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# Activate headless mode
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Enable headless mode
options.add_argument('--disable-gpu')  # Optional, recommended for Windows
options.add_argument('--window-size=1920x1080')  # Optional, set window size

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)


# Task 3
# Load the web page
driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")
books_list = driver.find_elements(By.CSS_SELECTOR, "li.row.cp-search-result-item")
#print(result_list)
results = []
for li in books_list:
    #print(li.text)
    try:
        # Get the book title
        title = li.find_element(By.CSS_SELECTOR, 'span.title-content')
        #print(title.text) 

        # Get the author names
        author_list = li.find_elements(By.CSS_SELECTOR, 'a.author-link')
        author_names = []
        for author in author_list:
            if author.text:
                author_names.append(author.text)

        # Check missing authors and convert to string
        if len(author_names) == 0:
            author_str = "Unknown"
        else:
            author_str = ";".join(author_names)
        #print(author_str)
         
        # Get format year
        format_year = li.find_element(By.CSS_SELECTOR, 'span.display-info-primary')
        #print(format_year.text)

        # Create book dictionary
        book_dict ={
            'Title': title.text,
            'Author': author_str,
            'Format-Year': format_year.text
        }
        # Append book_dict to results list
        results.append(book_dict)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        continue

#print(results)

# Create a DataFrame from results
df = pd.DataFrame(results)
print(df)

driver.quit()

# Task 4
# Write the DataFrame to a csv file 
df.to_csv('assignment8/get_books.csv', index=False)

# Write the results list out to a json file 
with open('assignment8/get_books.json', 'w') as file:
    json.dump(results, file, indent=4)