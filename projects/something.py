from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://google.com/')

browser.implicitly_wait(10)
browser.maximize_window()

browser.find_element_by_name("q").send_keys("Automation Step by Step")
browser.find_element_by_name("btnK").click()

