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


#### EXAMPLE OF CODE WITH SELENIUM AND FIREFOX:
```
from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=0, size=(800, 600))
display.start()

# now Firefox will run in a virtual display. 
# you will not see the browser.
browser = webdriver.Firefox()
browser.get('http://www.google.com')
print browser.title
browser.quit()

display.stop()
```

#### EXAMPLE OF CODE WITH GOOGLE HEADLESS
```
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

display = Display(visible=0, size=(1200, 800))
display.start()
# start Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--window-size=1200x800")
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('http://google.com/')
print(browser.title)
browser.quit()
display.stop()
```

