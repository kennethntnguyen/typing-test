import time
import numpy
from selenium.webdriver.common.keys import Keys

mean, std_dev = 0.075, 0.05

# Used to type a list of words to the specified element from a Selenium object
def delayedTyping(word_list, element):
    char_list = __splitWordList(word_list)
    num_of_chars = len(char_list)
    # Absolute value is taken since sleep function only allows values >=0
    keystroke_time = abs(numpy.random.normal(mean, std_dev, num_of_chars))

    for i in range(num_of_chars):
        element.send_keys(char_list[i])
        time.sleep(keystroke_time[i])

# Splits the list of words into list of characters
def __splitWordList(word_list):
    char_list = []
    for words in word_list:
        for chars in words:
            char_list.extend(chars)
        char_list.extend(' ')
    return char_list
