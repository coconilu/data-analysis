from selenium import webdriver
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
request_url = 'https://movie.douban.com/'
chrome = webdriver.Chrome('C:\\chrome\\chromedriver.exe')
chrome.get(request_url)
# html = chrome.page_source
# print(html)

# xpath
# navs = chrome.find_elements_by_xpath('//div[@class = "nav-items"]/ul/li/a')

# selector
navs = chrome.find_elements_by_css_selector('div.nav-items>ul>li>a')

for nav in navs:
  print(nav.text)

# chrome.close()
chrome.quit()
