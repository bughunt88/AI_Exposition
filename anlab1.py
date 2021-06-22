import cv2

def Detect(img, cascade):
    
    img = cv2.resize(img, dsize=None, fx=0.5, fy=0.5)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    results = cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5, minSize=(20,20))

    for box in results:
        x,y,w,h = box
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,255,255), thickness=2)

    cv2.imshow('facenet', img)
    cv2.waitKey(10000)
    

cascade_filename = 'C:/Study/anlab/haarcascade_frontalface_alt.xml'
cascade = cv2.CascadeClassifier(cascade_filename)

img = cv2.imread('C:/Study/anlab/image_00000388608754.jpg')

Detect(img, cascade)