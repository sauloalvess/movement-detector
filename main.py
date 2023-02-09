import cv2
import winsound

cam = cv2.VideoCapture(0)

while cam.isOpened():
    ret, frame1 = cam.read() #reads one frame
    ret, frame2 = cam.read() #reads the next frame
    diff = cv2.absdiff(frame1, frame2) #compares the two frames
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY) #converts the video to gray
    blur = cv2.GaussianBlur(gray, (5, 5), 0) #blur
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY) #getting rid of noises
    dilated = cv2.dilate(thresh, None, iterations=3) #dilates the threshold
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #finding the contours
    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    for c in contours:
        if cv2.contourArea(c) < 5000: #counts only big contours
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0, 255, 0), 2) #draws the rectangle in the contour
        winsound.Beep(500, 200)

    if cv2.waitKey(10) == ord('q'): #if presses Q, quits the program
        break

    cv2.imshow('Webcam', frame1) #displays the frame
