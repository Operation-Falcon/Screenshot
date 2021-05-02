from selenium import webdriver
from config import path
from time import sleep
from selenium.webdriver.firefox.options import Options

def screenshot_url(url):
    options = Options()
    options.add_argument("--headless")
    driver=webdriver.Firefox(executable_path=path, service_log_path ='/dev/null', firefox_options=options)
    driver.get(url)
    sleep(1)
    driver.save_screenshot("./snapshot/screenshot.png")

def screenshot_file_url(filename):
    with open(filename, 'r')as file:
        file=file.readlines()
        options = Options()
        options.add_argument("--headless")
        for i in range(0, len(file)):
            driver=webdriver.Firefox(executable_path=path, service_log_path='/dev/null', firefox_options=options)
            driver.get(file[i])
            sleep(2)
            driver.save_screenshot(f"./snapshot/screenshot"+f"{i}"+".png")
