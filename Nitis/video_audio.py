import urllib.request
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup  # return html data from parse
from urllib.parse import urlparse
from playsound import playsound
from gtts import gTTS
import sys

from selenium.webdriver.chrome.options import Options


class VAFetcher:
    def __init__(self, url):
        self.driver = webdriver.Edge(r"C:\Users\Uditya Raj\PycharmProjects\pythonml\msedgedriver.exe")
        self.html = urllib.request.urlopen(url)
        self.video_ids = re.findall(r"watch\?v=(\S{11})", self.html.read().decode())
        self.driver.get("https://www.youtube.com/watch?v=" + self.video_ids[0])
        time.sleep(240)
