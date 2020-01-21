import time
import numpy
from selenium.webdriver.common.keys import Keys

# Arbitratily set standard deviation. I chose what ever made the automated typing look more natural
std_dev = 0.02

# Used to type a list of words to the specified element from a Selenium object
def delayedTyping(wpm, word_list, element):
    # Splits word_list into a list of characters
    char_list = __splitWordList(word_list)
    num_of_chars = len(char_list)

    # Calculating the equivalence of the average length of words in word_list
    mean_word_length = num_of_chars/len(word_list)
    # This calculates the average time between keystrokes needed to roughly obtain the desired WPM
    mean_keystroke_time = 60/(mean_word_length*wpm)

    # Absolute value is taken since sleep function only allows values >=0
    keystroke_time = abs(numpy.random.normal(mean_keystroke_time, std_dev, num_of_chars))

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
