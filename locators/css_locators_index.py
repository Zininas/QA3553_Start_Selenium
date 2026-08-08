#page_url = "file:///Users/aszinin/Downloads/21.index%202.html"
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By

html_file = Path(__file__).parent / "21.index 2.html"
page_url = html_file.as_uri()
driver = webdriver.Chrome()
try:
    driver.get(page_url)
    button = driver.find_element(By.TAG_NAME, "button")
    print(button.tag_name)
    print(button.text)
    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        print(link.text)
    button_1 = driver.find_element(By.CSS_SELECTOR, "button")
    container = driver.find_element(By.CSS_SELECTOR, ".container")
    #container_1 = driver.find_element(By.TAG_NAME, "container")
    nav = driver.find_element(By.ID, "nav")
    nav_1 = driver.find_element(By.CSS_SELECTOR, "#nav")
    print("Nav id: ", nav.tag_name)
    print("Nav id: ", nav_1.tag_name)
  #  input("Press Enter to close the browser...")
finally:
    driver.quit()