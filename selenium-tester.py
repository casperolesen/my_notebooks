from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')

#browser = webdriver.Firefox()
browser = webdriver.Firefox(firefox_binary=binary)
browser.get('http://www.krak.dk')