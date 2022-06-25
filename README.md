## Useful Docker Selenium container image for automation

Forked from: [dimmg/dockselpy](https://github.com/dimmg/dockselpy)

#### BUILD IMAGE:
` docker build -t selenium . ` (in the same path as the Dockerfile)

#### Running with fabric
Run ```fab help``` for tasks
 - ```fab run```
   - Runs a container, mounting ./code and local /etc/hosts, runs ./code/main.py and removes the container when done
 - ```fab test```
   - Runs a container, mounting ./code and local /etc/hosts, runs ./code/test.py and removes the container when done


#### RUN CONTAINER:

 ```
 // run container, mount the python code, mount our local etc/hosts file, image to run (selenium) execute python
 docker run --rm -v $(pwd)/code:/code -v /etc/hosts:/etc/hosts -it selenium python /code/main.py
 ```

#### ChromeDriverManager

This uses [Webdriver Manager for Python](https://github.com/SergeyPirogov/webdriver_manager) to simplify management of binary drivers for different browsers. It's a massive headache keeping on top of these bianaries, ChromeDriverManager will install the needed bianary when it's defined, a la:

```
browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
```

#### EXAMPLE OF CODE WITH GOOGLE HEADLESS
```
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

display = Display(visible=0, size=(1200, 800))
display.start()
# start Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--window-size=1200x800")
browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
browser.get('http://google.com/')
print(browser.title)
browser.quit()
display.stop()
```
