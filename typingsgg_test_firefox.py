#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import hack_typingsgg as h
url = 'https://typings.gg/'

# Enables headless mode for
#options = Options()
#options.headless = True

# This opens up a Firefox browser
#pg = webdriver.Firefox(options=options)

pg = webdriver.Firefox()
# Navigates to the specified web page
pg.get(url)

h.setTestLength(100, pg)

for i in range(5):
  h.typeNormally(pg)
  h.redo(pg)
  print("WPM:", h.getWPM(pg))

pg.quit()
