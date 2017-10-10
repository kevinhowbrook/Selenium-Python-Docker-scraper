#### Useful Docker container image

Forked from: [khozzy/selenium-python-chrome](https://goo.gl/Fu723f)

#### BUILD IMAGE:

You can choose between:

##### 1) Build from Dockerfile:

` docker build -t selenium . ` (in the same path of your Dockerfile)

##### 2) Pull it from docker hub:
` docker pull pimuzzo/selenium-python-xvfb `

#### RUN CONTAINER:

You can choose between:

##### 1) Joining inside
` docker run --name selenium -ti pimuzzo/selenium-python-xvfb bash`

##### 2) Using from outside
` docker run -ti -v /your_local_dir:/home/something pimuzzo/selenium-python-xvfb python /home/something/your_file.py `

Optional:
- You can specify the browser with the BROWSER environment variable

#### EXAMPLE OF CODE WITH SELENIUM:
```
#!/usr/bin/env python

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
source: http://goo.gl/cmLS9Z

#todo
 - redo readme with my bits
 cmd to run 
 ``` docker run --rm -v $(pwd)/code:/code -it selenium python /code/main.py```
 
