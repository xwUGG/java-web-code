#导入selenium的webdriver库
from selenium import webdriver
#导入定时功能模块
import datetime
#导入时间模块
import time

now=datetime.datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))#获取此时的时间并打印

times = input('输入抢购时间格式为:2020-03-12 20:30:37.123456')


#取得浏览器的控制权
driver = webdriver.Chrome()

def login():#定义一个登录函数
    driver.get('')#网址
    #点击登录
    if driver.find_element_by_xpath(''):#寻找登录按钮
        driver.find_element_by_xpath('').click()#点击
        driver.maximize_window()#最大化窗口
        time.sleep(60)#延时60s
        driver.find_element_by_css_selector('')#定位商品选项
        driver.find_element_by_css_selector('').click()#点击
        #css定位元素最佳 一般用xpath
    

    driver.find_element_by_xpath('').click()
    
#定义一个购买函数
def buy(times): 
#实现while True循环抢购    
    while True:
        now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        if now > times:#比较要用字符串比较
            #如果到时间开始实现循环抢购
            while True:
                try：#处理异常语句
                    if driver.find_element_by_link_text('立即购买')：
                        driver.find_element_by_link_text('立即购买').click()
                    if driver.find_element_by_link_text('确定')
                        driver.find_element_by_link_text('确定').click()
                    if driver.find_element_by_link_text('付款')
                        driver.find_element_by_link_text('付款').click()
                        break#跳出循环
                except:#处理异常语句 如果try内不能执行 执行except内语句  可以有多个
                    if driver.find_element_by_link_text('我知道了')：
                        driver.find_element_by_link_text('我知道了').click()
                        print('时间未到')
                except:    
                    print('不能购买')
            sleep(0.01)
            while True:
                try:
                    if driver.find_element_by_xpath('')：
                        driver.find_element_by_xpath('').click() 
                        break#跳出循环
                except:#处理异常语句 如果try内不能执行 执行except内语句
                    print('不能购买')