## Useful Docker Selenium container image for automation

Forked from: [khozzy/selenium-python-chrome](https://goo.gl/Fu723f)

#### BUILD IMAGE:
` docker build -t selenium . ` (in the same path of your Dockerfile)

#### RUN CONTAINER:

 ``` 
 // run container, mount the python code, mount our local etc/hosts file, image to run (selenium) execute python
 docker run --rm -v $(pwd)/code:/code -v /etc/hosts:/etc/hosts -it selenium python /code/main.py
 ```


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

#todo
 - Fabric scripts
 
