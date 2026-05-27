import csv
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

# Task 6
driver.get('https://owasp.org/Top10/2025/')
results = []
elements = driver.find_elements(By.XPATH, '//article//ol/li/a')
for link in elements:
    title = link.text.strip()
    href = link.get_attribute("href")
    links_dict = {
        'Title': title,
        'Link': href
        }
    results.append(links_dict)
driver.quit()
print(results)

# CSV file 
with open('assignment8/owasp_top_10.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Link'])
    for row in results:
        writer.writerow([row['Title'], row['Link']])
    
