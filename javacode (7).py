from selenium import webdriver
#导入定时功能模块
import datetime
#导入时间模块
import time





#取得浏览器的控制权
driver = webdriver.Chrome()

driver.get('https://m.51tiangou.com/product/listing.html?id=14967495&scp=07.searchresult.product.0.p1okm')#网址

driver.maximize_window()#最大化窗口


driver.find_element_by_xpath('/html/body/div[2]/div[3]/div').click()
#不同的网站用一种元素定位不行就换另一种

driver.find_element_by_xpath('//*[@id="skuPanel"]/div[2]').click()    

time.sleep(80)#延时60s

def buy(times):
#实现while True循环抢购    
 
       
            #比较要用字符串比较
            #如果到时间开始实现循环抢购
            while True:
                try:
                #处理异常语句
                    driver.find_element_by_xpath('/html/body/div[2]/div[3]/div').click()
                    
                    driver.find_element_by_xpath('//*[@id="skuPanel"]/div[2]').click() 

                    time.sleep(5)

                    driver.find_element_by_xpath('/html/body/div[24]/div/button')
                    break
                    #跳出循环
                except:#处理异常语句 如果try内不能执行 执行except内语句  可以有多个
                    print('时间未到')
            