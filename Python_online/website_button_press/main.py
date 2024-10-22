# import module
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
import time

# Create the webdriver object. Here the
# chromedriver is present in the driver
# folder of the root directory.
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

# get url
url=input("Mi az URL? ")
driver.get(url)

# Maximize the window and let code stall
# for 10s to properly maximise the window.
driver.maximize_window()
time.sleep(10)

# Obtain button by link text and click.

button = driver.find_element(By.XPATH, "//form[input/@class='primary']")
button.click()
