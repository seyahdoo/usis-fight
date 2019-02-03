import requests
import time
import winsound


def alert():
    print("ALERT!!!")
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 1000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)
    return


def cant_connect():
    print('USIS is DOWN')
    alert()
    return


def website_up():
    print('USIS is UP')
    return


while True:
    time.sleep(2)
    try:
        request = requests.get('http://usis.yildiz.edu.tr/')
        if request.status_code == 200:
            website_up()
        else:
            cant_connect()
    except Exception as e:
        cant_connect()

