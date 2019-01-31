import time
import os
import streamlink
import cv2
from multiprocessing import Process

i = 0
NASAstream = 'https://www.ustream.tv/embed/17074538?html5ui&autoplay=true'


def changeBackground():
        try:
            os.system('reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d "%s" /f >nul' % (
                "C:/Windows/Temp/bkimagetemp.bmp"))
            time.sleep(0.2)
            os.system('RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters')
            time.sleep(0.2)
        except Exception:
            print("error updating background path")


def stream_to_url(url_name, quality='best'):
    streams = streamlink.streams(url_name)
    if streams:
        return streams[quality].to_url()
    else:
        raise ValueError("No steams were available")


def main(url, quality='best', fps=30.0):
    imagePath = "C:/Windows/Temp/bkimagetemp.bmp"
    stream_url = stream_to_url(url, quality)
    print("Loading stream {0}".format(stream_url))
    cap = cv2.VideoCapture(stream_url)

    frame_time = int((1.0 / fps) * 1000.0)

    while True:
        try:
            isFrame, frame = cap.read()
            if isFrame:
                cv2.imshow('frame',frame)
                cv2.imwrite(imagePath, frame)

                if cv2.waitKey(frame_time) & 0xFF == ord('q'):
                    break


        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    Process(target=main, args=[NASAstream]).start()
    Process(target=changeBackground).start()

