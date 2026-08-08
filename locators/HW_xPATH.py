# open browser
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    # open site
    driver.get("https://telranedu.web.app/login")

    # by tag_name
    div = driver.find_element(By.TAG_NAME, "div")
    div_1 = driver.find_element(By.CSS_SELECTOR, "div")
    div_2 = driver.find_element(By.XPATH, "//div")

    h1 = driver.find_element(By.TAG_NAME,"h1")
    h1_1 = driver.find_element(By.CSS_SELECTOR, "h1")
    h1_2 = driver.find_element(By.XPATH, "//h1")

    input_ = driver.find_element(By.TAG_NAME, "input")
    input_1 = driver.find_element(By.CSS_SELECTOR,"input")
    input_3 = driver.find_element(By.XPATH, "//input")

    a_list = driver.find_elements(By.TAG_NAME,"a")
    a_list_1 = driver.find_elements(By.CSS_SELECTOR, "a")
    a_list_2 = driver.find_elements(By.XPATH, "//a" )
    for a in a_list:
        print(a.text.lower())

# by class
    container = driver.find_element(By.CLASS_NAME,"container")
    container_1 = driver.find_element(By.CSS_SELECTOR,".container")
    container_3 = driver.find_element(By.XPATH, "//div[@class='container']")

    navbar = driver.find_element(By.CLASS_NAME,"navbar-component_nav__1X_4m")
    navbar_1 = driver.find_element(By.CSS_SELECTOR, ".navbar-component_nav__1X_4m")
    navbar_2 = driver.find_element(By.XPATH, "//div[@class='navbar-component_nav__1X_4m']" )

    login_login = driver.find_element(By.CLASS_NAME,"login_login__3EHKB")
    login_login_1 = driver.find_element(By.CSS_SELECTOR, ".login_login__3EHKB")
    login_login_2 = driver.find_element(By.XPATH, "//div[@class='login_login__3EHKB']")


# by id

    root = driver.find_element(By.ID,"root")
    root_1 = driver.find_element(By.CSS_SELECTOR,"#root")
    root_2 = driver.find_element(By.XPATH, "//*[@id='root']")

    root_3 = driver.find_elements(By.ID,"root")
    root_4 = driver.find_elements(By.CSS_SELECTOR, "#root")
    root_5 = driver.find_elements(By.XPATH, "//*[@id='root']")

#by text

    home = driver.find_element(By.LINK_TEXT,"HOME" )
    phonebook = driver.find_element(By.CSS_SELECTOR, "h1:first-child")
    print(phonebook.text)
    about = driver.find_element(By.XPATH,"//*[@href='/about']")
    login = driver.find_element(By.XPATH, "//*[@href='/login']")



# close browser
finally:
    driver.quit()
