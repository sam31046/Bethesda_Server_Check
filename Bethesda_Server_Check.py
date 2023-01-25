# -*- coding: UTF-8 -*-
__author__ = "Jhong,Dong You"

from selenium import webdriver
from fake_useragent import UserAgent  # Create random User-Agent
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
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/95.0.4638.69 Mobile Safari/537.36",
    }
    ua = UserAgent()
    headers["User-Agent"] = ua.random
    opt = webdriver.ChromeOptions()
    opt.add_argument('--user-agent=%s' % headers)
    driver = webdriver.Chrome(options=opt)
    url = "https://status.bethesda.net/en"
    while True:
        driver.get(url)
        conditions = (driver.page_source.find("Investigating") == -1) or \
                     (driver.page_source.find("All Systems Operational") != -1)
        if conditions is True:
            print("Server is online!")
            break
        driver.close()
        time.sleep(300)  # Check every 5 minutes
