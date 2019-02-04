from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import winsound
import configparser

def alert():
    print("ALERT!!!")
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 1000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)
    return


config = configparser.ConfigParser()
config.read('config.ini')

if not "REMOTE" in config:
    driver = webdriver.Chrome()
    print("waiting to login")
    url = driver.command_executor._url
    session_id = driver.session_id

    config["REMOTE"] = {}
    config["REMOTE"]["url"] = url
    config["REMOTE"]["session_id"] = session_id
    print(url)
    print(session_id)

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

    print("Lütfen Login olunuz.")

    driver.get("http://usis.yildiz.edu.tr/main.jsp")
    exit(0)

url = config["REMOTE"]["url"]
session_id = config["REMOTE"]["session_id"]
driver = webdriver.Remote(command_executor=url, desired_capabilities={})
driver.session_id = session_id


print("Usis in bulunduğu pencere aranıyor.")
handles = driver.window_handles
size = len(handles)
for x in range(size):
    driver.switch_to.window(handles[x])
    print(driver.current_url)
    if "http://usis.yildiz.edu.tr/" in driver.current_url:
        break

alert()

def kontrol(ders_kod, ders_grup, mevcut_kontenjan, ders_isim):
    try:
        elems = driver.find_elements_by_xpath("//td[contains(text(),'" + ders_kod + "')]")
        pr = elems[ders_grup].find_element_by_xpath('..')
        ih: str = pr.get_attribute('innerHTML')
        if mevcut_kontenjan in ih:
            print("{} {} hala dolu".format(ders_kod, ders_isim))
        else:
            print("ALERT!!!")
            print("{} {} ŞUAN AÇIK!!!!!".format(ders_kod, ders_isim))
            alert()
    except Exception as e:
        print(e)
        print("{} {} Bulunamadı, bir sorun olmalı???".format(ders_kod, ders_isim))

def isvisible(ders_kod, ders_isim):
    try:
        elem = driver.find_element_by_xpath("//td[contains(text(),'{}')]".format(ders_kod))
        print("Actually found ALERT!!")
        print("{} {} ŞUAN AÇIK!!!!!".format(ders_kod, ders_isim))
        alert()
    except Exception as e:
        print("{} {} Hala bulunamadı".format(ders_kod, ders_isim))

while True:
    time.sleep(2)
    driver.get("http://usis.yildiz.edu.tr/CrsListOfferedCourses.do")
    time.sleep(1)
    driver.get("http://usis.yildiz.edu.tr/CrsListOfferedCoursesPrint.jsp")

    kontrol("BLM3810",0,"55/53", "Biyoenformatiğe Giriş")
    isvisible("BLM0000","Hayalet Ders")



