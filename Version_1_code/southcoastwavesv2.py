from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.surfline.com/surf-report/bournemouth/584204214e65fad6'
           'a7709cf4?camId=5834968e3421b20545c4b525')

title = driver.title
print(title)

