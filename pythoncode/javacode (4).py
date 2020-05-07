#导入selenium的webdriver库
from selenium import webdriver
#导入定时功能模块
import datetime
#导入时间模块
import time

#取得浏览器的控制权
driver = webdriver.Chrome()
#get()打开某某网址
driver.get("https://detail.tmall.com/item.htm?spm=a230r.1.14.6.4a2233a3iPl1Q0&id=585319218965&cm_id=140105335569ed55e27b&abbucket=17")
#点击登录*[
driver.find_element_by_xpath('').click()
driver.maximize_window()
driver.find_element_by_css_selector('').click()
time.sleep(20)

driver.find_element_by_xpath('').click()

now=datetime.datetime.now()
#输入定时执行时间 格式为(2020,4,10,22,50,44)年月日时分秒
times=datetime.datetime(2020,4,11,0,41,0)
#定义一个购买函数
def buy(times): 
#实现while True循环抢购    
    while True:
        if now > times:
            #如果到时间开始实现循环抢购
            while True:
                try：#处理异常语句
                    if driver.find_element_by_link_text('立即购买')：
                        driver.find_element_by_link_text('立即购买').click()
                        break#跳出循环
                except:#处理异常语句 如果try内不能执行 执行except内语句
                    print('不能购买')
            sleep(0.01)
            while True:
                try:
                    if driver.find_element_by_xpath('')：
                        driver.find_element_by_xpath('').click() 
                        break#跳出循环
                except:#处理异常语句 如果try内不能执行 执行except内语句
                    print('不能购买')