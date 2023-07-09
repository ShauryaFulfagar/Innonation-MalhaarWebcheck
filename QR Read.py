import cv2
import imutils
from pyzbar import pyzbar
import numpy as np

camera = cv2.VideoCapture(2)

while True:
    switchRet, frame = camera.read()
    if not switchRet: break
    
    
    frame = cv2.bitwise_not(frame)
    frame = cv2.rotate(frame, cv2.ROTATE_180)

    frame = imutils.resize(frame, width=800)

    def endPause():
            global data
            data = qr.data.decode("utf-8")
            camera.release()
            cv2.destroyAllWindows()
            return data

    for qr in pyzbar.decode(frame):
        (x,y,w,h) = qr.rect; cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        
        
        endPause()

    if cv2.waitKey(1) == ord('q'):
        break
        
camera.release()
cv2.destroyAllWindows()
dd = endPause()
print("QR code read successfully: " + str(dd))