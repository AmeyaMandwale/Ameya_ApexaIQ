"""windows 11 Scrapper"""
#import libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome()

driver.get("https://learn.microsoft.com/en-us/windows/release-health/windows11-release-information")
time.sleep(1)

tables = driver.find_elements(By.XPATH, "//table")

All_tables = [] 

for table in tables:
    table_list = []
    all_table_rows = table.find_elements(By.XPATH, ".//tr")
    for table_row in all_table_rows:
        row = []
        all_data = table_row.find_elements(By.XPATH, ".//td | .//th")
        for data in all_data:
            row.append(data.get_attribute("textContent"))
            # row.append(data.text)    # the content that is actually visible to the user in the browser.
        table_list.append(row)
    All_tables.append(table_list)

    df = pd.DataFrame(table_list)
    df.to_csv(r"D:\ApexaIQ\Day3.csv", mode="a", index=False, header=not pd.io.common.file_exists("Day3.csv"))

    df_empty = pd.DataFrame([[""] * len(df.columns)])  # Empty row with the same number of columns
    df_empty.to_csv(r"D:\ApexaIQ\Day3.csv", mode="a", index=False, header=not pd.io.common.file_exists("Day3.csv"))

print(All_tables)

print(df)