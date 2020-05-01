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
#20秒是用来登录的
driver.find_element_by_xpath('//*[@id="J_Itemlist_Pic_610041391219"]').click()
#获取网页句柄  每一个网页有一个句柄序列号
handle=driver.window_handles
#通过句柄切换窗口 到第二个窗口  从0开始计数
driver.switch_to_window(handle[1])
#获取当地时间
now=datetime.datetime.now()
#输入定时执行时间 格式为(2020,4,10,22,50,44)年月日时分秒
sched_Timer=datetime.datetime(2020,4,10,23,45,0)
if now==sched_Timer:
    #点击购买按钮
    driver.find_element_by_xpath('//*[@id="J_Itemlist_Pic_610041391219"]').click()

