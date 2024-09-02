import time
import csv
import logging
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import config

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(config.LOGGING_NAME)


class Messenger:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.load_message()

    def load_message(self):
        with open('message.txt', 'r', encoding='utf-8') as file:
            self.msg = file.read()

    def send_message(self, num):
        link = f'{config.URL}send?phone={num}&text={self.msg}'
        try:
            self.driver.get(link)

            input_element_select = config.INPUT_ELEMENT
            time.sleep(10)
            input_field = self.driver.find_element(By.XPATH, input_element_select)

            input_field.click()
            input_field.send_keys(Keys.ENTER)
            logger.info(f"{config.APPROVAL} {num}")


        except WebDriverException:
            logger.info(f"{config.REJECTION} {num}")


    def process_numbers(self, filename):
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                num = row[0]
                self.send_message(num)
                time.sleep(config.SEND_MSG_TIME)
