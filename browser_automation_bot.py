from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://quotes.toscrape.com")

time.sleep(2)

title = driver.title
quotes = driver.find_elements(By.CLASS_NAME, "text")

with open("browser_bot_output.txt", "w", encoding="utf-8") as f:
    f.write("Page title: " + title + "\n\n")
    for q in quotes:
        f.write(q.text + "\n")

print("Saved to browser_bot_output.txt")

input("Press ENTER to close the browser...")

driver.quit()