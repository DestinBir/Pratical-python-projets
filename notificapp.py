from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title="*** Prendre une pause ***",
            message="Le repos est très important pour votre santé tant mentale que pysiologique. "
                    "Il est temps de prendre une pause de 30 min au min.",
            app_icon="",
            timeout=5)
        time.sleep(10)
