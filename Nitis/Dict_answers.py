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


class wikiFetcher:
    def __init__(self, url):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=chrome_options,
                                       executable_path=r'C:\Users\Uditya Raj\PycharmProjects\pythonml\chromedriver.exe')
        #self.driver = webdriver.PhantomJS(executable_path=r"C:\Users\nivaniva\phantomjs-2.1.1-windows\bin\phantomjs.exe")  # javascript browser
        #self.driver = webdriver.Edge(r"C:\Users\Uditya Raj\PycharmProjects\pythonml\msedgedriver.exe")
        self.driver.wait = WebDriverWait(self.driver, 5)
        self.url = url
        self.lookup()

    def respond2(self, response):
        language = 'en'
        myobj = gTTS(text=response, lang=language, slow=False)
        myobj.save("wikiAnswer.mp3")
        playsound('./wikiAnswer.mp3')

    def lookup(self):
        self.driver.get(self.url)
        try:
            ip = self.driver.wait.until(EC.presence_of_all_elements_located(
                (By.CLASS_NAME, 'gsfi')
            ))
        except:
            print('...')

        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        #answer = soup.find_all(class_='mw-body-content mw-content-ltr')
        answer = soup.find_all(class_='def')
        print(answer[0].get_text())
        self.respond2("Answer to your question is "+answer[0].get_text())