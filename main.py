from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def main():
    """
    """
    chrome = webdriver.Chrome("./driver/chromedriver.exe")
    chrome.get("https://www.google.co.jp")
    search_box = chrome.find_element_by_name("q")
    search_box.send_keys("qwerty")
    search_box.send_keys(Keys.RETURN)

    time.sleep(5)


if __name__ == "__main__":
   """
   """
   main()
