from selenium import webdriver
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
request_url = 'https://movie.douban.com/'
chrome = webdriver.Chrome('C:\chrome\chromedriver.exe')
chrome.get(request_url)
# html = chrome.page_source
# print(html)

navs = chrome.find_element_by_xpath('//div[@class = "nav-items"]/ul')
print(navs)
print(navs.text)

# chrome.close()
chrome.quit()
