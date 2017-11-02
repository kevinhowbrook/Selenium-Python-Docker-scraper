from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Example:
    def __init__(self):
        display = Display(visible=0, size=(1400, 2800))
        display.start()
        # now Firefox will run in a virtual display.
        # you will not see the browser.
        browser = webdriver.Firefox()
     #   browser.implicitly_wait(10) # seconds
        browser.get('http://google.com/')
        print(browser.title)
        browser.save_screenshot('/code/screenshots/eg.png')
        browser.quit()
        display.stop()