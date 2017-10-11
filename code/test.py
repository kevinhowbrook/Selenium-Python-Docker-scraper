#!/usr/bin/env python

from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=0, size=(1200, 800))
display.start()

# now Firefox will run in a virtual display.
# you will not see the browser.
browser = webdriver.Firefox()
browser.get('http://google.com/')
print(browser.title)
browser.save_screenshot('/code/ss.png')
browser.quit()
display.stop()