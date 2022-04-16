from firebase_admin import credentials,storage
import firebase_admin
from time import sleep
from datetime import datetime
import os
import cv2

Id = credentials.Certificate(r'./dosya_adi.json')
app = firebase_admin.initialize_app(Id)

storage=firebase_admin.storage

cap=cv2.VideoCapture(0)
while True:

    _, frame = cap.read()

    cv2.imshow("frame", frame)


    now = datetime.now()
    dt = now.strftime("%d%m%Y%H:%M:%S")
    name = dt + ".jpg"
    cap.capture(name)
    print(name + " saved")
    storage.bucket(name).put(name)
    print("Image sent")
    os.remove(name)
    print("File Removed")
    sleep(2)

    if cv2.waitKey(1) & 0xff == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()


