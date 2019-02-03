from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import winsound


def alert():
    print("ALERT!!!")
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 1000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)
    return


# driver = webdriver.Chrome()
# print("waiting to login")
# url = driver.command_executor._url
# print(url)
# session_id = driver.session_id
# print(session_id)
# exit(0)

url = "http://127.0.0.1:54085"
session_id = "3cf17ed03d23c19e936af8c91cff5825"
driver = webdriver.Remote(command_executor=url, desired_capabilities={})
driver.session_id = session_id

# driver.get("http://usis.yildiz.edu.tr/main.jsp")


handles = driver.window_handles
size = len(handles)
for x in range(size):
    driver.switch_to.window(handles[x])
    print(driver.current_url)
    if driver.current_url == "http://usis.yildiz.edu.tr/CrsListOfferedCourses.do":
        break

alert()

while True:
    time.sleep(2)
    driver.get("http://usis.yildiz.edu.tr/CrsListOfferedCourses.do")
    time.sleep(1)
    driver.get("http://usis.yildiz.edu.tr/CrsListOfferedCoursesPrint.jsp")

    ders_kod = "BLM3810"
    ders_grup = 0
    mevcut_kontenjan = "30/30"

    try:
        elems = driver.find_elements_by_xpath("//td[contains(text(),'" + ders_kod + "')]")
        pr = elems[ders_grup].find_element_by_xpath('..')
        ih: str = pr.get_attribute('innerHTML')
        if mevcut_kontenjan in ih:
            print("Biyoenformatiğe Giriş hala dolu")
        else:
            print("ALERT!!!")
            print("BLM3810 Biyoenformatiğe Giriş ŞUAN AÇIK!!!!!")
            alert()
    except Exception as e:
        print(e)
        print("not found")

    # try:
    #     elem = driver.find_element_by_xpath("//td[contains(text(),'BLM3520')]")
    #     print("Actually found ALERT!!")
    #     print("BLM3520 Mobil ŞUAN AÇIK!!!!!")
    #     alert()
    # except Exception as e:
    #     print("not found")

