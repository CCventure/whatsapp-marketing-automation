import time
from browser import Browser
from messenger import Messenger
import config
import os
import logging

logger = logging.getLogger(config.LOGGING_NAME)


def main():
    browser = Browser()
    messenger = Messenger(browser.driver)
    url = config.URL
    browser.open_url(url)
    time.sleep(config.LOGIN_TIME)
    
    filename = config.NUMBERS_FILE
    logger.info(f"Currently working on {filename}")
    
    while True:
        logger.info(config.PROCCES_MESSAGE)
        messenger.process_numbers(filename)
        logger.info(config.COMPLETED_MESSAGE) 
        break

if __name__ == "__main__":
    main()
