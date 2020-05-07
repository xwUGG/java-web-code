#导入selenium的webdriver库
from selenium import webdriver
#导入定时功能模块
import datetime
#导入时间模块
import time





#取得浏览器的控制权
driver = webdriver.Chrome()

def login():#定义一个登录函数
    driver.get('https://m.51tiangou.com/product/listing.html?id=14967495&scp=07.searchresult.product.0.p1okm')#网址

    driver.maximize_window()#最大化窗口
    if driver.find_element_by_link_text('立即购买'):
        driver.find_element_by_link_text('立即购买').click()
    time.sleep(2)
    if driver.find_element_by_link_text('确定'):
        driver.find_element_by_link_text('确定').click()    
time.sleep(60)#延时60s
        
    

    
    
#定义一个购买函数
def buy(times):
#实现while True循环抢购    
    while True:
        now=datetime.datetime.now()
        times = datetime.datetime(2020,4,11,23,40,0)

        if now > times:
            #比较要用字符串比较
            #如果到时间开始实现循环抢购
            while True:
                try:
                #处理异常语句
                    if driver.find_element_by_link_text('立即购买'):
                        driver.find_element_by_link_text('立即购买').click()
                    
                    if driver.find_element_by_link_text('付款'):
                        driver.find_element_by_link_text('付款').click()
                        break
                    #跳出循环
                except:#处理异常语句 如果try内不能执行 执行except内语句  可以有多个
                    if driver.find_element_by_link_text('我知道了'):
                        driver.find_element_by_link_text('我知道了').click()
                        print('时间未到')
            time.sleep(0.01)
            while True:
                try:
                    if driver.find_element_by_link_text('确定'):
                        driver.find_element_by_link_text('确定').click()
                        break#跳出循环
                except:#处理异常语句 如果try内不能执行 执行except内语句
                    print('不能购买')
            while True:
                try:
                #处理异常语句
                    
                    if driver.find_element_by_link_text('付款'):
                        driver.find_element_by_link_text('付款').click()
                        break
                    #跳出循环
                except:
                    #处理异常语句 如果try内不能执行 执行except内语句  可以有多个
                    if driver.find_element_by_link_text('我知道了'):
                        driver.find_element_by_link_text('我知道了').click()
                        print('时间未到')