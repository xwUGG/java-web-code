#导入selenium的webdriver库
from selenium import webdriver
#导入定时功能模块
import datetime
#导入时间模块
import time

#取得浏览器的控制权
driver = webdriver.Chrome()
#get()打开某某网址
driver.get("http://taobao.com")
#driver.find_element_by_id（）定位id的元素的搜索框.sen_keys搜索框里面输入
driver.find_element_by_id("q").send_keys('手机')
#点击搜索按钮 定位元素copy xpath 凡是定位xpath都是在网页复制
#按钮都用xpath定位
driver.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button').click()
#最大化浏览器窗口
driver.maximize_window()
#休眠20秒后在运行
time.sleep(20)
driver.find_element_by_xpath('//*[@id="J_Itemlist_Pic_610041391219"]').click()