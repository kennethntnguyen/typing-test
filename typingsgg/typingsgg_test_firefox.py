#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import hack_typingsgg as h
url = 'https://typings.gg/'

# Enables headless mode for
#options = Options()
#options.headless = True

# This opens up a Firefox browser in headless mode
# pg = webdriver.Firefox(options=options)

# This opens up a Firefox browser
pg = webdriver.Firefox()

# Navigates to the specified web page
pg.get(url)

# Set the typing test to 100 words (50 words by default)
h.setTestLength(25, pg)

# Runs the test 5 times and printing the WPM results each time
for i in range(5):
  h.typeNormally(150,pg)
  h.redo(pg)
  print("WPM:", h.getWPM(pg))

# Closes the FireFox browser
pg.quit()
