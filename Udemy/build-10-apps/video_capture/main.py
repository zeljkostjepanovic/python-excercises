import cv2, time

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Cam", gray)
    key = cv2.waitKey(20)

    if key == ord('q'):
        break


video.release()
cv2.destroyAllWindows

