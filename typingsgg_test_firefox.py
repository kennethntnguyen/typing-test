#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import HackTypingsgg as htg
url = 'https://typings.gg/'

# Enables headless mode for
#options = Options()
#options.headless = True

# This opens up a Firefox browser
#pg = webdriver.Firefox(options=options)


pg = webdriver.Firefox()
# Navigates to the specified web page
pg.get(url)

htg.setTestLength(250, pg)
htg.typeFast(pg)
print(htg.getWPM(pg))

pg.quit()
