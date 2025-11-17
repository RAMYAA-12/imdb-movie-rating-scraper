from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("user-agent=Mozilla/5.0")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.imdb.com/chart/top/")

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item"))
)

movie_rows = driver.find_elements(By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item")

movies = []
for row in movie_rows:
    title = row.find_element(By.CSS_SELECTOR, "h3.ipc-title__text").text
    year = row.find_element(By.CSS_SELECTOR, ".cli-title-metadata-item:nth-child(1)").text
    rating = row.find_element(By.CSS_SELECTOR, ".ipc-rating-star--rating").text
    movies.append([title, year, rating])

driver.quit()

df = pd.DataFrame(movies, columns=["Title", "Year", "Rating"])
df.to_csv("imdb_top_250.csv", index=False)

print("DONE!! File saved as imdb_top_250.csv")
