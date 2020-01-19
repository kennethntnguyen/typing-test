# Hacking the Typing Test

Through the use of BeautifulSoup, Selenium and a FireFox webdriver I was able to hack the typing test to gain a WPM advantage.

# hack_typingsgg Module:

Function Name | Description
--------------|------------
setTestLength(n, page) | Set the number of words for the typing test, there are 3 choices: 10, 25, 50, 100 and 250 Words.
getWPM(page) | Returns the WPM results after a test or of the previous test.
redo(page) | Restarts the typing test.
getWordList(page) | Returns all the words from the typing test in order as a list of strings.
typeNormally(wpm, page) | Automates the typing test using the "realistic_typing.py" module.
typeFast(page) | Automates the typing test by sending words as a whole one by one from "word_list."
typeSuperFast(page) | Automates the typing test by sending the whole word list at once.

# realistic_typing Module:

Function Name | Description
--------------|------------
delayedTyping(word_list, element) | Set the delay between each keystroke to make the typing more natural and humanlike.
