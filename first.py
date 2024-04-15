import cvzone.SerialModule
from cvzone.HandTrackingModule import HandDetector
import cv2

# Starting the video capture from the default camera (0)
cap = cv2.VideoCapture(0)

# Creating an instance of HandDetector with detection confidence threshold 1 and maximum hands to detect set to 2
detector = HandDetector(detectionCon=1, maxHands=2)

# Creating a SerialObject instance with the specified port ("/dev/cu.usbserial-110")
ser = cvzone.SerialModule.SerialObject("/dev/cu.usbserial-110")

while True:
    # Get image frame
    success, img = cap.read()

    # Find the hand and its landmarks
    hands, img = detector.findHands(img)

    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]
        bbox1 = hand1["bbox"]
        centerPoint1 = hand1['center']
        handType1 = hand1["type"]

        fingers1 = detector.fingersUp(hand1)
        print(fingers1)
        ser.sendData(fingers1)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
