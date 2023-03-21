import cv2

face_cascade=cv2.CascadeClassifier(r"C:\Users\KIIT\AppData\Roaming\Python\Python310\site-packages\cv2\data\haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)

while 1:
    ret,img=cap.read()
    color=cv2.cvtColor(img,cv2.COLOR_BGR2RGBA)
    faces=face_cascade.detectMultiScale(color,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

