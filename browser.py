from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import config

class Browser:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument(f'--user-data-dir={config.CHROME_PROFILE_PATH}')
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)

    def open_url(self, url):
        self.driver.get(url)
