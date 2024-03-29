from pyvirtualdisplay import Display
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

class Example:
    def __init__(self):
        display = Display(visible=0, size=(1200, 800))
        display.start()

        # now Firefox will run in a virtual display.
        # you will not see the browser.
        # start Chrome
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--window-size=1200x800")
        chrome_options.add_argument('--disable-dev-shm-usage')
        browser = webdriver.Chrome(options=chrome_options)
        browser.get('http://google.com/')

        ## test bs4
        html_source = browser.page_source

        soup = BeautifulSoup(html_source, 'html.parser')
        links = soup.findAll("a")
        data = []
        for count, elem in enumerate(links):
            data.append(elem)

        print(browser.title)
        print(str(len(data)) + 'Links found')

        browser.save_screenshot('/code/ss.png')
        browser.quit()
        display.stop()
