import cv2
import numpy as np

def emptyFunction():
	pass

def main():
	windowName = "Color Tracking"
	cv2.namedWindow(windowName)
  #Capturing live video
	cap = cv2.VideoCapture(0)

	if cap.isOpened():
		ret, frame = cap.read()
	else:
		ret = False
  #Lower values - BGR
	cv2.createTrackbar('low_B', windowName, 0, 255, emptyFunction)
	cv2.createTrackbar('low_G', windowName, 0, 255, emptyFunction)
	cv2.createTrackbar('low_R', windowName, 0, 255, emptyFunction)

  #Higher value - BGR
	cv2.createTrackbar('high_B', windowName, 0, 255, emptyFunction)
	cv2.setTrackbarPos('high_B', windowName, 255)
	cv2.createTrackbar('high_G', windowName, 0, 255, emptyFunction)
	cv2.setTrackbarPos('high_G', windowName, 255)
	cv2.createTrackbar('high_R', windowName, 0, 255, emptyFunction)
	cv2.setTrackbarPos('high_R', windowName, 255)

	while ret:
		ret, frame = cap.read()

		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

		low_blue = cv2.getTrackbarPos('low_B', windowName)
		low_green = cv2.getTrackbarPos('low_G', windowName)
		low_red = cv2.getTrackbarPos('low_R', windowName)

		high_blue = cv2.getTrackbarPos('high_B', windowName)
		high_green = cv2.getTrackbarPos('high_G', windowName)
		high_red = cv2.getTrackbarPos('high_R', windowName)

		low = np.array([low_blue, low_green, low_red])
		high = np.array([high_blue, high_green, high_red])
    
    '''
		Blue Color
		Low values(100, 50, 50)
		High values(140, 255, 255)

		Green Color
		Low values(40, 50, 50)
		High values(80, 255, 255)

		Red Color
		Low values(140, 150, 50)
		High values(180, 255, 255)
    '''
    
		image_mask = cv2.inRange(hsv, low, high)

		output = cv2.bitwise_and(frame, frame, mask = image_mask)

		cv2.imshow(windowName, output)	#Main Window
		cv2.imshow("Binary Masked", image_mask) #Window for Binary Masked Live Video
		cv2.imshow("Original", frame)	#Window for Original Live Video
		if cv2.waitKey(1) == 27:
			break

	cv2.destroyAllWindows()
	cap.release()

if __name__ == "__main__":
	main()
  
