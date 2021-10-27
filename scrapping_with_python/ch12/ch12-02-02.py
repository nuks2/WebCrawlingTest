from selenium import webdriver

driver = webdriver.PhantomJS(executable_path='./phantomjs-2.1.1-macosx/bin/phantomjs')
driver.get("http://pythonscraping.com")
driver.implicitly_wait(1)
print(driver.get_cookies())
print('-----------------------------------------------------------------------------')

savedCookies = driver.get_cookies()

# driver2 = webdriver.PhantomJS(executable_path='./phantomjs-2.1.1-macosx/bin/phantomjs')
driver2 = webdriver.Chrome(executable_path='/Volumes/DevHD/LearningProjects/WebCrawlingTest/web_driver/chromedriver')   
driver2.get("http://pythonscraping.com")
driver2.implicitly_wait(1)
driver2.delete_all_cookies()
for cookie in savedCookies:
    print('cookie: ', cookie)
    driver2.add_cookie(cookie)


driver2.get("http://pythonscraping.com")
driver.implicitly_wait(1)
print(driver2.get_cookies())