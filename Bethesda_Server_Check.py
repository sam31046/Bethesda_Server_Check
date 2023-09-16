# -*- coding: UTF-8 -*-

from selenium import webdriver
from fake_useragent import UserAgent  # Create random User-Agent
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import time

if __name__ == '__main__':
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Host": "https://mops.twse.com.tw",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Sec-GPC": 1,
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/95.0.4638.69 Mobile Safari/537.36",
    }
    ua = UserAgent()
    headers["User-Agent"] = ua.random
    opt = webdriver.ChromeOptions()
    opt.add_argument('--user-agent=%s' % headers)
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()),
                              options=opt)
    url = "https://status.bethesda.net/en"
    while True:
        driver.get(url)
        delay = 20  # seconds
        try:
            myElem = WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((By.CLASS_NAME,
                                                'current-status-container')))
            print("Page is ready!")

        except TimeoutError:
            print("Loading took too much time!")

        conditions = (driver.page_source.find("Investigating") == -1) or \
                     (driver.page_source.find("maintenance") == -1) or \
                     (driver.page_source.find("All Systems Operational") != -1)

        if conditions is True:
            print("Server is online!")
            break

        driver.close()
        time.sleep(300)  # Check every 5 minutes
