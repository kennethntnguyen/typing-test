# Note: This module was created for learning purposes.
# The following module contains functions used to automatically perform the typing test from
# the website "https://typings.gg".

# Note: Functions that have "page" in their parameters require the user to pass a Selenium webdriver
# object in order for the function to operate as intended.

import re
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

# Set the number of words for the typings.gg test
def setTestLength(n, page):
  if n == 10:
    page.find_element_by_id('wc-10').click()
  elif n == 25:
    page.find_element_by_id('wc-25').click()
  elif n == 50:
    page.find_element_by_id('wc-50').click()
  elif n == 100:
    page.find_element_by_id('wc-100').click()
  elif n == 250:
    page.find_element_by_id('wc-250').click()
  else:
    print("The typing test doesn't support those number of words.")

# Reparses the HTML - this is needed in order to extract the current sequence of words
def reparseHTML(page):
  html = page.execute_script("return document.documentElement.outerHTML")
  soup = BeautifulSoup(html, 'html.parser')
  return soup

# Gets the WPM results from the page
def getWPM(page):
  soup = reparseHTML(page)
  wpm = str(soup.find(id='right-wing'))
  wpm = re.search('(?<=WPM: )(.*)(?= / )', wpm)
  # Returns the part of the string that matches
  wpm = wpm.group()
  if(wpm == 'XX'):
    wpm = 'Typing test is not done.'
  else:
    wpm = int(wpm)
  return wpm

# Function that resets typing test to a new set of words
def redo(page):
  # Finds the input bar for typing
  type_here = page.find_element_by_id('input-field')
  # Finds the redo button
  redo = page.find_element_by_id('redo-button')
  type_here.send_keys(Keys.TAB)
  redo.send_keys(Keys.ENTER)

# Prints the list of words in the text display
def printWordList(page):
  soup = reparseHTML(page)
  word_list = str(soup.find(id='text-display'))
  word_list = re.search('(?<=\"highlight\">)(.*)(?=</div>)', word_list).group()
  word_list = re.sub(' </span>','',word_list)
  word_list = re.split('<span>',word_list)
  return word_list

# Performs the typing test word by word - sends each word in whole at once
def typeFast(page):
  soup = reparseHTML(page)
  # Finds the input bar for typing
  type_here = page.find_element_by_id('input-field')
  word_list = getWordList(page)
  for i in word_list:
    type_here.send_keys(i)
    time.sleep(0.175)
    type_here.send_keys(' ')

# Performs the typing test by sending the entire sequence of words for the current test
def typeSuperFast(page):
  soup = reparseHTML(page)
  # Finds the input bar for typing
  type_here = page.find_element_by_id('input-field')
  word_list = getWordList(page)
  type_here.send_keys(word_list)
