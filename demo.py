from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

web = Chrome()  # 初始化浏览器
web.get('http://erp.lemfix.com/login.html')  # 访问网站

web.implicitly_wait(10)  # 设置一个隐性等待时间10s

web.find_element(By.XPATH, '//input[@id="username"]').send_keys('test123')  # 账号
web.find_element(By.XPATH, '//input[@id="password"]').send_keys('123456')  # 密码
web.find_element(By.XPATH, '//button[@id="btnSubmit"]').click()  # 点击登录

web.find_element(By.XPATH, '//span[text()="零售出库"]').click()  # 点击零售出库

data_id = web.find_element(By.XPATH, '//a[@title="零售出库"]').get_attribute('data-tab-id')
iframe_id = data_id + '-frame'

web.switch_to.frame(iframe_id)

web.find_element(By.XPATH, '//input[@name="searchNumber"]').send_keys('13')
web.find_element(By.XPATH, '//span[text()="查询"]').click()  # 点击查询

number = web.find_element(By.XPATH, '//div[@class="datagrid-cell datagrid-cell-c1-number"][1]').text
print(number)
