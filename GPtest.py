# -*- coding: utf-8 -*-
from time import sleep
from selenium import webdriver

options = webdriver.ChromeOptions()
#關掉自動控制顯示
options.add_argument('disable-infobars')

#注意!!!這邊需要使用到個人User資料
#使用個人資料開啟瀏覽器以防止它創建默認的瀏覽器
#路徑不同請自行更改個人路徑
options.add_argument("user-data-dir=C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data")

broswer = webdriver.Chrome(chrome_options=options)

GpIndex = 0
page = input("請輸入頁數 :")
bsn = input("請輸入BSN數值:")
snA = input("請輸入SNA數值:")

pagea = str(page)
bsna  = str(bsn)
snAa = str(snA)
checkname = ""


while True:
    #進入網址選定網址
    broswer.get("https://forum.gamer.com.tw/C.php?page="+pagea+"&bsn="+bsna+"&snA="+snAa+"")
    sleep(3)
    #判斷14格數根據網頁中的(((c-section)))數量
    for x in range(1,14):
        #用try來做判斷，防止搜尋不到中斷程式執行
        try:
            #打印第幾次判斷
            print(x)
            sleep(1)
            #使用用絕對位置獲取帳號ID
            Findaccount = broswer.find_element_by_xpath("//div[@id ='BH-master']/section[@class ='c-section']["+str(x)+"]/div[@class ='c-section__main c-post ']/div [@class ='c-post__header']/div[@class = 'c-post__header__author']/a[@class ='userid']")
            #判斷找到新帳號和舊帳號是否相等
            #如果不相等繼續下面的判斷
            print(Findaccount.text +"   checkname:" + checkname)
            if checkname != Findaccount.text:
                #如果不相等將新帳號取代舊帳號防止GP冷卻///不一定成功
                checkname = Findaccount.text
                sleep(2)
                #使用絕對路徑獲取推的按鈕
                FindGp = broswer.find_elements_by_xpath("//div[@class ='c-section__main c-post ']/div[@class ='c-post__body']/div[@class ='c-post__body__buttonbar']/div[@class ='gp']")[GpIndex]
                print("click")
                sleep(1)
                FindGp.click()
                print("yes")
                GpIndex +=1
        except :
            #失敗打印NO
            print("NO")
    page +=1
    pagea = str(page)
    GpIndex = 0